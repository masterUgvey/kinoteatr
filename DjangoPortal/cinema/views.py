# cinema/views.py
from django.shortcuts import render
from .forms import SettingsForm
from .data import MOVIES

def index(request):
    selected_genre = 'all'
    selected_theme = 'dark'

    # Обработка формы настроек
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            selected_genre = form.cleaned_data['genre']
            selected_theme = form.cleaned_data['theme']
            
            # Сохраняем настройки в cookies
            response = render(request, 'cinema/index.html', {
                'form': form,
                'movies': MOVIES,
                'selected_genre': selected_genre,
                'selected_theme': selected_theme,
            })
            response.set_cookie('preferred_genre', selected_genre, max_age=30*24*60*60)
            response.set_cookie('preferred_theme', selected_theme, max_age=30*24*60*60)
            return response
    else:
        # Проверяем cookies, есть ли сохранённые настройки
        preferred_genre = request.COOKIES.get('preferred_genre', 'all')
        preferred_theme = request.COOKIES.get('preferred_theme', 'dark')
        form = SettingsForm(initial={
            'genre': preferred_genre,
            'theme': preferred_theme
        })
        selected_genre = preferred_genre
        selected_theme = preferred_theme

    # Фильтрация фильмов по жанру
    if selected_genre == 'all':
        filtered_movies = MOVIES
    else:
        filtered_movies = [movie for movie in MOVIES if movie['genre'] == selected_genre]

    return render(request, 'cinema/index.html', {
        'form': form,
        'movies': filtered_movies,
        'selected_genre': selected_genre,
        'selected_theme': selected_theme,
    })