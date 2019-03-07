from tethys_sdk.base import TethysAppBase, url_map_maker


class MotusLayout(TethysAppBase):
    """
    Tethys app class for Motus Layout.
    """

    name = 'Motus Layout'
    index = 'motus_layout:home'
    icon = 'motus_layout/images/icon.gif'
    package = 'motus_layout'
    root_url = 'motus-layout'
    color = '#c0392b'
    description = 'N'
    tags = '&quot;test,app, myfirstapp,&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='motus-layout',
                controller='motus_layout.controllers.home'
            ),
            UrlMap(
                name='Motus_Map',
                url='motus-layout/Motus_Map',
                controller='motus_layout.controllers.Motus_Map'
            ),
        )

        return url_maps
