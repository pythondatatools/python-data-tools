<script>
    export let library = "";
    export let version = "";
</script>

<span class="version-badge">
    <span class="lib">{library}</span>
    <span class="ver">{version}</span>
</span>

<style>
    .version-badge {
        display: inline-flex;
        font-size: 0.75rem;
        border-radius: 4px;
        overflow: hidden;
        border: 1px solid var(--border-color);
    }

    .lib {
        background: var(--bg-secondary);
        color: var(--text-secondary);
        padding: 0.125rem 0.5rem;
    }

    .ver {
        background: var(--accent-blue);
        color: white;
        padding: 0.125rem 0.5rem;
        font-weight: 500;
    }
</style>
