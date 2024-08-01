from django.contrib import admin
from .models import Genre, Filmwork, GenreFilmwork, Person, PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name', 'description') 


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline,) 
    list_display = ('title', 'type', 'creation_date', 'rating')
    list_filter = ('type',)
    search_fields = ('title', 'description', 'id')


class PersonFilmworkInline(admin.TabularInline):
    model=PersonFilmwork


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = (PersonFilmworkInline,) 
    list_display = ('full_name', 'gender')
    list_filter = ('gender',)
    search_fields = ('full_name', 'gender')