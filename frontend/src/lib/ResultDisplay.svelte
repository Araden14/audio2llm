<script lang="ts">
    import { getContext, onMount } from 'svelte';
    import type { Writable } from 'svelte/store';
    import { marked } from 'marked';

    const state = getContext('state') as {
        llmResponse: Writable<string>;
        responseStatus: Writable<string>;
    };
    const { llmResponse, responseStatus } = state;

    let resultContent: HTMLElement;

    llmResponse.subscribe(value => {
        if (resultContent) {
            if (value) {
                resultContent.innerHTML = `<div class="markdown-content">${marked.parse(value)}</div>`;
                resultContent.classList.remove('empty');
            } else {
                resultContent.innerHTML = `
                    <div class="empty-icon">🎤</div>
                    <div>Enregistrez un audio pour voir la réponse ici</div>
                `;
                resultContent.classList.add('empty');
            }
        }
    });
</script>

<div class="result-container">
    <div class="result-header">
        <h2 class="result-title">Réponse du LLM</h2>
        <div class="result-status">{@html $responseStatus || ''}</div>
    </div>
    <div class="result-content empty" bind:this={resultContent}>
        <div class="empty-icon">🎤</div>
        <div>Enregistrez un audio pour voir la réponse ici</div>
    </div>
</div>

<style>
    .result-container {
        flex: 1;
        display: flex;
        flex-direction: column;
    }

    .result-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 2px solid #e1e5e9;
    }

    .result-title {
        color: #333;
        font-size: 22px;
        font-weight: 600;
        margin: 0;
    }

    .result-status {
        display: flex;
        align-items: center;
        gap: 8px;
        color: #666;
        font-size: 14px;
    }

    .result-content {
        flex: 1;
        background: #f8f9fa;
        border-radius: 12px;
        padding: 25px;
        overflow-y: auto;
        min-height: 300px;
        border: 1px solid #e1e5e9;
    }

    .result-content.empty {
        display: flex;
        align-items: center;
        justify-content: center;
        color: #999;
        font-style: italic;
        flex-direction: column;
        gap: 10px;
    }

    .result-content.empty .empty-icon {
        font-size: 48px;
        opacity: 0.3;
    }

    /* Markdown styling */
    :global(.markdown-content h1),
    :global(.markdown-content h2),
    :global(.markdown-content h3),
    :global(.markdown-content h4),
    :global(.markdown-content h5),
    :global(.markdown-content h6) {
        color: #333;
        margin: 20px 0 10px 0;
        line-height: 1.4;
    }

    :global(.markdown-content h1) { font-size: 24px; border-bottom: 2px solid #667eea; padding-bottom: 8px; }
    :global(.markdown-content h2) { font-size: 20px; }
    :global(.markdown-content h3) { font-size: 18px; }

    :global(.markdown-content p) {
        color: #555;
        line-height: 1.7;
        margin: 12px 0;
    }

    :global(.markdown-content ul),
    :global(.markdown-content ol) {
        color: #555;
        line-height: 1.6;
        margin: 12px 0;
        padding-left: 20px;
    }

    :global(.markdown-content li) {
        margin: 6px 0;
    }

    :global(.markdown-content code) {
        background: #f1f3f4;
        padding: 2px 6px;
        border-radius: 4px;
        font-family: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', monospace;
        font-size: 14px;
        color: #d73a49;
    }

    :global(.markdown-content pre) {
        background: #f6f8fa;
        border: 1px solid #e1e4e8;
        border-radius: 8px;
        padding: 16px;
        overflow-x: auto;
        margin: 16px 0;
    }

    :global(.markdown-content pre code) {
        background: none;
        padding: 0;
        color: #24292e;
        font-size: 13px;
    }

    :global(.markdown-content blockquote) {
        border-left: 4px solid #667eea;
        margin: 16px 0;
        padding-left: 16px;
        color: #666;
        font-style: italic;
    }

    :global(.markdown-content a) {
        color: #667eea;
        text-decoration: none;
    }

    :global(.markdown-content a:hover) {
        text-decoration: underline;
    }

    :global(.markdown-content strong) {
        font-weight: 600;
        color: #333;
    }
</style>
