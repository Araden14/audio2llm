<script lang="ts">
  import PromptInput from './PromptInput.svelte';
  import ModelSelect from './ModelSelect.svelte';
  import WebSearchToggle from './WebSearchToggle.svelte';
  import Recorder from './Recorder.svelte';
  import RecordingPreview from './RecordingPreview.svelte';
  import { createEventDispatcher } from 'svelte';

  export let toggleRecording: () => Promise<void>;

  const dispatch = createEventDispatcher();

  function handleSendAudio() {
    dispatch('sendAudio');
  }
</script>

<div class="left-panel">
  <h1>🎙️ Audio → LLM</h1>
  <PromptInput />
  <ModelSelect />
  <WebSearchToggle />
  <Recorder {toggleRecording} />
  <RecordingPreview on:sendAudio={handleSendAudio} />
</div>

<style>
  .left-panel {
    background: white;
    border-radius: 20px;
    padding: 40px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    flex: 0 0 500px;
    min-width: 450px;
  }

  h1 {
    text-align: center;
    color: #333;
    margin-bottom: 30px;
    font-size: 28px;
  }

  @media (max-width: 1200px) {
    .left-panel {
      flex: none;
      min-width: auto;
    }
  }
</style>
