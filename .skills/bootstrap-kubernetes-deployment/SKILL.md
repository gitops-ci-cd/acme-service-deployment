---
name: bootstrap-kubernetes-deployment
description: Automatically creates and populates a new Kubernetes deployment repository for a service using GitHub templates and convention-based configuration. Use when the user wants to create a new service or bootstrap a deployment.
argument-hint: "[repository-name]"
---

# Bootstrap Kubernetes Deployment Repository

## Description

Automatically creates and populates a new Kubernetes deployment repository for a service using GitHub's template repository feature and a cookiecutter GitHub Actions workflow. All configuration is convention-based, deriving values from the service name and GitHub organization.

## Instructions

### Step 1: Extract Information from Request

**Extracted from user request:**
- Repository name (must end with `-deployment`, e.g., "user-api-deployment", "payment-service-deployment")

**Derived by skill:**
- `organization`: Inferred from current GitHub organization context
- `service_name`: Derived by removing `-deployment` suffix from repository name

**Derived by workflow:**
- `image_name`: "{service_name}"
- `image_registry`: "ghcr.io/{organization}"

### Step 2: Confirm with User

Before taking any action, present the derived values and ask the user to confirm:

```
I'm about to create the following repository:

- **Repository:** {organization}/{repository_name}
- **Template:** {organization}/acme-service-deployment
- **Service name:** {service_name}
- **Image registry:** ghcr.io/{organization}/{service_name}

Shall I proceed?
```

Do not continue until the user explicitly confirms.

### Step 3: Create Repository from Template

<!--
TODO: We can't currently create a repository from a template using the MCP server, so this is a placeholder for the actual API call that would be made. The implementation may require using the GitHub REST API directly or a custom MCP action.
-->

Use the GitHub MCP server to create a repository from the template:

```
mcp_github_create_repository(
    name="{repository_name}",
    organization="{organization}",
    description="Kubernetes manifests for deploying {service_name}",
    template_owner="{organization}",
    template_repo="acme-service-deployment"
)
```

### Step 4: Trigger Cookiecutter Workflow

Run the cookiecutter workflow to populate the repository:

```
mcp_github_run_workflow(
    owner="{organization}",
    repo="{repository_name}",
    workflow_id="Cookiecutter",
    ref="main"
)
```

### Step 5: Provide Summary

```markdown
Created repository at https://github.com/{organization}/{repository_name}!

The repository has been populated with Kubernetes deployment manifests for the {service_name} service, using the Acme Application CRD. The structure includes:

- Kustomize manifests
- Kubernetes deployment manifests
- Environment overlays (local, sandbox, production)
```
