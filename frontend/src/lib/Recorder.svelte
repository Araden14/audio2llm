<script lang="ts">
	import { getContext } from 'svelte';
	import type { Writable } from 'svelte/store';

	export let toggleRecording: () => Promise<void>;

	const state = getContext('state') as {
		isRecording: Writable<boolean>;
		status: Writable<string>;
	};
	const { isRecording, status } = state;
</script>

<div class="recorder">
	<button class="btn btn-record" class:recording={$isRecording} on:click={toggleRecording}>
		{$isRecording ? 'Arrêter' : 'Enregistrer'}
	</button>
	<div class="status">{$status || ''}</div>
</div>

<style>
    .recorder {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
    }

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

    .btn-record {
        background: #667eea;
        color: white;
    }

    .btn-record:hover {
        background: #5a67d8;
        transform: translateY(-2px);
    }

    .btn-record.recording {
        background: #ef4444;
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(239, 68, 68, 0); }
        100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
    }

    .status {
        color: #666;
        font-size: 14px;
        min-height: 20px;
    }
</style>
