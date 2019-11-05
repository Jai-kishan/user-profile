from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from mysite.core import views as core_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)