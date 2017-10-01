import app.config

CONFIG = 'app/settings/site.yaml'
SITE_SETTINGS = app.config.set_settings(CONFIG)
print(SITE_SETTINGS['settings']['url'])
