from django import forms

GENRE_CHOICES = [
    ('all', 'Все жанры'),
    ('sci-fi', 'Фантастика'),
    ('drama', 'Драма'),
    ('action', 'Боевик'),
]

class GenreForm(forms.Form):
    genre = forms.ChoiceField(
        choices=GENRE_CHOICES,
        label='Выберите жанр',
        widget=forms.Select(attrs={'class': 'form-control'})
    )