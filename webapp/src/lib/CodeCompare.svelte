<!--
  CodeCompare.svelte
  Side-by-side code comparison component
  Supports: pandas, duckdb, bigquery, polars (extensible)
-->
<script>
  export let examples = [];
  export let title = '';
  export let description = '';
  
  // Platforms configuration (extensible)
  const platforms = {
    pandas: { name: 'Pandas', icon: '🐼', color: '#150458' },
    duckdb: { name: 'DuckDB', icon: '🦆', color: '#fff100' },
    bigquery: { name: 'BigQuery', icon: '☁️', color: '#4285f4' },
    polars: { name: 'Polars', icon: '🐻‍❄️', color: '#cd792c' },
    // Future platforms can be added here
    // ibis: { name: 'Ibis', icon: '🔄', color: '#...' },
    // chdb: { name: 'chDB', icon: '⚡', color: '#...' },
  };
  
  let selectedPlatforms = ['pandas', 'duckdb', 'bigquery', 'polars'];
  
  function togglePlatform(platform) {
    if (selectedPlatforms.includes(platform)) {
      if (selectedPlatforms.length > 1) {
        selectedPlatforms = selectedPlatforms.filter(p => p !== platform);
      }
    } else {
      selectedPlatforms = [...selectedPlatforms, platform];
    }
  }
  
  $: visibleExamples = examples.filter(e => selectedPlatforms.includes(e.platform));
  $: columnWidth = `${100 / visibleExamples.length}%`;
</script>

<div class="compare-section">
  {#if title}
    <h3 class="section-title">{title}</h3>
  {/if}
  
  {#if description}
    <p class="section-desc">{description}</p>
  {/if}
  
  <div class="platform-toggles">
    {#each Object.entries(platforms) as [key, platform]}
      {#if examples.some(e => e.platform === key)}
        <button 
          class="toggle-btn" 
          class:active={selectedPlatforms.includes(key)}
          style="--platform-color: {platform.color}"
          on:click={() => togglePlatform(key)}
        >
          <span class="icon">{platform.icon}</span>
          <span class="name">{platform.name}</span>
        </button>
      {/if}
    {/each}
  </div>
  
  <div class="code-panels" style="--cols: {visibleExamples.length}">
    {#each visibleExamples as example}
      <div class="code-panel" style="--platform-color: {platforms[example.platform]?.color || '#888'}">
        <div class="panel-header">
          <span class="platform-icon">{platforms[example.platform]?.icon}</span>
          <span class="platform-name">{platforms[example.platform]?.name}</span>
          {#if example.language}
            <span class="language-badge">{example.language}</span>
          {/if}
        </div>
        <pre class="code-block"><code>{example.code}</code></pre>
      </div>
    {/each}
  </div>
</div>

<style>
  .compare-section {
    margin: 2rem 0;
  }
  
  .section-title {
    margin-bottom: 0.5rem;
    color: var(--text-primary);
  }
  
  .section-desc {
    color: var(--text-secondary);
    margin-bottom: 1rem;
  }
  
  .platform-toggles {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1rem;
    flex-wrap: wrap;
  }
  
  .toggle-btn {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.5rem 1rem;
    background: var(--bg-tertiary);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    color: var(--text-secondary);
    font-size: 0.875rem;
    transition: all 0.2s;
  }
  
  .toggle-btn:hover {
    border-color: var(--platform-color);
    color: var(--text-primary);
  }
  
  .toggle-btn.active {
    background: color-mix(in srgb, var(--platform-color) 20%, transparent);
    border-color: var(--platform-color);
    color: var(--text-primary);
  }
  
  .code-panels {
    display: grid;
    grid-template-columns: repeat(var(--cols), 1fr);
    gap: 1rem;
  }
  
  @media (max-width: 1200px) {
    .code-panels {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  
  @media (max-width: 768px) {
    .code-panels {
      grid-template-columns: 1fr;
    }
  }
  
  .code-panel {
    border: 1px solid var(--border-color);
    border-radius: 8px;
    overflow: hidden;
    background: var(--bg-secondary);
  }
  
  .panel-header {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1rem;
    background: var(--bg-tertiary);
    border-bottom: 2px solid var(--platform-color);
    font-size: 0.875rem;
  }
  
  .platform-icon {
    font-size: 1.1rem;
  }
  
  .platform-name {
    font-weight: 500;
    color: var(--text-primary);
  }
  
  .language-badge {
    margin-left: auto;
    padding: 0.2rem 0.5rem;
    background: var(--bg-primary);
    border-radius: 4px;
    color: var(--text-muted);
    font-size: 0.75rem;
  }
  
  .code-block {
    margin: 0;
    border: none;
    border-radius: 0;
    background: transparent;
    min-height: 150px;
  }
</style>
