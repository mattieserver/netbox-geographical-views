from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_geographical_views:home',
        link_text='Topology',
        buttons=(
               PluginMenuButton(
                link='plugins:netbox_geographical_views:home',
                title='Geographical View',
                icon_class='mdi mdi-plus-thick',
                permissions=[],
            ),
        )
    ),
)