# portfolio/urls.py
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.portfolio_view, name='portfolio'),  # Portfolio main page
    path('add/', views.add_project, name='add_project'),  # Page to add a new project
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about"),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('query-messages/', views.query_messages, name='query_messages'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files
