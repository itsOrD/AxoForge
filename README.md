# AI-Native Project Scaffold (Meta-Template)

> **Purpose**: A universal, language-agnostic foundation for AI-assisted software engineering.
> **Goal**: Clone this repo, define your intent, and let the AI hydrate the rest.

## 🚀 Usage Guide

### 1. clone & Initialize
```bash
git clone [this-repo] my-new-project
cd my-new-project
rm -rf .git
git init
```

### 2. Define Your Intent
Open **[SCAFFOLD_INTENT.md](./SCAFFOLD_INTENT.md)** and fill in the details.
*   **Goal**: What are you building?
*   **stack**: Python? Go? Node?
*   **Architecture**: Monolith? Microservices?

### 3. Hydrate (The Magic Step)
Ask your AI Agent (AntiGravity, Cursor, etc.):
> "Read SCAFFOLD_INTENT.md and hydrate the entire project structure (Dockerfile, tech_stack.md, pipelines) to match those decisions."

### 4. Start Building
Once hydrated, the project is ready.
*   `{{PACKAGE_MANAGER}} install`
*   `{{PACKAGE_MANAGER}} run dev`

## 📂 Structure
*   **[.context/](.context/)**: The "Brain". Rules and constraints for the AI.
*   **[docs/](docs/)**: The "Manual". Personas, Workflows, and Architecture.
*   **[SCAFFOLD_INTENT.md](SCAFFOLD_INTENT.md)**: The Source of Truth.
