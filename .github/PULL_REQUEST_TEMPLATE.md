# Pull Request Template

## Fast PR Mode (Tiny Changes)

Use this section **instead of** the full template for tiny, low-risk updates (for example docs, comments, typo fixes, or metadata changes).

**Fast mode is not allowed if the PR changes code, configuration, dependencies, or workflow/runtime logic.**

### Quick Summary

- What changed:
- Why:

### Quick Checklist

- [ ] Tiny and low-risk change
- [ ] No code-path or runtime behavior changes
- [ ] No security impact
- [ ] No migration/deployment steps required
- [ ] CI passed or not required for this change type

---

## Full PR Mode

Use the full template below for all non-trivial changes.

## Summary

Describe what changed and why. Focus on user or system impact.

## Linked Work Item(s)

- Work item / ticket: `WORK-1234`
- Additional references (optional):

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Refactor / cleanup
- [ ] Documentation update
- [ ] Test-only change
- [ ] Security improvement
- [ ] CI/CD or tooling change

## Scope of Changes

List key areas touched (modules, workflows, docs, configs):

-

## Validation and Testing

Describe what you validated and how.

### Automated

- [ ] Unit tests
- [ ] Integration tests
- [ ] Lint / static analysis
- [ ] CI pipeline checks

### Manual

- [ ] Manual testing completed
- [ ] Not applicable

Manual test notes (if applicable):

-

## Security and Compliance

- [ ] No security impact
- [ ] Security impact assessed and documented
- [ ] No new secrets, tokens, or credentials introduced
- [ ] Dependency or supply-chain impact reviewed
- [ ] License/compliance impact reviewed (if dependencies changed)

## Breaking Changes

- [ ] No breaking changes
- [ ] Breaking changes present (describe below)

If breaking changes exist, include migration steps:

-

## Deployment and Rollback

- [ ] No special deployment steps
- [ ] Special deployment steps required (describe below)

Deployment notes:

-

Rollback plan:

-

## Reviewer Notes

Anything specific reviewers should focus on:

-

## Final Checklist

- [ ] Code follows repository conventions
- [ ] Tests are added/updated where needed
- [ ] Documentation is updated where needed
- [ ] Changelog is updated (if applicable)
- [ ] CI is passing or failures are explained
