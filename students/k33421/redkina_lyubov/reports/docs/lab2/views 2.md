Файл `views.py` в Django - это место, где определяются функции (или классы) представлений, которые обрабатывают HTTP-запросы и возвращают HTTP-ответы. Он определяют то, как данные будут представлены и как пользователи будут взаимодействовать с приложением.
Можно сказать, что файл `views.py` централизует логику обработки запросов, что делает код более читаемым и поддерживаемым.

Функция `home(request)` возвращает базовую домашнюю страницу приложения и содержит ссылки на все остальные.
```
def home(request):
    return render(request, 'home.html', {})
```

Функции `all_authors`, `all_registrations`, `all_reviews`, `all_presentations`, `all_conferences` получают все записи из соответствующих моделей и передают их в соответствующие шаблоны.
```
def all_authors(request):
    authors_list = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors_list})

def all_registrations(request):
    registrations_list = Registration.objects.all()
    return render(request, 'registrations.html', {'registrations': registrations_list})

def all_reviews(request):
    reviews_list = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews_list})

def all_presentations(request):
    presentations_list = Presentation.objects.all()
    return render(request, 'presentations.html', {'presentations': presentations_list})

def all_conferences(request):
    conferences_list = Conference.objects.all()
    return render(request, 'conferences.html', {'conferences': conferences_list})
```


Далее я создаю функции `author_detail`, `registration_detail`, `review_detail`, `presentation_detail`, `conference_detail`. Они получают объекты по заданным идентификаторам и передают их в соответствующие шаблоны для детального отображения. Таким образом, они отображают детальную информации об авторе, регистрации, отзыве, выступлении и конференции.
```
def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author_detail.html', {'author': author})

def registration_detail(request, registration_id):
    registration = get_object_or_404(Registration, pk=registration_id)
    return render(request, 'registration_detail.html', {'registration': registration})

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})

def presentation_detail(request, presentation_id):
    presentation = get_object_or_404(Presentation, pk=presentation_id)
    return render(request, 'presentation_detail.html', {'presentation': presentation})

def conference_detail(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    return render(request, 'conference_detail.html', {'conference': conference})
```

Далее я создаю классы `AuthorCreateView`, `AuthorUpdateView`, `RegistrationCreateView`, `RegistrationUpdateView`, `RegistrationDeleteView`, `ReviewCreateView`, `ReviewUpdateView`, `PresentationCreateView`, `PresentationUpdateView`.
Эти классы наследуются от базовых классов Django и определяют логику для создания, обновления и удаления объектов соответствующих моделей. Они также указывают шаблоны и URL-адреса для перенаправления после успешных операций.
```
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'add_author.html'
    success_url = '/'

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'edit_author.html'
    success_url = '/'

class RegistrationCreateView(CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'add_registration.html'
    success_url = '/'

class RegistrationUpdateView(UpdateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'edit_registration.html'
    success_url = '/'

class RegistrationDeleteView(DeleteView):
    model = Registration
    template_name = 'delete_registration.html'
    success_url = '/'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'add_review.html'
    success_url = '/'

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'edit_review.html'
    success_url = '/'
class PresentationCreateView(CreateView):
    model = Presentation
    form_class = PresentationForm
    template_name = 'add_presentation.html'
    success_url = '/'

class PresentationUpdateView(UpdateView):
    model = Presentation
    form_class = PresentationForm
    template_name = 'edit_presentation.html'
    success_url = '/'
```

И наконец функция `conference_authors`. Эта функция формирует словарь авторов для выбранной конференции на основе данных о регистраций. Благодаря этому возможно отображение списка авторов, разбитый по конференциям.
```
def conference_authors(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    # Получаем все регистрации для данной конференции
    registrations = Registration.objects.filter(conference=conference)
    # Формируем словарь, где ключи - конференции, значения - списки авторов
    authors_by_conference = {}
    for registration in registrations:
        if registration.conference not in authors_by_conference:
            authors_by_conference[registration.conference] = []
        authors_by_conference[registration.conference].append({'author': registration.author, 'title': registration.title})
    return render(request, 'conference_authors.html', {'authors_by_conference': authors_by_conference})
```