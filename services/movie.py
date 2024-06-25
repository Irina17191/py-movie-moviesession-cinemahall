from django.db.models import QuerySet
from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet | Movie:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids)

    queryset = Movie.objects.all()

    if genres_ids:
        return queryset.filter(genres__id__in=genres_ids).distinct()

    if actors_ids:
        return queryset.filter(actors__id__in=actors_ids).distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> Movie:

    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)

    if genres_ids:
        for genre_id in genres_ids:
            movie.genres.add(genre_id)

    if actors_ids:
        for actors_id in actors_ids:
            movie.actors.add(actors_id)

    return movie
