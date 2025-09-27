<script lang="ts">
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';

    const state = getContext('state') as {
        selectedModel: Writable<string>;
    };
    const { selectedModel } = state;
</script>

<div class="model-container">
    <label for="model" class="model-label">Sélectionner le modèle :</label>
    <select bind:value={$selectedModel} class="model-select">
        <option value="google/gemini-2.0-flash-lite-001">Google: Gemini 2.0 Flash Lite ($0.075/$0.30)</option>
        <option value="google/gemini-2.0-flash-001">Google: Gemini 2.0 Flash ($0.10/$0.40)</option>
        <option value="google/gemini-2.5-flash-lite-preview-09-2025">Google: Gemini 2.5 Flash Lite Preview 09-2025 ($0.10/$0.40)</option>
        <option value="google/gemini-2.5-flash-lite">Google: Gemini 2.5 Flash Lite ($0.10/$0.40)</option>
        <option value="google/gemini-2.5-flash-lite-preview-06-17">Google: Gemini 2.5 Flash Lite Preview 06-17 ($0.10/$0.40)</option>
        <option value="google/gemini-2.5-flash">Google: Gemini 2.5 Flash ($0.30/$2.50)</option>
        <option value="google/gemini-2.5-pro">Google: Gemini 2.5 Pro ($1.25/$10.00)</option>
        <option value="google/gemini-2.5-pro-preview">Google: Gemini 2.5 Pro Preview 06-05 ($1.25/$10.00)</option>
        <option value="google/gemini-2.5-pro-preview-05-06">Google: Gemini 2.5 Pro Preview 05-06 ($1.25/$10.00)</option>
        <option value="openai/gpt-4o-audio-preview">OpenAI: GPT-4o Audio ($2.50/$10.00)</option>
    </select>
</div>

<style>
    .model-container {
        margin-bottom: 20px;
    }

    .model-label {
        display: block;
        color: #555;
        margin-bottom: 8px;
        font-weight: 500;
    }

    .model-select {
        width: 100%;
        padding: 12px;
        border: 2px solid #e1e5e9;
        border-radius: 8px;
        font-size: 16px;
        font-family: inherit;
        background-color: white;
        cursor: pointer;
    }

    .model-select:focus {
        outline: none;
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }

    .model-select option {
        padding: 10px;
        font-size: 14px;
    }
</style>
