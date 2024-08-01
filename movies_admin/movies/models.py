import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
        )
    
    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name 

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Type(models.TextChoices):
    MOVIE = 'movie', 'Movie'
    TV_SHOW = 'tv_show', 'Tv Show'


class Filmwork(UUIDMixin, TimeStampedMixin):
    certificate = models.CharField(_('certificate'), max_length=512, blank=True)
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
    genres = models.ManyToManyField(Genre, through='GenreFilmwork')
    file_path = models.FileField(_('file'), blank=True, null=True, upload_to='movies/')

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


class Gender(models.TextChoices):
    MALE = 'mail', _('male')
    FEMALE = 'female', _('femail')


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_('full name'), max_length=225, blank=False)
    gender = models.TextField(_('gender'), choices=Gender.choices, null=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = "content\".\"person"
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'


class PersonFilmwork(UUIDMixin):
    film_work=models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.TextField(_('role'))
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"