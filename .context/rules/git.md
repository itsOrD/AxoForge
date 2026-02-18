# Git Rules & Strategy

> **AI Directive**: History is documentation. Keep it clean and readable.

## 1. Branching Strategy: Feature Branches
*   **Main Branch**: `main` (Protected, Deployable)
*   **Feature Branches**: `feat/[name]`, `fix/[name]`, `chore/[name]`

## 2. The Golden Workflow: Linear History
We enforce a **Semi-Linear History** using Rebase + Fast-Forward.

### Step-by-Step
1.  **Start**: `git checkout -b feat/my-cool-feature`
2.  **Work**: Commit often locally.
3.  **Sync**:
    ```bash
    git fetch origin
    git rebase origin/main
    # Resolve conflicts if any
    ```
4.  **Push**: `git push --force-with-lease origin feat/my-cool-feature`
5.  **Merge (Manager/Lead)**:
    ```bash
    git checkout main
    git merge --ff-only feat/my-cool-feature
    ```
    *If this fails, it means the branch is not up to date. Go back to step 3.*

## 3. Commit Messages (Semantic)
Format: `type(scope): description`

*   `feat`: New feature
*   `fix`: Bug fix
*   `docs`: Documentation only
*   `style`: Formatting (no code change)
*   `refactor`: Code change that neither fixes a bug nor adds a feature
*   `test`: Adding missing tests
*   `chore`: Tooling, build process

**Example**: `feat(auth): implement google oauth login`
