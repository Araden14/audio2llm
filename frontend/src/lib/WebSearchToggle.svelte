<script lang="ts">
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';

    const state = getContext('state') as {
        webSearchEnabled: Writable<boolean>;
    };
    const { webSearchEnabled } = state;
</script>

<div class="web-search-container">
    <div class="web-search-toggle">
        <label class="toggle-label">
            <input type="checkbox" bind:checked={$webSearchEnabled} class="toggle-input">
            <span class="toggle-slider"></span>
            <span class="toggle-text">🔍 Recherche Web</span>
        </label>
        <div class="web-search-info">
            <small>Ajoute des données web en temps réel aux réponses</small>
        </div>
    </div>
</div>

<style>
    .web-search-container {
        margin-bottom: 20px;
    }

    .web-search-toggle {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .toggle-label {
        position: relative;
        display: flex;
        align-items: center;
        cursor: pointer;
        font-size: 16px;
        font-weight: 500;
        color: #555;
        user-select: none;
    }

    .toggle-input {
        position: absolute;
        opacity: 0;
        cursor: pointer;
        height: 0;
        width: 0;
    }

    .toggle-slider {
        position: relative;
        display: inline-block;
        width: 50px;
        height: 24px;
        background-color: #ccc;
        border-radius: 24px;
        transition: .4s;
        margin-right: 10px;
    }

    .toggle-slider:before {
        position: absolute;
        content: "";
        height: 18px;
        width: 18px;
        left: 3px;
        bottom: 3px;
        background-color: white;
        border-radius: 50%;
        transition: .4s;
    }

    .toggle-input:checked + .toggle-slider {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    .toggle-input:checked + .toggle-slider:before {
        transform: translateX(26px);
    }

    .toggle-text {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .web-search-info {
        flex: 1;
    }

    .web-search-info small {
        color: #666;
        font-size: 13px;
        line-height: 1.4;
    }
</style>
