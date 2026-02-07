<script>
    import { onMount } from "svelte";
    import Fuse from "fuse.js";
    import navData from "../nav.json";
    import examplesData from "../../data/examples.json";

    let query = "";
    let results = [];
    let fuse;
    let isFocused = false;

    // Prepare search index
    const searchIndex = [];

    // Add navigation items
    navData.forEach((section) => {
        section.items.forEach((item) => {
            searchIndex.push({
                title: item.title,
                path: item.path,
                type: "Page",
                section: section.section,
            });
        });
    });

    // Add code examples
    Object.entries(examplesData).forEach(([key, data]) => {
        // Extract a clean title from the key (e.g., load_csv_pandas -> CSV Loading (Pandas))
        const parts = key.split("_");
        const type = parts[1].toUpperCase();
        const lib = parts[2]
            ? parts[2].charAt(0).toUpperCase() + parts[2].slice(1)
            : "";
        const title = `${type} ${lib ? "(" + lib + ")" : ""}`;

        // Find the page path based on the key prefix
        const pagePath = `/load/${parts[1]}`; // Simplified heuristic

        searchIndex.push({
            title: title,
            path: pagePath,
            type: "Example",
            section: "Code Snippets",
            content: data.code.substring(0, 200), // Some context
        });
    });

    onMount(() => {
        fuse = new Fuse(searchIndex, {
            keys: ["title", "section", "content"],
            threshold: 0.3,
            includeMatches: true,
        });
    });

    $: {
        if (fuse && query) {
            results = fuse.search(query).slice(0, 8);
        } else {
            results = [];
        }
    }

    function handleKeydown(e) {
        if (e.key === "Escape") {
            query = "";
            isFocused = false;
        }
    }
</script>

<div class="search-container" role="search" on:keydown={handleKeydown}>
    <div class="search-input-wrapper" class:focused={isFocused}>
        <span class="search-icon">🔍</span>
        <input
            type="text"
            placeholder="Search docs (e.g. 'csv', 'parquet')"
            bind:value={query}
            on:focus={() => (isFocused = true)}
            on:blur={() => setTimeout(() => (isFocused = false), 200)}
        />
    </div>

    {#if isFocused && results.length > 0}
        <div class="search-results">
            {#each results as result}
                <a
                    href={result.item.path}
                    class="result-item"
                    on:click={() => (query = "")}
                >
                    <div class="result-info">
                        <span class="result-title">{result.item.title}</span>
                        <span class="result-meta">{result.item.section}</span>
                    </div>
                    <span
                        class="result-type"
                        class:page={result.item.type === "Page"}
                    >
                        {result.item.type}
                    </span>
                </a>
            {/each}
        </div>
    {:else if isFocused && query.length > 2 && results.length === 0}
        <div class="search-results no-results">
            No results found for "{query}"
        </div>
    {/if}
</div>

<style>
    .search-container {
        position: relative;
        width: 100%;
        max-width: 400px;
    }

    .search-input-wrapper {
        display: flex;
        align-items: center;
        background: var(--bg-tertiary);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 0 0.75rem;
        transition: all 0.2s;
    }

    .search-input-wrapper.focused {
        border-color: var(--accent-blue);
        box-shadow: 0 0 0 2px rgba(66, 133, 244, 0.2);
        background: var(--bg-primary);
    }

    .search-icon {
        font-size: 0.875rem;
        opacity: 0.5;
    }

    input {
        width: 100%;
        padding: 0.5rem 0.75rem;
        background: transparent;
        border: none;
        color: var(--text-primary);
        font-size: 0.875rem;
        outline: none;
    }

    .search-results {
        position: absolute;
        top: calc(100% + 0.5rem);
        left: 0;
        right: 0;
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        z-index: 1000;
        max-height: 400px;
        overflow-y: auto;
    }

    .no-results {
        padding: 1rem;
        font-size: 0.875rem;
        color: var(--text-muted);
        text-align: center;
    }

    .result-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.75rem 1rem;
        text-decoration: none;
        color: var(--text-primary);
        border-bottom: 1px solid var(--border-color);
        transition: background 0.15s;
    }

    .result-item:last-child {
        border-bottom: none;
    }

    .result-item:hover {
        background: var(--bg-secondary);
    }

    .result-info {
        display: flex;
        flex-direction: column;
        gap: 0.15rem;
    }

    .result-title {
        font-size: 0.875rem;
        font-weight: 500;
    }

    .result-meta {
        font-size: 0.75rem;
        color: var(--text-muted);
    }

    .result-type {
        font-size: 0.65rem;
        font-weight: 700;
        text-transform: uppercase;
        padding: 0.15rem 0.4rem;
        border-radius: 4px;
        background: #1e293b;
        color: #94a3b8;
    }

    .result-type.page {
        background: #0f172a;
        color: #38bdf8;
    }

    @media (max-width: 900px) {
        .search-container {
            max-width: none;
            margin-bottom: 1rem;
        }
    }
</style>
