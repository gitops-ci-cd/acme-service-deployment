from jinja2.ext import Extension

def lowercase(value):
    """Convert a string to lowercase."""
    return str(value).lower()

def uppercase(value):
    """Convert a string to uppercase."""
    return str(value).upper()

def dash_to_underscore(value):
    """Convert dashes to underscores."""
    return str(value).replace('-', '_')

def app_name_from_project(value):
    """Derive app name from project name by removing '-deployment' suffix."""
    project = str(value)
    if project.endswith('-deployment'):
        return project[:-11]  # Remove '-deployment'
    return project

class CustomExtension(Extension):
    """A custom Jinja2 extension to add filters."""
    def __init__(self, environment):
        super().__init__(environment)
        # Register custom filters
        environment.filters['lowercase'] = lowercase
        environment.filters['uppercase'] = uppercase
        environment.filters['dash_to_underscore'] = dash_to_underscore
        environment.filters['app_name_from_project'] = app_name_from_project
