"""timesup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from app.views import PrivacyView, FAQSView, HOWITWORKSView, LandingPageView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', LandingPageView.as_view(), name='landingpage_view'),
    url(r'^privacy$', PrivacyView.as_view(), name='privacy_view'),
    url(r'^faqs$', FAQSView.as_view(), name='faqs_view'),
    url(r'^howitworks$', HOWITWORKSView.as_view(), name='howitworks_view')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
