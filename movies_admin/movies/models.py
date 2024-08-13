from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from .mixins import UUIDMixin, TimeStampedMixin
from django.utils.translation import gettext_lazy as _


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name 

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Filmwork(UUIDMixin, TimeStampedMixin):

    class Type(models.TextChoices):
        MOVIE = 'movie', 'Movie'
        TV_SHOW = 'tv_show', 'Tv Show'


    title=models.TextField(_('title'), max_length=225, blank=False) 
    description=models.TextField(_('description'), blank=True)
    creation_date=models.DateField(_('created time'), blank=True)
    rating= models.FloatField(
        _('rating'), 
        default=0.0, 
        blank=False,
        validators= [MinValueValidator(0), MaxValueValidator(100)]
        )
    type=models.CharField('type', choices=Type.choices, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

        indexes = [
            models.Index(fields=['film_work', 'genre'])
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['film_work', 'genre'],
                name='unique_filmwork_genre'
            ),
        ]


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_('full name'), max_length=225, blank=False)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = "content\".\"person"
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'


class PersonFilmwork(UUIDMixin):

    class PesonRole(models.TextChoices):
        DIRECTOR = 'director', _('Director')
        SCREENWRITER = 'screenwriter', _('Screenwriter')
        ACTOR = 'actor', _('Actor')
        COMPOSER = 'composer', _('Composer')
        CINEMATOGRAPHER = 'cinematographer', _('Cinematographer')
        EDITOR = 'editor', _('Editor')
        VOICE_ACTOR = 'voice_actor', _('Voice Actor')
        DUBBING_ACTOR = 'dubbing_actor', _('Dubbing Actor')

    film_work=models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.TextField(_('role'), choices=PesonRole.choices, default=PesonRole.ACTOR)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"

        indexes = [
            models.Index(fields=['film_work', 'person']),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['film_work', 'person', 'role'],
                name='unique_person_filmwork_role'
            ),
        ]