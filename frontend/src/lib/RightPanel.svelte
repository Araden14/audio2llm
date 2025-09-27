<script lang="ts">
  import ResultDisplay from './ResultDisplay.svelte';
  import { getContext } from 'svelte';
  import type { Writable } from 'svelte/store';

  const state = getContext('state') as {
    llmResponse: Writable<string>;
    responseStatus: Writable<string>;
  };
</script>

<div class="right-panel">
  <ResultDisplay />
</div>

<style>
  .right-panel {
    background: white;
    border-radius: 20px;
    padding: 40px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    flex: 1;
    min-height: 600px;
    display: flex;
    flex-direction: column;
  }

  @media (max-width: 1200px) {
    .right-panel {
      min-height: 400px;
    }
  }
</style>
