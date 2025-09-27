<script lang="ts">
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';

    const state = getContext('state') as {
        prompt: Writable<string>;
    };
    const { prompt } = state;
</script>

<div class="prompt-container">
  <label for="prompt" class="prompt-label">Que voulez-vous demander à propos de cet audio ?</label>
  <textarea bind:value={$prompt} class="prompt-input" placeholder="Ex: Raconte une histoire drôle, Traduis en anglais, Résume ce texte, Réponds à cette question, etc. (laissez vide pour réponse automatique)"></textarea>
</div>

<style>
  .prompt-container {
    margin-bottom: 20px;
  }

  .prompt-label {
    display: block;
    color: #555;
    margin-bottom: 8px;
    font-weight: 500;
  }

  .prompt-input {
    width: 100%;
    padding: 12px;
    border: 2px solid #e1e5e9;
    border-radius: 8px;
    font-size: 16px;
    font-family: inherit;
    resize: vertical;
    min-height: 80px;
  }

  .prompt-input:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
  }
</style>
