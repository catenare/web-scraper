from pathlib import Path
from ruamel.yaml import YAML

SITE_SETTINGS = 'settings'
SITE_URL = 'url'

def set_settings(config):
    yaml = YAML(typ='safe')
    config_file = Path(config)
    return yaml.load(config_file)

def get_site_url(site_data):
    return site_data[SITE_SETTINGS][SITE_URL]

if __name__ == "__main__":
    site_config = 'app/settings/site.yaml'
    site_data = set_settings(site_config)
    print(get_site_url(site_data))
