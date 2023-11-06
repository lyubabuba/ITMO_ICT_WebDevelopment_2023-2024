from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Author, Conference, Registration, Presentation, Review
from .forms import PresentationForm, RegistrationForm, ReviewForm, AuthorForm

# Представление для отображения всех конференций
def all_conferences(request):
    conferences_list = Conference.objects.all()
    return render(request, 'conferences.html', {'conferences': conferences_list})

def all_authors(request):
    authors_list = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors_list})

def all_registrations(request):
    registrations_list = Registration.objects.all()
    return render(request, 'registrations.html', {'registrations': registrations_list})

def all_presentations(request):
    presentations_list = Presentation.objects.all()
    return render(request, 'presentations.html', {'presentations': presentations_list})

def all_reviews(request):
    reviews_list = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews_list})

# Представление для отображения всех авторов для выбранной конференций
def conference_authors(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    authors = Author.objects.filter(registration__conference=conference)
    return render(request, 'conference_authors.html', {'conference': conference, 'authors': authors})

# Представление для создания автора
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'add_author.html'
    success_url = reverse_lazy('authors_list')

# Представление для редактирования автора
class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'edit_author.html'
    success_url = reverse_lazy('authors_list')

# Представление для создания презентации
class PresentationCreateView(CreateView):
    model = Presentation
    form_class = PresentationForm
    template_name = 'add_presentation.html'
    success_url = reverse_lazy('presentations_list')

# Представление для редактирования презентации
class PresentationUpdateView(UpdateView):
    model = Presentation
    form_class = PresentationForm
    template_name = 'edit_presentation.html'
    success_url = reverse_lazy('presentations_list')

# Представление для удаления презентации
class PresentationDeleteView(DeleteView):
    model = Presentation
    template_name = 'delete_presentation.html'
    success_url = reverse_lazy('presentations_list')

# Представление для создания регистрации
class RegistrationCreateView(CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'add_registration.html'
    success_url = reverse_lazy('registrarions_list')

# Представление для редактирования регистрации
class RegistrationUpdateView(UpdateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'edit_registration.html'
    success_url = reverse_lazy('registrarions_list')

# Представление для удаления регистрации
class RegistrationDeleteView(DeleteView):
    model = Registration
    template_name = 'delete_registration.html'
    success_url = reverse_lazy('registrarions_list')

# Представление для создания отзыва
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'add_review.html'
    success_url = reverse_lazy('reviews_list')

# Представление для редактирования отзыва
class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'edit_review.html'
    success_url = reverse_lazy('reviews_list')

# Представление для удаления отзыва
class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'delete_review.html'
    success_url = reverse_lazy('reviews_list')

# Представление для домашней страницы
def home(request):
    return render(request, 'home.html', {})
