# 🦎 AxoForge
**The AI-Native Project Foundation**

![AxoForge Logo](docs/assets/logo.png)

![Status](https://img.shields.io/badge/Status-Beta-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Agent-Ready](https://img.shields.io/badge/Agent-Ready-purple?style=for-the-badge)

> **Philosophy**: A universal, language-agnostic scaffold designed for **Human-AI Collaboration**.
> AxoForge doesn't make decisions for you—it helps you and your AI agent make them *together*.

---

## 📚 Table of Contents
- [Motivation](#-motivation-why-axoforge)
- [Features](#-key-features)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [The Workflow](#-the-workflow)
- [For Agents](#-for-ai-agents)
- [Contributing](#-contributing)

---

## 🧠 Motivation: Why AxoForge?

There are hundreds of "AI Starter Kits" on GitHub. AxoForge sits in the "Goldilocks Zone" between "Vibe Coding" (chaos) and "Opinionated Stacks" (rigidity).

| Feature | 🕸️ "Vibe Coding" | 📦 "Starter Kits" (e.g. T3) | 🦎 AxoForge |
| :--- | :--- | :--- | :--- |
| **Structure** | None (Spaghetti) | Rigid (Next.js/Supabase/etc.) | **Flexible (Context-Driven)** |
| **Agent Support** | "Hope it reads my mind" | "Read these 50 files" | **Native MCP & Context Packing** |
| **Scalability** | Low (Breaks at 5 files) | High (If you stick to the stack) | **High (Architected by You)** |
| **Tech Stack** | Whatever the AI picks | Hardcoded | **Language Agnostic** |

---

## ✨ Key Features

*   **🤖 Agent-First Design**: The documentation is written for the AI to read, ensuring it understands your architectural values (YAGNI, DRY, SOLID) before writing code.
*   **🛠️ MCP Ready**: Pre-configured with Model Context Protocol (MCP) support, giving your agent filesystem access and reasoning tools from day one.
*   **🧠 Context Packing**: Built-in utilities to condense your entire project context into a single prompt for LLMs.
*   **🔄 Self-Hydrating**: Interactive setup scripts that customize the template to your specific goal and stack.

---

## ⚡ Quick Start

### 1. Initialize
Clone this repository to start your new project.

```bash
git clone https://github.com/your-username/AxoForge my-new-project
cd my-new-project
```

**Note on Git History:**
The setup script will handle git reset for you!
If you chose not to remove the .git history, than do make sure you manually run this:

```bash
rm -rf .git
git init
git add .
git commit -m "Init commit"
```

### 2. Configure (The Magic)
Run the interactive setup script to "hydrate" the template.

```bash
python3 .context/scripts/setup.py
```

*   **What it does**:
    *   **Resets History**: Starts a fresh git repository.
    *   **Captures Intent**: Prompts for your Goal ("Build a crypto trading bot") and Stack ("Python, FastAPI").
    *   **Configures Tools**: Generates a custom `mcp.json` for your agent.
    *   **Updates Docs**: Replaces this generic README with one specific to your project.

### 3. Connect & Build
1.  **Reload Editor**: Restart Cursor/Windsurf to load the new `mcp.json`.
2.  **Verify Intent**: Open **`SCAFFOLD_INTENT.md`** and verify your choices.
3.  **Prompt Agent**:
    > "Read SCAFFOLD_INTENT.md and hydrate the project structure (Dockerfile, pipelines, boilerplate) to match those decisions."

---

## 📂 Project Structure

AxoForge separates **Intent** (what/why) from **Implementation** (how).

```plaintext
.
├── .context/               # The "Brain" - System Prompts & Logic
│   ├── rules/              # Coding standards (coding.md, testing.md)
│   ├── scripts/            # Automation (setup.py, pack_context.py)
│   └── templates/          # Source templates for hydration
├── docs/                   # The "Manual" - Implementation Details
│   ├── ARCHITECTURE.md     # Decisions & Diagrams
│   ├── MCP.md              # Tool Configuration
│   └── WORKFLOWS.md        # How to build/deploy
├── SCAFFOLD_INTENT.md      # The "DNA" - Single Source of Truth
├── compose.yml             # Infrastructure Definition
└── Dockerfile              # Deployment Logic
```

---

## 🔄 The Workflow

AxoForge enforces an **"Intent-First"** workflow to prevent scope creep.

1.  **Define Intent**: Edit `SCAFFOLD_INTENT.md`. This is the *only* place where high-level decisions live.
2.  **Feed Context**: The `.context/` folder acts as a "System Prompt" for your project.
3.  **Collaborate**: Ask the AI to implement features *based on* the Intent and Context.

---

## 🤖 For AI Agents

If you are an AI reading this, please adhere to the following:

1.  **Read Context First**: Always check `.context/rules/` before writing code.
2.  **Respect Intent**: `SCAFFOLD_INTENT.md` is the source of truth. Do not deviate from the stack defined there without user approval.
3.  **Use Tools**: Use the available MCP tools (`filesystem`, `sequential-thinking`) to plan your actions.

To manually pack context for an LLM:
```bash
python3 .context/scripts/pack_context.py | pbcopy
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING_AI.md](.context/CONTRIBUTING_AI.md) for guidelines on how to modify the core AxoForge template.

---

**Built with ❤️ for the AI-Native Future.**
