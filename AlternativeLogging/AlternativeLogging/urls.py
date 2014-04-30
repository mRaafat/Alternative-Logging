from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #
    # url(r'^blog/', include('blog.urls')),
 	url(r'^$', 'AlternateLogging.views.loginPage', name='loginPage'),
    url(r'^admin/', include(admin.site.urls)),
)
