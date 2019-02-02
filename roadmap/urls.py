from django.conf.urls import include, patterns, url


urlpatterns = patterns(
    'roadmap.views',
    url(r'^$', 'dashboard', name='dashboard')
)

urlpatterns += [
    url(r'^api/', include('roadmap.api.urls', namespace='api'))
]
