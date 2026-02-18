# Dockerfile Template
# > AI Directive: Hydrate based on SCAFFOLD_INTENT.md and {{LANGUAGE}} specifics.

# Stage 1: Builder
FROM {{BUILDER_IMAGE}} AS builder
WORKDIR /app
COPY . .
RUN {{BUILD_COMMAND}}

# Stage 2: Runner
FROM {{RUNNER_IMAGE}} AS runner
WORKDIR /app
COPY --from=builder /app/{{BUILD_OUTPUT}} ./
CMD ["{{START_COMMAND}}"]
