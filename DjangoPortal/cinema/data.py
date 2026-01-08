# Базовый URL для медиафайлов
MEDIA_URL = '/images/posters/'

MOVIES = [
    {
        'id': 1,
        'title': 'Интерстеллар',
        'genre': 'sci-fi',
        'genre_display': 'Фантастика',
        'description': 'Фильм о путешествиях сквозь червоточины в космосе.',
        'year': 2014,
        'image_url': MEDIA_URL + 'interstellar.jpg'
    },
    {
        'id': 2,
        'title': 'Крестный отец',
        'genre': 'drama',
        'genre_display': 'Драма',
        'description': 'Эпическая история о сицилийской мафиозной семье.',
        'year': 1972,
        'image_url': MEDIA_URL + 'the_godfather.jpg'
    },
    {
        'id': 3,
        'title': 'Бегущий по лезвию 2049',
        'genre': 'sci-fi',
        'genre_display': 'Фантастика',
        'description': 'Продолжение культового фильма о будущем Лос-Анджелеса.',
        'year': 2017,
        'image_url': MEDIA_URL + 'blade_runner.jpg'
    },
    {
        'id': 4,
        'title': 'Джентльмены',
        'genre': 'action',
        'genre_display': 'Боевик',
        'description': 'Криминальная комедия о британском наркобароне.',
        'year': 2019,
        'image_url': MEDIA_URL + 'gentlemen.jpeg'
    },
    {
        'id': 5,
        'title': 'Начало',
        'genre': 'sci-fi',
        'genre_display': 'Фантастика',
        'description': 'Профессиональный вор внедряется в сны других людей.',
        'year': 2010,
        'image_url': MEDIA_URL + 'inception.jpg'
    },
    {
        'id': 6,
        'title': 'Форрест Гамп',
        'genre': 'drama',
        'genre_display': 'Драма',
        'description': 'История жизни человека с низким IQ, который стал свидетелем ключевых событий истории США.',
        'year': 1994,
        'image_url': MEDIA_URL + 'forrest.jpg'
    },
]

# Список жанров для формы
GENRES = [
    ('all', 'Все жанры'),
    ('sci-fi', 'Фантастика'),
    ('drama', 'Драма'),
    ('action', 'Боевик'),
]