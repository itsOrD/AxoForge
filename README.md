# 🦎 AxoForge
**The AI-Native Project Foundation**

> **Philosophy**: A universal, language-agnostic scaffold designed for **Human-AI Collaboration**.
> Unlike "vibe coding" templates or opinionated starter kits, AxoForge doesn't make decisions for you—it helps you and your AI agent make them *together*.

## ⚡ Quick Start

### 1. Initialize
Clone this repository to start your new project.
```bash
git clone https://github.com/your-username/AxoForge my-new-project
cd my-new-project
rm -rf .git  # Start fresh
git init
```

### 2. Configure
Run the interactive setup script to "hydrate" the template with your project's identity.
```bash
python3 .context/scripts/setup.py
```
*This will prompt you for your goal, tech stack, and preferences, updating all context files and generating your AI toolkit configuration.*

### 3. Connect
The setup script generates a `mcp.json` file. Configure your AI editor (Cursor, Windsurf) or Agent to use this MCP server configuration to give it access to the tools it needs.

---

## 📖 How to Use

AxoForge is built on the **"Intent-First"** workflow.

### Step 1: Define Intent (`SCAFFOLD_INTENT.md`)
This file is the DNA of your project. If you didn't use the setup script, edit this manually. content here drives everything else.
*   **Goal**: What are you building?
*   **Constraints**: What *can't* you change?
*   **Stack**: What tools are you using?

### Step 2: Feed the Brain (`.context/`)
The `.context/` directory contains the "System Prompt" for your project.
*   **Rules**: Coding standards, testing guidelines.
*   **Scripts**: Use `.context/scripts/pack_context.py` to grab the entire project context when you need to paste it into a chat window.

### Step 3: Build Together
Now, ask your AI Agent:
> "Read SCAFFOLD_INTENT.md and hydrate the project structure (Dockerfile, pipelines, boilerplate) to match those decisions."

Because the *Intent* is clear and the *Context* is structured, the AI will build exactly what you want, not what a generic template dictates.

---

## 🧠 Motivation: Why AxoForge?

There are hundreds of "AI Starter Kits" on GitHub. Most fall into two traps:

1.  **The "Vibe Coding" Trap**: Zero structure. Just "start chatting and hope it works." This creates unmaintainable spaghetti code that falls apart as complexity grows.
2.  **The "Opinionated Stack" Trap**: "Here is a Next.js + Tailwind + Supabase + LangChain template." Great if that's exactly what you want. Useless if you want Go, Rust, or a simple Python script.

**AxoForge is different.**

*   **Agile & Agnostic**: It provides the *structure* for AI collaboration without dictating the *technology*.
*   **Meta-Context**: It treats **Context as Code**. The documentation is written *for the AI* to read, ensuring it understands your architectural values (YAGNI, DRY, SOLID) before it writes a single line of code.
*   **Agent-Ready**: Pre-configured with Model Context Protocol (MCP) support, ensuring your agent has the right tools (filesystem access, sequence thinking) from day one.
