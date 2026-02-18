# Model Context Protocol (MCP) Configuration

> **AI Directive**: Required external tools for the AI Agent.

## 1. Required Servers

### Core
*   **filesystem**: Read/Write access to the repository.
*   **sequential-thinking**: Planning and reasoning.

### Database (Hydrated)
*   **`{{DATABASE_MCP_SERVER}}`**: Interface for `{{DATABASE}}`.
    *   *Config*: Connection string via `{{ENV_VAR_NAME}}`.

### Browser (Optional)
*   **browser-base**: For E2E testing or web scraping if required.

## 2. Tool Usage Rules
*   **Read-Only First**: Inspect before modification.
*   **User Confirmation**: Require approval for destructive actions (DROP, DELETE).
