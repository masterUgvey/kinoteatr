from django import forms

GENRE_CHOICES = [
    ('all', 'Все жанры'),
    ('sci-fi', 'Фантастика'),
    ('drama', 'Драма'),
    ('action', 'Боевик'),
]

THEME_CHOICES = [
    ('dark', 'Темная'),
    ('light', 'Светлая'),
]

class SettingsForm(forms.Form):
    genre = forms.ChoiceField(
        choices=GENRE_CHOICES,
        label='Выберите жанр',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    theme = forms.ChoiceField(
        choices=THEME_CHOICES,
        label='Тема оформления',
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )