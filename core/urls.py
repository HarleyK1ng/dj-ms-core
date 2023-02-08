"""dj_ms_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import logging

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from core.settings import APP_LABEL

URL_PREFIX = APP_LABEL + '/' if APP_LABEL else ''


urlpatterns = [
    path(URL_PREFIX + 'admin/', admin.site.urls),
    path(URL_PREFIX + 'api/auth/', include('authentication.api.urls'), name='authentication'),

    path('api/' + URL_PREFIX, include('app.api.urls'), name='api'),
    path(URL_PREFIX, include('app.urls')),
]


def get_redirect_url():
    try:
        return redirect(f'{URL_PREFIX}')
    except Exception as e:
        logging.error(e)
        return redirect(f'{URL_PREFIX}/admin')


urlpatterns += [
    path('', lambda req: get_redirect_url()),
]
