# AI-First Contribution Guidelines

> **Directive**: This repository is designed to be maintained by **AI Agents** (like me) with **Human Supervision**.

## 1. The Golden Rule of Context
**Do not change code without updating the Context.**
If you change *what* the code does, you must update:
*   `SCAFFOLD_INTENT.md` (if the goal changed).
*   `.context/rules/*.md` (if the pattern changed).

## 2. Workflow for Humans
When you want to make a change:
1.  **Don't write code first.**
2.  **Write Intent.** Update `task.md` or `SCAFFOLD_INTENT.md` with what you want.
3.  **Prompt the Agent.** "I've updated the intent. Please implement X."

## 3. Workflow for Agents
1.  **Read Context First.** Always checks `SCAFFOLD_INTENT.md` before `SCAFFOLD_INTENT.md`.
2.  **Plan.** Create `.context/plans/implementation_plan.md` before big changes.
3.  **Hydrate.** If you see `{{PLACEHOLDER}}`, ask the user to run `setup.py`.

## 4. MCP & Tools
*   We use **MCP** to give agents tools.
*   If you add a tool, update `docs/MCP.md` and `mcp.json.template`.
