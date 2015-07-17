from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from main.views import GetPost, MakerListView, CerealDetailView, CerealSearchView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_cereal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^first_view/(?P<starts_with>\w+)/$', 'main.views.first_view'),
    url(r'^first_view/$', 'main.views.first_view'),
    url(r'^get_post/$', 'main.views.get_post'),
    url(r'^template_view/$', 'main.views.template_view'),
    url(r'^detailed_view/$', 'main.views.detailed_view'),
    url(r'^cereal_search/$', 'main.views.cereal_search'),
    url(r'^cereal_create/$', 'main.views.cereal_create'),
    url(r'^GetPost/$', csrf_exempt(GetPost.as_view())),
    url(r'^maker_list/$', MakerListView.as_view()),
    url(r'^cereals/(?P<pk>[0-9]+)/$', CerealDetailView.as_view()),
    url(r'^CerealSearchView/$', CerealSearchView.as_view()),
)
