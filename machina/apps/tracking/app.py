# -*- coding: utf-8 -*-

# Standard library imports
# Third party imports
from django.conf.urls import patterns
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

# Local application / specific library imports
from machina.core.app import Application
from machina.core.loading import get_class


class TrackingApp(Application):
    name = 'tracking'

    mark_forums_read_view = get_class('tracking.views', 'MarkForumsReadView')
    mark_topics_read_view = get_class('tracking.views', 'MarkTopicsReadView')
    unread_topics_view = get_class('tracking.views', 'UnreadTopicsView')

    def get_urls(self):
        urls = [
            url(_(r'^mark/forums/$'), self.mark_forums_read_view.as_view(), name='mark-all-forums-read'),
            url(_(r'^mark/forums/(?P<pk>\d+)/$'), self.mark_forums_read_view.as_view(), name='mark-subforums-read'),
            url(_(r'^mark/forum/(?P<pk>\d+)/topics/$'), self.mark_topics_read_view.as_view(), name='mark-topics-read'),
            url(_(r'^unread-topics/$'), self.unread_topics_view.as_view(), name='unread-topics'),
        ]
        return patterns('', *urls)


application = TrackingApp()
