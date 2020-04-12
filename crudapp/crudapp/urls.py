"""crudapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rick_and_morty_app.views import HomePageView, CreateCharacterView, CharacterUpdate, CharacterDetailView, DeleteCharacter
from django.conf import settings # new
from django.conf.urls.static import static # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='character_list'),
    path('create/', CreateCharacterView.as_view(), name='character_create'),
    path('update/<int:pk>', CharacterUpdate.as_view(), name='character_edit'),
    path('character/<int:pk>', CharacterDetailView.as_view(), name='character_details'),
    path('delete/<int:pk>', DeleteCharacter.as_view(), name='character_delete')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)