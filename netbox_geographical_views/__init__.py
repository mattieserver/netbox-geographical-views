from extras.plugins import PluginConfig

class GeographicalViewsConfig(PluginConfig):
    name = 'netbox_geographical_views'
    verbose_name = 'Geographical views'
    description = 'A netbox plugin that plots your devices on a world map'
    version = '0.0.1-alpha.1'
    author = 'Mattijs Vanhaverbeke'
    author_email = 'author@example.com'
    base_url = 'netbox_geographical_views'
    required_settings = []
    default_settings = {
    }

config = GeographicalViewsConfig