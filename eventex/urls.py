from django.conf.urls import url, include
from django.contrib import admin

from eventex.core.views import speakers_detail, talk_list, home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
    url(r'^palestras/$', talk_list, name='talk_list'),
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', speakers_detail, name='speakers_detail'),
    url(r'^admin/', admin.site.urls),
]
