"""boar_bar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from share.views import NotExisting, Logout
from user.views import signup, activate, account_activation_sent


urlpatterns = [
    url(
        r'^$',
        RedirectView.as_view(url='/home/', permanent=True),
    ),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^user/', include('user.urls', namespace='user')),
    url(r'^admin/', admin.site.urls),

    # registration views
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^signup/$', signup, name="signup"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$',
        activate, name='activate'),
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'share/login_failure.html',
         'redirect_field_name': 'previous'},
        name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^password_reset/$', auth_views.password_reset,
        {'template_name': 'registration_custom/password_reset_form.html'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,
        {'template_name': 'registration_custom/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name': 'registration_custom/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,
        {'template_name': 'registration_custom/password_reset_complete.html'}, name='password_reset_complete'),

    url(
        r'^dict/',
        include('dictionary.urls', namespace='dictionary')
    ),
    url(
        r'^word/',
        include('word.urls', namespace='word')
    ),
    url(
        r'^learn/',
        include('course.urls', namespace='course')
    ),
    url(
        r'^proposal/',
        include('proposal.urls', namespace='proposal')
    ),
    url(
        r'^collection/',
        include('collection.urls', namespace='collection')
    ),
    url(
        r'^contribute/',
        include('contribute.urls', namespace='contribute')
    ),
    url(
        r'^translate/',
        include('translator.urls', namespace='translator')
    ),
    url(
        r'^api/',
        include('api.urls', namespace='api')
    ),
    url(
        r'^favicon\.ico$',
        RedirectView.as_view(url='/static/favicon.png', permanent=True)
    ),
    url(
        r'^.*$',
        NotExisting.as_view(),
        name='not_existing',
    ),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
