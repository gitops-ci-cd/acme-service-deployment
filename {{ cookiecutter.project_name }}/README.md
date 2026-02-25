# {{ cookiecutter.project_name | replace('-', ' ') | title }}

Kubernetes manifests for deploying {{ cookiecutter.project_name | app_name_from_project }}. This utilizes the [Acme Application](https://github.com/dudo-home-lab/kro-addon/blob/main/base/resource-graph-definitions/acme-application.yaml) custom resource definition from the kro Addon to deploy the application.

## Structure

```text
{{ cookiecutter.project_name }}/
├── base/
│   ├── acme-application.yaml      # Core application definition
│   ├── kustomization.yaml         # Base kustomization config
│   └── image_transformer_config.yaml
└── overlays/
    ├── local/                     # Local development environment
    ├── sandbox/                   # Sandbox/staging environment
    └── production/                # Production environment
```

## Usage

Apply the manifests using kustomize:

```bash
# Local environment
kubectl apply -k overlays/local

# Sandbox environment
kubectl apply -k overlays/sandbox

# Production environment
kubectl apply -k overlays/production
```

## Configuration

**Image**: `{{ cookiecutter.image_registry }}/{{ cookiecutter.image_name }}`

Configure environment-specific settings in the overlays.
