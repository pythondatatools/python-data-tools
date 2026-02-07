<script>
    import { createEventDispatcher } from "svelte";
    import { base } from "$app/paths";
    import Search from "./Search.svelte";

    const dispatch = createEventDispatcher();

    function toggleSidebar() {
        dispatch("toggleSidebar");
    }

    function toggleChat() {
        dispatch("toggleChat");
    }
</script>

<nav class="navbar">
    <div class="navbar-left">
        <button
            class="hamburger"
            on:click={toggleSidebar}
            aria-label="Toggle Navigation"
        >
            <svg viewBox="0 0 24 24" width="24" height="24">
                <path
                    fill="currentColor"
                    d="M3,6H21V8H3V6M3,11H21V13H3V11M3,16H21V18H3V16Z"
                />
            </svg>
        </button>
        <div class="logo-mobile">
            <a href="{base}/">
                <span>🐍 Python Data Tools</span>
            </a>
        </div>
    </div>

    <div class="navbar-center">
        <Search />
    </div>

    <div class="navbar-right">
        <button
            class="chat-toggle"
            on:click={toggleChat}
            aria-label="Toggle AI Chat"
        >
            <span class="chat-icon">🛡️</span>
            <span class="chat-label">Ask Guardian</span>
        </button>
    </div>
</nav>

<style>
    .navbar {
        height: 64px;
        background: var(--bg-secondary);
        border-bottom: 1px solid var(--border-color);
        padding: 0 1.5rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        position: fixed;
        top: 0;
        left: 260px; /* Offset by sidebar width on desktop */
        right: 0;
        z-index: 100;
        backdrop-filter: blur(8px);
        background: rgba(15, 23, 42, 0.8); /* Sleek dark glass effect */
    }

    .navbar-left {
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .navbar-center {
        flex: 1;
        max-width: 600px;
        margin: 0 2rem;
    }

    .logo-mobile {
        display: none;
    }

    .navbar-right {
        display: flex;
        align-items: center;
    }

    .chat-toggle {
        background: var(--bg-tertiary);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 0.5rem 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: var(--text-primary);
        cursor: pointer;
        transition: all 0.2s;
        margin-left: auto;
    }

    .chat-toggle:hover {
        background: var(--accent-blue);
        color: white;
        border-color: var(--accent-blue);
    }

    .chat-icon {
        font-size: 1.1rem;
    }

    .chat-label {
        font-size: 0.85rem;
        font-weight: 500;
    }

    .logo-mobile span {
        font-weight: 700;
        font-size: 1rem;
        background: linear-gradient(
            135deg,
            var(--accent-blue),
            var(--accent-purple)
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        white-space: nowrap;
    }

    .hamburger {
        display: none; /* Hidden on desktop */
        background: transparent;
        border: none;
        color: var(--text-primary);
        align-items: center;
        justify-content: center;
        padding: 0.5rem;
        border-radius: 6px;
        transition: background 0.2s;
        cursor: pointer;
    }

    .hamburger:hover {
        background: var(--bg-tertiary);
    }

    @media (max-width: 900px) {
        .navbar {
            left: 0;
            padding: 0 1rem;
            height: 60px;
        }

        .navbar-center {
            display: none; /* Hide full search on mobile nav, maybe add a toggle later */
        }

        .navbar-right {
            display: none;
        }

        .hamburger {
            display: flex;
        }

        .logo-mobile {
            display: block;
        }
    }
</style>
