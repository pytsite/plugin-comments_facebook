"""PytSite Facebook Comments Driver Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load_uwsgi():
    from pytsite import tpl
    from plugins import facebook, comments
    from . import _comments_driver

    tpl.register_package(__name__)

    try:
        facebook.get_app_id()
        comments.register_driver(_comments_driver.Driver())

    except facebook.error.AppIdNotSet:
        pass
