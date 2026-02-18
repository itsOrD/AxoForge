# Commit Strategy & Git Workflow

> **AI Directive**: Enforce a Linear History. No Merge Bubbles unless explicitly requested.

## 1. The Strategy: Semi-Linear History
We use **Feature Branches** combined with **Rebase** to keep the main history clean.

## 2. The Workflow (Command Reference)

### Start Feature
```bash
git checkout main
git pull origin main
git checkout -b feature/[name]
```

### Sync with Main (Daily/Pre-Push)
```bash
git fetch origin
git rebase origin/main
# If conflicts: Fix files -> git add . -> git rebase --continue
```

### Push Feature
```bash
git push --force-with-lease origin feature/[name]
```

### Merge (Maintainer Only)
```bash
git checkout main
git pull origin main
git merge --ff-only feature/[name]
git push origin main
```

## 3. Automation
*   **Pre-commit Hooks**:
    *   Linting (Biome/ESLint).
    *   Type Checking (tsc).
    *   Commit Message Linting (Conventional Commits).

## 4. Semantic Commits
Refer to `.context/rules/git.md` for specific types.
