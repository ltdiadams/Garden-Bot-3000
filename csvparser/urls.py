"""csvparser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# Growbot: create urls for different views of webapp
# To be deployed as a public webapp
#
# Logan DiAdams,
# For PHYS/COMP-3361
# 2019

from django.contrib import admin
from django.urls import path
from dataset.views import parse_data, fill_threshold
from django.conf.urls.static import static
from django.conf import settings
import dataset.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', parse_data),
    path('threshold/', fill_threshold),
    # path('upload/', new_csv)
    path('upload/', views.UploadFileView.as_view(), name='upload_my_file'),
    path('uploaded/?P<pk>\d+)/', views.UploadDetailView.as_view(), name='my_file')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)