# Architecture & Design Patterns

> **AI Directive**:
> 1.  Hydrate this document based on `SCAFFOLD_INTENT.md`.
> 2.  Use this as the mutable log of architectural decisions.

## 1. System Overview
**[Project Name]** follows a **{{ARCHITECTURE_STYLE}}** architecture.

*   **Frontend**: `{{FRONTEND_FRAMEWORK}}`
*   **Backend**: `{{BACKEND_FRAMEWORK}}`
*   **Database**: `{{DATABASE}}`
*   **Communication**: `{{COMMUNICATION_PROTOCOL}}`

## 2. Architecture Decision Records (ADR) Log

### ADR-001: Initial Stack Selection (Template)
*   **Status**: Accepted
*   **Date**: {{DATE}}
*   **Context**: Need to select a stack for [Goal].
*   **Decision**: `{{LANGUAGE}}` + `{{FRAMEWORK}}`.
*   **Reasoning**: Alignment with team skills and performance requirements.
*   **Consequences**: [Trade-offs accepted].

## 3. Design Patterns (Menu)
*Select patterns relevant to the chosen architecture:*

*   **Repository Pattern**: Abstract data access to allow swapping backends/mocking.
*   **Factory Pattern**: Centralize object creation logic.
*   **Adapter Pattern**: Wrap 3rd party libraries to prevent vendor lock-in.
*   **Observer/PubSub**: Decouple components via event-driven communication.
*   **Strategy Pattern**: Swap algorithms at runtime (e.g., varied Payment Providers).
