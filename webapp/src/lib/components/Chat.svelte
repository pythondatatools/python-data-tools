<script>
    import { onMount } from "svelte";
    import * as webllm from "@mlc-ai/web-llm";

    export let isOpen = false;

    let messages = [
        {
            role: "system",
            content:
                "You are 'The Guardian', an AI assistant for Python Data Tools. You help users with Pandas, Polars, DuckDB, and BigQuery. Keep answers concise and code-heavy.",
        },
        {
            role: "assistant",
            content:
                "Hello! I'm The Guardian. How can I help you with your data wrangling today?",
        },
    ];
    let input = "";
    let engine = null;
    let isLoading = false;
    let progress = "";
    let isModelLoaded = false;

    const selectedModel = "Llama-3.1-8B-Instruct-q4f16_1-MLC"; // Efficient and high quality

    async function initEngine() {
        if (engine) return;
        isLoading = true;

        try {
            engine = await webllm.CreateMLCEngine(selectedModel, {
                initProgressCallback: (report) => {
                    progress = report.text;
                },
            });
            isModelLoaded = true;
        } catch (err) {
            console.error("Web-LLM Init Error:", err);
            progress = "Error: This feature requires a WebGPU-enabled browser.";
        } finally {
            isLoading = false;
        }
    }

    async function sendMessage() {
        if (!input.trim() || isLoading) return;

        if (!isModelLoaded) {
            await initEngine();
            if (!isModelLoaded) return;
        }

        const userMsg = { role: "user", content: input };
        messages = [...messages, userMsg];
        const currentInput = input;
        input = "";

        isLoading = true;
        try {
            const reply = await engine.chat.completions.create({
                messages: messages.map((m) => ({
                    role: m.role,
                    content: m.content,
                })),
            });
            const assistantMsg = {
                role: "assistant",
                content: reply.choices[0].message.content,
            };
            messages = [...messages, assistantMsg];
        } catch (err) {
            messages = [
                ...messages,
                {
                    role: "assistant",
                    content:
                        "Sorry, I encountered an error. Make sure your browser supports WebGPU.",
                },
            ];
        } finally {
            isLoading = false;
        }
    }

    function handleKeydown(e) {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    }
</script>

{#if isOpen}
    <div
        class="chat-overlay"
        role="presentation"
        on:click={() => (isOpen = false)}
        on:keydown={(e) => e.key === "Escape" && (isOpen = false)}
    ></div>
    <div class="chat-window">
        <div class="chat-header">
            <div class="header-info">
                <span class="bot-icon">🛡️</span>
                <div>
                    <h3>The Guardian</h3>
                    <p class="status">
                        {isModelLoaded ? "Online" : "Ready to Load"}
                    </p>
                </div>
            </div>
            <button class="close-btn" on:click={() => (isOpen = false)}
                >&times;</button
            >
        </div>

        <div class="chat-messages">
            {#each messages.filter((m) => m.role !== "system") as msg}
                <div class="message {msg.role}">
                    <div class="message-content">
                        {msg.content}
                    </div>
                </div>
            {/each}

            {#if isLoading}
                <div class="message assistant loading">
                    <div class="message-content">
                        {#if !isModelLoaded}
                            <div class="progress-bar">
                                <p>Downloading Model (~4GB)...</p>
                                <p class="progress-detail">{progress}</p>
                            </div>
                        {:else}
                            <span class="typing-dot"></span>
                            <span class="typing-dot"></span>
                            <span class="typing-dot"></span>
                        {/if}
                    </div>
                </div>
            {/if}
        </div>

        <div class="chat-input">
            <textarea
                placeholder="Ask about Pandas, Polars..."
                bind:value={input}
                on:keydown={handleKeydown}
            ></textarea>
            <button
                on:click={sendMessage}
                disabled={isLoading || !input.trim()}
            >
                {isModelLoaded ? "Send" : "Initialize"}
            </button>
        </div>
    </div>
{/if}

<style>
    .chat-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(4px);
        z-index: 1000;
    }

    .chat-window {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 400px;
        height: 600px;
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: 16px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        display: flex;
        flex-direction: column;
        z-index: 1001;
        overflow: hidden;
        animation: slideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes slideIn {
        from {
            transform: translateY(20px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }

    .chat-header {
        padding: 1rem 1.5rem;
        background: var(--bg-secondary);
        border-bottom: 1px solid var(--border-color);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .header-info {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .bot-icon {
        font-size: 1.5rem;
    }

    .header-info h3 {
        font-size: 1rem;
        margin: 0;
        font-weight: 600;
    }

    .status {
        font-size: 0.75rem;
        color: var(--accent-green);
        margin: 0;
    }

    .close-btn {
        background: transparent;
        border: none;
        color: var(--text-muted);
        font-size: 1.5rem;
        cursor: pointer;
    }

    .chat-messages {
        flex: 1;
        padding: 1.5rem;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        gap: 1rem;
        background: #0f172a;
    }

    .message {
        display: flex;
        flex-direction: column;
    }

    .message.user {
        align-items: flex-end;
    }

    .message-content {
        padding: 0.75rem 1rem;
        border-radius: 12px;
        font-size: 0.9rem;
        line-height: 1.5;
        max-width: 85%;
        white-space: pre-wrap;
    }

    .user .message-content {
        background: var(--accent-blue);
        color: white;
        border-bottom-right-radius: 2px;
    }

    .assistant .message-content {
        background: var(--bg-tertiary);
        color: var(--text-primary);
        border-bottom-left-radius: 2px;
    }

    .chat-input {
        padding: 1rem;
        background: var(--bg-secondary);
        border-top: 1px solid var(--border-color);
        display: flex;
        gap: 0.75rem;
        align-items: flex-end;
    }

    textarea {
        flex: 1;
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 0.75rem;
        color: var(--text-primary);
        font-family: inherit;
        font-size: 0.9rem;
        resize: none;
        height: 60px;
        outline: none;
    }

    textarea:focus {
        border-color: var(--accent-blue);
    }

    button {
        background: var(--accent-blue);
        color: white;
        border: none;
        padding: 0.75rem 1.25rem;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        transition: opacity 0.2s;
        height: 40px;
    }

    button:disabled {
        opacity: 0.5;
        cursor: not-allowed;
    }

    .progress-bar {
        font-size: 0.8rem;
    }

    .progress-detail {
        color: var(--text-muted);
        margin-top: 0.25rem;
    }

    .typing-dot {
        display: inline-block;
        width: 6px;
        height: 6px;
        background: var(--text-muted);
        border-radius: 50%;
        margin-right: 3px;
        animation: typing 1.4s infinite;
    }

    .typing-dot:nth-child(2) {
        animation-delay: 0.2s;
    }
    .typing-dot:nth-child(3) {
        animation-delay: 0.4s;
    }

    @keyframes typing {
        0%,
        60%,
        100% {
            transform: translateY(0);
        }
        30% {
            transform: translateY(-4px);
        }
    }

    @media (max-width: 600px) {
        .chat-window {
            bottom: 0;
            right: 0;
            width: 100%;
            height: 100%;
            border-radius: 0;
        }
    }
</style>
