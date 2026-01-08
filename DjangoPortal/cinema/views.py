from django.shortcuts import render
from .forms import GenreForm
from .data import MOVIES

def index(request):
    selected_genre = 'all'

    # Обработка выбора жанра из формы
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            selected_genre = form.cleaned_data['genre']
            # Сохраняем выбор в cookies
            response = render(request, 'cinema/index.html', {
                'form': form,
                'movies': MOVIES,
                'selected_genre': selected_genre,
            })
            response.set_cookie('preferred_genre', selected_genre, max_age=30*24*60*60)  # 30 дней
            return response
    else:
        # Проверяем cookies, есть ли сохранённый жанр
        preferred_genre = request.COOKIES.get('preferred_genre', 'all')
        form = GenreForm(initial={'genre': preferred_genre})
        selected_genre = preferred_genre

    # Фильтрация фильмов по жанру
    if selected_genre == 'all':
        filtered_movies = MOVIES
    else:
        filtered_movies = [movie for movie in MOVIES if movie['genre'] == selected_genre]

    return render(request, 'cinema/index.html', {
        'form': form,
        'movies': filtered_movies,
        'selected_genre': selected_genre,
    })