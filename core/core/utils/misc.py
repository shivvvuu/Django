import yaml


def yaml_coerce(value):
    # Convert value to proper Python
    if isinstance(value, str):
        # yaml.load returns a Python Object(we are just creating some quick yaml data with a dummy)
        # Convert string dict "{'apple':1,'bacon':2}" to Python dict
        # Useful because sometimes we need to stringify settings this way(like in Dockerfiles)
        return yaml.load(f'dummy:{value}', Loader=yaml.SafeLoader)['dummy']
    return value
