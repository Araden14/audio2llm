<script lang="ts">
    import { getContext, createEventDispatcher } from 'svelte';
    import type { Writable } from 'svelte/store';

    const dispatch = createEventDispatcher();
    const state = getContext('state') as {
        showRecordingPreview: Writable<boolean>;
        recordingDuration: Writable<string>;
        currentAudioBlob: Writable<Blob | null>;
        status: Writable<string>;
    };
    const { showRecordingPreview, recordingDuration, currentAudioBlob, status } = state;

    let audioPreviewSrc = '';
    currentAudioBlob.subscribe(blob => {
        if (audioPreviewSrc) {
            URL.revokeObjectURL(audioPreviewSrc);
        }
        if (blob) {
            audioPreviewSrc = URL.createObjectURL(blob);
        }
    });

    function discardRecording() {
        showRecordingPreview.set(false);
        if (audioPreviewSrc) {
            URL.revokeObjectURL(audioPreviewSrc);
        }
        currentAudioBlob.set(null);
        status.set('Enregistrement supprimé');
        setTimeout(() => {
            status.set('');
        }, 2000);
    }

    function sendAudio() {
        dispatch('sendAudio');
    }

</script>

{#if $showRecordingPreview}
<div class="recording-preview">
    <div class="preview-header">
        <h3>🎵 Enregistrement terminé</h3>
        <div class="recording-info">
            <span class="recording-duration">{$recordingDuration}</span>
        </div>
    </div>
    
    <div class="audio-player">
        <audio controls src={audioPreviewSrc} class="audio-control">
            Votre navigateur ne supporte pas l'élément audio.
        </audio>
    </div>

    <div class="action-buttons">
        <button class="btn btn-discard" on:click={discardRecording}>
            <span class="btn-icon">🗑️</span>
            <span class="btn-text">Supprimer</span>
        </button>
        <button class="btn btn-send" on:click={() => dispatch('sendAudio')}>
            <span class="btn-icon">🚀</span>
            <span class="btn-text">Envoyer à l'IA</span>
        </button>
    </div>
</div>
{/if}

<style>
    .btn {
        padding: 12px 30px;
        border: none;
        border-radius: 50px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
        min-width: 150px;
    }
    .recording-preview {
        margin-top: 25px;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 16px;
        padding: 25px;
        border: 2px solid #e1e5e9;
        animation: slideIn 0.3s ease-out;
    }

    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .preview-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }

    .preview-header h3 {
        color: #333;
        font-size: 18px;
        font-weight: 600;
        margin: 0;
    }

    .recording-info {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .recording-duration {
        background: #667eea;
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 14px;
        font-weight: 500;
        font-family: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', monospace;
    }

    .audio-player {
        margin-bottom: 20px;
        text-align: center;
    }

    .audio-control {
        width: 100%;
        max-width: 400px;
        border-radius: 8px;
        outline: none;
    }

    .action-buttons {
        display: flex;
        gap: 15px;
        justify-content: center;
    }

    .btn-discard {
        background: linear-gradient(135deg, #6c757d 0%, #495057 100%);
        color: white;
        border: none;
        display: flex;
        align-items: center;
        gap: 8px;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .btn-discard:hover {
        background: linear-gradient(135deg, #5a6268 0%, #3d4246 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(108, 117, 125, 0.3);
    }

    .btn-discard:active {
        transform: translateY(0);
        box-shadow: 0 4px 15px rgba(108, 117, 125, 0.2);
    }

    .btn-send {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        color: white;
        border: none;
        display: flex;
        align-items: center;
        gap: 8px;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .btn-send:hover {
        background: linear-gradient(135deg, #218838 0%, #1cc88a 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(40, 167, 69, 0.3);
    }

    .btn-send:active {
        transform: translateY(0);
        box-shadow: 0 4px 15px rgba(40, 167, 69, 0.2);
    }

    .btn-icon {
        font-size: 18px;
        display: flex;
        align-items: center;
    }

    .btn-text {
        font-weight: 600;
        font-size: 15px;
    }

    /* Button ripple effect */
    .btn-discard::before,
    .btn-send::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.3s, height 0.3s;
    }

    .btn-discard:active::before,
    .btn-send:active::before {
        width: 100px;
        height: 100px;
    }
</style>
