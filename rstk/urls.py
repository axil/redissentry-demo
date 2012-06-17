from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth import views as auth_views

from django.contrib import admin
admin.autodiscover()

from core.views import main_page

urlpatterns = patterns('',
    url(r'^$', main_page),
    url(r'^logged_in/$', auth_views.logout, {'template_name': 'core/logged_in.html'}, 'logged_in'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'core/logout.html'}, 'logout'),
    url(r'^admin/', include(admin.site.urls)),
)

