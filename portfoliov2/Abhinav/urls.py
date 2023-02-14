from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view() , name='about'),
    path('work/',views.WorkPage.as_view(), name= 'work'),
    path("work/1",views.PersonalPage.as_view(),name = "personal"),
    path("work/2",views.ContributePage.as_view(),name = "contribute"),
    path("work/3",views.PhotographyPage.as_view(),name = "photography"),
    path("contact/", views.ContactPage.as_view(), name="form")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)