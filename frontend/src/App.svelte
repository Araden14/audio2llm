<script lang="ts">
  import LeftPanel from './lib/LeftPanel.svelte';
  import RightPanel from './lib/RightPanel.svelte';
  import { setContext } from 'svelte';
  import { get } from 'svelte/store';
  import { writable } from 'svelte/store';

  const state = {
    prompt: writable(''),
    selectedModel: writable('google/gemini-2.5-flash'),
    webSearchEnabled: writable(false),
    isRecording: writable(false),
    status: writable(''),
    llmResponse: writable(''),
    responseStatus: writable(''),
    currentAudioBlob: writable<Blob | null>(null),
    showRecordingPreview: writable(false),
    recordingDuration: writable('0:00')
  };

  setContext('state', state);

  let mediaRecorder: MediaRecorder;
  let audioChunks: Blob[] = [];
  let recordingStartTime = 0;

  async function startRecording() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorder = new MediaRecorder(stream);
      audioChunks = [];
      recordingStartTime = Date.now();
      
      mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
      };
      
      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
        state.currentAudioBlob.set(audioBlob);
        
        const duration = (Date.now() - recordingStartTime) / 1000;
        const minutes = Math.floor(duration / 60);
        const seconds = Math.floor(duration % 60);
        state.recordingDuration.set(`${minutes}:${seconds.toString().padStart(2, '0')}`);
        
        state.showRecordingPreview.set(true);
      };
      
      mediaRecorder.start();
      state.isRecording.set(true);
      state.status.set('Enregistrement en cours...');
      state.showRecordingPreview.set(false);
      state.llmResponse.set('');
      state.responseStatus.set('');
      
    } catch (error) {
      state.status.set("Erreur: Impossible d'accéder au microphone");
      console.error('Erreur:', error);
    }
  }

  function stopRecording() {
    if (mediaRecorder && mediaRecorder.state !== 'inactive') {
      mediaRecorder.stop();
      mediaRecorder.stream.getTracks().forEach(track => track.stop());
      state.isRecording.set(false);
      state.status.set('Enregistrement terminé');
    }
  }

  async function toggleRecording() {
    const isRecording = get(state.isRecording);
    if (!isRecording) {
      await startRecording();
    } else {
      stopRecording();
    }
  }

  async function sendAudioToServer() {
    const audioBlob = get(state.currentAudioBlob);
    if (!audioBlob) {
        state.status.set('Aucun enregistrement à envoyer');
        return;
    }

    try {
        state.showRecordingPreview.set(false);

        state.responseStatus.set('<span class="loading"></span> Analyse en cours...');
        state.llmResponse.set('');

        const formData = new FormData();
        formData.append('audio', audioBlob, 'recording.webm');
        formData.append('prompt', get(state.prompt) || 'Vous êtes un assistant utile. Écoutez attentivement cette audio et comprenez ce que l\'utilisateur demande. Répondez ensuite de manière appropriée et utile à la demande formulée dans l\'audio. Ne vous contentez pas de répéter ce qui est dit, mais fournissez une vraie réponse à la question ou à la demande.');
        formData.append('model', get(state.selectedModel));
        formData.append('web_search_enabled', get(state.webSearchEnabled).toString());

        const API_URL = 'http://localhost:8000/process-audio';
        const fetchResponse = await fetch(API_URL, {
            method: 'POST',
            body: formData
        });

        if (!fetchResponse.ok) {
            throw new Error(`Erreur serveur: ${fetchResponse.status}`);
        }

        const data = await fetchResponse.json();

        state.llmResponse.set(data.response || 'Aucune réponse disponible');

        let statusText = 'Analyse terminée ✓';
        if (data.model) {
            const modelName = data.model.split('/').pop().replace(/-/g, ' ');
            statusText += ` • ${modelName}`;
        }
        if (data.web_search_enabled) {
            statusText += ' • 🔍 Web';
        }
        if (data.usage && data.usage.total_tokens) {
            statusText += ` • ${data.usage.total_tokens} tokens`;
        }

        state.responseStatus.set(statusText);
        state.status.set('Analyse terminée ✓');

        state.currentAudioBlob.set(null);

    } catch (error) {
        const errorMessage = error instanceof Error ? error.message : 'Erreur inconnue';
        state.llmResponse.set(`<div class="empty-icon">❌</div><div style="color: #ef4444;">Erreur: ${errorMessage}</div>`);
        state.responseStatus.set('❌ Erreur');
        state.status.set(`Erreur: ${errorMessage}`);
        console.error('Erreur:', error);
    }
  }

</script>

<div class="app-container">
  <LeftPanel {toggleRecording} on:sendAudio={sendAudioToServer} />
  <RightPanel />
</div>

<style>
  .app-container {
    display: flex;
    gap: 30px;
    max-width: 1400px;
    margin: 0 auto;
    min-height: calc(100vh - 40px);
  }

  @media (max-width: 1200px) {
    .app-container {
      flex-direction: column;
      gap: 20px;
    }
  }
</style>
