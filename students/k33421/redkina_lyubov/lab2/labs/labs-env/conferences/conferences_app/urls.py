from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Пути для конференций
    path('conferences/', views.all_conferences, name='all_conferences'),
    path('conference/<int:conference_id>/', views.conference_authors, name='conference_authors'),

    # Пути для авторов
    path('authors/', views.all_authors, name='all_authors'),
    path('authors/add/', views.AuthorCreateView.as_view(), name='add_author'),
    path('authors/edit/<int:pk>/', views.AuthorUpdateView.as_view(), name='edit_author'),

    # Пути для презентаций
    path('presentations/', views.all_presentations, name='all_presentations'),
    path('presentations/add/', views.PresentationCreateView.as_view(), name='add_presentation'),
    path('presentations/edit/<int:pk>/', views.PresentationUpdateView.as_view(), name='edit_presentation'),
    path('presentations/delete/<int:pk>/', views.PresentationDeleteView.as_view(), name='delete_presentation'),

    # Пути для регистраций
    path('registrations/', views.all_registrations, name='all_registrations'),
    path('registrations/add/', views.RegistrationCreateView.as_view(), name='add_registration'),
    path('registrations/edit/<int:pk>/', views.RegistrationUpdateView.as_view(), name='edit_registration'),
    path('registrations/delete/<int:pk>/', views.RegistrationDeleteView.as_view(), name='delete_registration'),

    # Пути для отзывов
    path('reviews/', views.all_reviews, name='all_reviews'),
    path('reviews/add/', views.ReviewCreateView.as_view(), name='add_review'),
    path('reviews/edit/<int:pk>/', views.ReviewUpdateView.as_view(), name='edit_review'),
    path('reviews/delete/<int:pk>/', views.ReviewDeleteView.as_view(), name='delete_review'),
]
