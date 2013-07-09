from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # url(r'^$', 'RBPICameraRest.views.home', name='home'),
    # url(r'^RBPICameraRest/', include('RBPICameraRest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    (r'^version/$', 'RBPICameraRest.api.views.version'),
    (r'^photo/params/$', 'RBPICameraRest.api.views.get_photo_params'),
    (r'^photo/shot/$', 'RBPICameraRest.api.views.photo_shot'),

    (r'^video/params/$', 'RBPICameraRest.api.views.get_video_params'),
    (r'^video/streaming/$', 'RBPICameraRest.api.views.video_streaming'),
)

