<script>
    import CodeTabs from "$lib/components/CodeTabs.svelte";
    import Icon from "$lib/components/Icon.svelte";
    import examples from "../../../data/examples.json";
</script>

<div class="page">
    <div class="page-header">
        <div class="breadcrumb">
            <span>Load</span>
            <span class="sep">/</span>
            <span class="current">Databases</span>
        </div>
        <h1>Load from Databases</h1>
        <p class="intro">
            Reading data directly from SQL databases like PostgreSQL, MySQL, or
            SQLite is a fundamental skill. Each library has unique strengths
            here.
        </p>
    </div>

    <section class="quick-ref">
        <h2>Quick Reference</h2>
        <div class="ref-grid">
            <div class="ref-card pandas">
                <Icon name="pandas" size={20} color="var(--pandas-color)" />
                <div class="ref-content">
                    <code>pd.read_sql(query, conn)</code>
                    <span class="ref-note">Standard & reliable</span>
                </div>
            </div>
            <div class="ref-card polars">
                <Icon name="polars" size={20} color="var(--polars-color)" />
                <div class="ref-content">
                    <code>pl.read_database_uri()</code>
                    <span class="ref-note">High-perf w/ ConnectorX</span>
                </div>
            </div>
            <div class="ref-card duckdb">
                <Icon name="duckdb" size={20} color="var(--duckdb-color)" />
                <div class="ref-content">
                    <code>duckdb.sql("SELECT ...")</code>
                    <span class="ref-note">Query files directly</span>
                </div>
            </div>
            <div class="ref-card bigquery">
                <Icon name="cloud" size={20} color="var(--bigquery-color)" />
                <div class="ref-content">
                    <code>EXTERNAL_QUERY()</code>
                    <span class="ref-note">Federated queries</span>
                </div>
            </div>
        </div>
    </section>

    <section class="examples">
        <h2>Full Examples</h2>
        <p class="section-intro">
            These examples use a local SQLite database that is <strong
                >automatically created</strong
            > when you run the script.
        </p>
        <CodeTabs {examples} task="load_database" section="load" />
    </section>

    <section class="enterprise">
        <h2>Enterprise Connectors</h2>
        <p class="section-intro">
            Corporate environments often use Postgres, SQL Server, or DB2. Here
            are the standard connection strings for each.
        </p>
        <div class="ent-grid">
            <div class="ent-card postgres">
                <div class="ent-header">
                    <Icon name="database" size={20} />
                    <h3>PostgreSQL</h3>
                </div>
                <code>postgresql://user:pass@localhost:5432/mydb</code>
                <span class="ent-note"
                    >Best with <strong>psycopg2</strong> driver</span
                >
            </div>
            <div class="ent-card mssql">
                <div class="ent-header">
                    <Icon name="database" size={20} />
                    <h3>SQL Server</h3>
                </div>
                <code>mssql+pyodbc://user:pass@server/db?driver=ODBC...</code>
                <span class="ent-note"
                    >Requires <strong>pyodbc</strong> driver</span
                >
            </div>
            <div class="ent-card db2">
                <div class="ent-header">
                    <Icon name="database" size={20} />
                    <h3>IBM DB2</h3>
                </div>
                <code>ibm_db_sa://user:pass@host:50000/mydb</code>
                <span class="ent-note">Requires <strong>ibm_db_sa</strong></span
                >
            </div>
        </div>
    </section>

    <section class="when-to-use">
        <h2>Key Differences</h2>
        <div class="when-grid">
            <div class="when-card">
                <div class="when-header">
                    <Icon name="pandas" size={24} color="var(--pandas-color)" />
                    <h3>Pandas</h3>
                </div>
                <ul>
                    <li>
                        Uses standard connectors like <code>psycopg2</code> or
                        <code>sqlalchemy</code>
                    </li>
                    <li>Slower for very large result sets</li>
                    <li>Best for legacy compatibility</li>
                </ul>
            </div>
            <div class="when-card">
                <div class="when-header">
                    <Icon name="polars" size={24} color="var(--polars-color)" />
                    <h3>Polars</h3>
                </div>
                <ul>
                    <li>
                        Uses <code>adbc</code> or <code>connectorx</code> drivers
                    </li>
                    <li>Significantly faster (multi-threaded reads)</li>
                    <li>Direct-to-Arrow memory mapping</li>
                </ul>
            </div>
            <div class="when-card">
                <div class="when-header">
                    <Icon name="duckdb" size={24} color="var(--duckdb-color)" />
                    <h3>DuckDB</h3>
                </div>
                <ul>
                    <li>
                        Can query databases <strong>without moving data</strong>
                    </li>
                    <li>
                        Supports "Federated Queries" (join Postgres + MySQL +
                        CSV)
                    </li>
                    <li>Reads SQLite files directly from disk (zero-copy)</li>
                </ul>
            </div>
        </div>
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
    .ref-card.bigquery {
        border-left: 3px solid var(--bigquery-color);
    }

    .when-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: var(--space-4);
    }

    .when-card {
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: var(--space-5);
    }

    .when-header {
        display: flex;
        align-items: center;
        gap: var(--space-3);
        margin-bottom: var(--space-4);
    }

    .when-header h3 {
        font-size: 1rem;
        margin: 0;
    }

    .when-card ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }

    .when-card li {
        font-size: 0.85rem;
        color: var(--text-secondary);
        padding: var(--space-1) 0;
        padding-left: var(--space-4);
        position: relative;
    }

    .when-card li::before {
        content: "•";
        position: absolute;
        left: 0;
        color: var(--accent-primary);
    }

    .ent-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: var(--space-4);
    }

    .ent-card {
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-md);
        padding: var(--space-4);
    }

    .ent-header {
        display: flex;
        align-items: center;
        gap: var(--space-2);
        margin-bottom: var(--space-3);
    }

    .ent-header h3 {
        font-size: 1rem;
        margin: 0;
    }

    .ent-card code {
        display: block;
        font-size: 0.75rem;
        background: var(--bg-tertiary);
        padding: var(--space-2);
        border-radius: var(--radius-sm);
        margin-bottom: var(--space-2);
        word-break: break-all;
        color: var(--accent-secondary);
    }

    .ent-note {
        font-size: 0.75rem;
        color: var(--text-muted);
    }

    @media (max-width: 600px) {
        h1 {
            font-size: 1.75rem;
        }
        .intro {
            font-size: 1rem;
        }
    }
</style>
