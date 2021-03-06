"""PytSite Facebook Comments Driver Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import requests as _requests
from typing import Iterable as _Iterable
from pytsite import logger as _logger
from plugins import auth as _auth, comments as _comments
from ._widget import Comments as _CommentsWidget


class Driver(_comments.driver.Abstract):
    """Facebook Comments Driver.
    """

    def get_name(self) -> str:
        """Get driver's name.
        """
        return 'facebook'

    def get_description(self) -> str:
        """Get driver's description.
        """
        return 'Facebook'

    def get_widget(self, widget_uid: str, thread_uid: str) -> _CommentsWidget:
        """Get comments widget.
        """
        return _CommentsWidget(widget_uid, href=thread_uid)

    def get_comments_count(self, thread_uid: str) -> int:
        """Get comments count for particular thread.
        """
        count = 0

        try:
            r = _requests.get('https://graph.facebook.com/v2.4', {
                'fields': 'share{comment_count}',
                'id': thread_uid,
            }).json()

            if 'share' in r:
                count = int(r['share']['comment_count'])

        except Exception as e:
            _logger.error(e)

        return count

    def create_comment(self, thread_uid: str, body: str, author: _auth.model.AbstractUser,
                       status: str = 'published', parent_uid: str = None) -> _comments.model.AbstractComment:
        """Create new comment.
        """
        raise NotImplementedError("Not implemented yet.")

    def get_comments(self, thread_uid: str, limit: int = 0, skip: int = 0) \
            -> _Iterable[_comments.model.AbstractComment]:
        raise NotImplementedError("Not implemented yet.")

    def get_comment(self, uid: str) -> _comments.model.AbstractComment:
        """Get single comment by UID.
        """
        raise NotImplementedError("Not implemented yet.")

    def delete_comment(self, uid: str):
        """Mark comment as deleted.
        """
        raise NotImplementedError("Not implemented yet.")

    def delete_thread(self, thread_uid: str):
        """Physically remove comments for particular thread.
        """
        raise NotImplementedError("Not implemented yet.")

    def get_permissions(self, user: _auth.model.AbstractUser = None) -> dict:
        """Get permissions definition for user.
        """
        return {'create': True}
