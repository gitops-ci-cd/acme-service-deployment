# {{ cookiecutter.project_name | replace('-', ' ') | title }}

Kubernetes manifests for deploying {{ cookiecutter.project_name | app_name_from_project }}. This utilizes the [Acme Application](https://github.com/dudo-home-lab/kro-addon/blob/main/base/resource-graph-definitions/acme-application.yaml) abstraction to define the application and its components, requiring minimal boilerplate while providing consistent day-2 operations support.
