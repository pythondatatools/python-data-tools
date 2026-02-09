<script>
    import CodeTabs from "$lib/components/CodeTabs.svelte";
    import Icon from "$lib/components/Icon.svelte";
    import examples from "../../../data/examples.json";
</script>

<div class="page">
    <div class="page-header">
        <div class="breadcrumb">
            <span>Transform</span>
            <span class="sep">/</span>
            <span class="current">Joins & Merges</span>
        </div>
        <h1>Joins & Merges</h1>
        <p class="intro">
            Combining datasets is where the real power of data science begins.
            Learn how to use Inner, Left, and Outer joins to unify your data.
        </p>
    </div>

    <section class="quick-ref">
        <h2>Quick Reference</h2>
        <div class="ref-grid">
            <div class="ref-card pandas">
                <Icon name="pandas" size={20} color="var(--pandas-color)" />
                <div class="ref-content">
                    <code>pd.merge(df1, df2, on='id')</code>
                    <span class="ref-note"
                        >Versatile <code>merge</code> function</span
                    >
                </div>
            </div>
            <div class="ref-card polars">
                <Icon name="polars" size={20} color="var(--polars-color)" />
                <div class="ref-content">
                    <code>df1.join(df2, on='id')</code>
                    <span class="ref-note"
                        >Intuitive <code>.join()</code> method</span
                    >
                </div>
            </div>
            <div class="ref-card duckdb">
                <Icon name="duckdb" size={20} color="var(--duckdb-color)" />
                <div class="ref-content">
                    <code>SELECT * FROM A JOIN B ON ...</code>
                    <span class="ref-note">Standard SQL syntax</span>
                </div>
            </div>
        </div>
    </section>

    <section class="visual-explainer">
        <h2>Visualizing Joins</h2>
        <div class="join-visuals">
            <div class="join-type">
                <span class="label">Inner Join</span>
                <div class="venn">
                    <div class="circle left"></div>
                    <div class="circle right"></div>
                    <div class="overlap"></div>
                </div>
                <span class="note">Matches only</span>
            </div>
            <div class="join-type">
                <span class="label">Left Join</span>
                <div class="venn">
                    <div class="circle left active"></div>
                    <div class="circle right"></div>
                    <div class="overlap active"></div>
                </div>
                <span class="note">All from Left</span>
            </div>
            <div class="join-type">
                <span class="label">Full Join</span>
                <div class="venn">
                    <div class="circle left active"></div>
                    <div class="circle right active"></div>
                    <div class="overlap active"></div>
                </div>
                <span class="note">Everything</span>
            </div>
        </div>
    </section>

    <section class="examples">
        <h2>Full Examples</h2>
        <p class="section-intro">
            Examples using a custom <strong>Employees & Departments</strong> dataset.
        </p>
        <CodeTabs {examples} task="transform_join" section="transform" />
    </section>
</div>

<style>
    .page {
        max-width: 900px;
    }

    .page-header {
        margin-bottom: var(--space-8);
    }

    .breadcrumb {
        display: flex;
        align-items: center;
        gap: var(--space-2);
        font-size: 0.8rem;
        color: var(--text-muted);
        margin-bottom: var(--space-3);
    }

    .breadcrumb .sep {
        color: var(--border-color);
    }
    .breadcrumb .current {
        color: var(--accent-primary);
    }

    h1 {
        font-size: 2.25rem;
        margin-bottom: var(--space-3);
    }

    .intro {
        font-size: 1.1rem;
        color: var(--text-secondary);
        max-width: 650px;
    }

    section {
        margin-bottom: var(--space-10);
    }

    h2 {
        font-size: 1.25rem;
        margin-bottom: var(--space-4);
        margin-top: 0;
    }

    .section-intro {
        font-size: 0.9rem;
        color: var(--text-muted);
        margin-bottom: var(--space-4);
    }

    /* Quick Ref Grid */
    .ref-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: var(--space-3);
    }

    .ref-card {
        display: flex;
        align-items: flex-start;
        gap: var(--space-3);
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-md);
        padding: var(--space-4);
    }

    .ref-content {
        display: flex;
        flex-direction: column;
        gap: var(--space-1);
    }

    .ref-card code {
        font-size: 0.8rem;
        color: var(--text-primary);
        background: transparent;
        padding: 0;
    }

    .ref-note {
        font-size: 0.7rem;
        color: var(--text-muted);
    }

    .ref-card.pandas {
        border-left: 3px solid var(--pandas-color);
    }
    .ref-card.polars {
        border-left: 3px solid var(--polars-color);
    }
    .ref-card.duckdb {
        border-left: 3px solid var(--duckdb-color);
    }

    /* Venn Diagrams */
    .join-visuals {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: var(--space-6);
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: var(--space-8);
        text-align: center;
    }

    .join-type {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: var(--space-3);
    }

    .label {
        font-size: 0.8rem;
        font-weight: 600;
        color: var(--text-primary);
    }

    .note {
        font-size: 0.7rem;
        color: var(--text-muted);
    }

    .venn {
        position: relative;
        width: 80px;
        height: 50px;
    }

    .circle {
        position: absolute;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        border: 2px solid var(--border-color);
        background: transparent;
    }

    .circle.left {
        left: 0;
    }
    .circle.right {
        right: 0;
    }

    .circle.active {
        background: rgba(124, 58, 237, 0.1);
        border-color: var(--accent-primary);
    }

    .overlap {
        position: absolute;
        left: 25px;
        width: 30px;
        height: 50px;
        overflow: hidden;
    }

    .overlap.active::before {
        content: "";
        position: absolute;
        left: -25px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: var(--accent-primary);
        opacity: 0.4;
    }
</style>
