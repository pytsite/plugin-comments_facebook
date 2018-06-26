"""PytSite Comments Driver Widgets.
"""
from pytsite import router as _router, lang as _lang, tpl as _tpl, html as _html
from plugins import assetman as _assetman, widget as _widget, facebook as _facebook

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Comments(_widget.Abstract):
    """Comments Widget.
    """

    def __init__(self, uid: str, **kwargs):
        """Init.
        """
        super().__init__(uid, **kwargs)

        self._app_id = _facebook.get_app_id()
        self._href = kwargs.get('href', _router.current_url())

        js_sdk_args = {
            'app_id': self._app_id,
            'language': _lang.ietf_tag(sep='_')
        }
        _assetman.add_inline_js(_tpl.render('facebook@fb-js-sdk', js_sdk_args))

    def _get_element(self, **kwargs) -> _html.Element:
        """Get an HTML element representation of the widget.
        :param **kwargs:
        """
        return _html.Div(
            uid=self.uid,
            css='fb-comments',
            data_href=self._href,
            data_width='100%'
        )
