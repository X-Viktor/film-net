from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os

engine = create_engine(os.environ['DATABASE_URL'], echo=False)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    sex = Column(String, nullable=False)
    test_id = Column(Integer, ForeignKey('tests.id', ondelete='CASCADE'))
    watched_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'))
    recommended_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'))


class Test(Base):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    result = Column(String, nullable=False)


class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    year_create = Column(Date)
    budget = Column(Numeric)
    marketing = Column(Numeric)
    fees_usa = Column(Numeric)
    fees_ru = Column(Numeric)
    fees_world = Column(Numeric)
    premier_russia = Column(Date)
    premier_world = Column(Date)
    age_id = Column(Integer, ForeignKey('ages.id', ondelete='CASCADE'))
    rating_mpaa_id = Column(Integer, ForeignKey('ratings_mpaa.id', ondelete='CASCADE'))
    time = Column(Time, nullable=False)


class FilmWithIndexSites(Base):
    __tablename__ = 'films_with_index_sites'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    kinopoisk_id = Column(Integer, nullable=False)


class FilmName(Base):
    __tablename__ = 'film_names'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    name_ru = Column(String)
    name_en = Column(String)


class FilmCountry(Base):
    __tablename__ = 'film_country'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    country_id = Column(Integer, ForeignKey('country.id', ondelete='CASCADE'), nullable=False)


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Age(Base):
    __tablename__ = 'ages'

    id = Column(Integer, primary_key=True)
    age = Column(Integer)


class RatingMPAA(Base):
    __tablename__ = 'ratings_mpaa'

    id = Column(Integer, primary_key=True)
    rating_mpaa = Column(String)


class FilmGenre(Base):
    __tablename__ = 'film_genres'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id', ondelete='CASCADE'), nullable=False)


class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    genre = Column(String)


class FilmActor(Base):
    __tablename__ = 'film_actors'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    actor_id = Column(Integer, ForeignKey('genres.id', ondelete='CASCADE'), nullable=False)


class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    actor = Column(String)


class FilmKeyword(Base):
    __tablename__ = 'film_keywords'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    keyword_id = Column(Integer, ForeignKey('keywords.id', ondelete='CASCADE'), nullable=False)


class Keyword(Base):
    __tablename__ = 'keywords'

    id = Column(Integer, primary_key=True)
    keyword = Column(String)


class FilmRating(Base):
    __tablename__ = 'film_ratings'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    rating_kinopoisk = Column(Numeric)


class RatingCount(Base):
    __tablename__ = 'rating_counts'

    id = Column(Integer, primary_key=True)
    film_rating_id = Column(Integer, ForeignKey('film_ratings.id', ondelete='CASCADE'), nullable=False)
    count_kinopoisk = Column(Numeric)


class FilmScreenwriter(Base):
    __tablename__ = 'film_screenwriters'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    screenwriter_id = Column(Integer, ForeignKey('screenwriters.id', ondelete='CASCADE'), nullable=False)


class Screenwriter(Base):
    __tablename__ = 'screenwriters'

    id = Column(Integer, primary_key=True)
    screenwriter = Column(String)


class FilmProducer(Base):
    __tablename__ = 'film_producers'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    producer_id = Column(Integer, ForeignKey('producers.id', ondelete='CASCADE'), nullable=False)


class Producer(Base):
    __tablename__ = 'producers'

    id = Column(Integer, primary_key=True)
    producer = Column(String)


class FilmStageDirector(Base):
    __tablename__ = 'film_stage_directors'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    stage_director_id = Column(Integer, ForeignKey('stage_directors.id', ondelete='CASCADE'), nullable=False)


class StageDirector(Base):
    __tablename__ = 'stage_directors'

    id = Column(Integer, primary_key=True)
    stage_director = Column(String)


class FilmOperator(Base):
    __tablename__ = 'film_operators'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    operator_id = Column(Integer, ForeignKey('operators.id', ondelete='CASCADE'), nullable=False)


class Operator(Base):
    __tablename__ = 'operators'

    id = Column(Integer, primary_key=True)
    operator = Column(String)


class FilmComposer(Base):
    __tablename__ = 'film_composers'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    composer_id = Column(Integer, ForeignKey('composers.id', ondelete='CASCADE'), nullable=False)


class Composer(Base):
    __tablename__ = 'composers'

    id = Column(Integer, primary_key=True)
    composer = Column(String)


class FilmPainter(Base):
    __tablename__ = 'film_painters'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    painter_id = Column(Integer, ForeignKey('painters.id', ondelete='CASCADE'), nullable=False)


class Painter(Base):
    __tablename__ = 'painters'

    id = Column(Integer, primary_key=True)
    painter = Column(String)


class FilmEditor(Base):
    __tablename__ = 'film_editors'

    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    editor_id = Column(Integer, ForeignKey('editors.id', ondelete='CASCADE'), nullable=False)


class Editor(Base):
    __tablename__ = 'editors'

    id = Column(Integer, primary_key=True)
    editor = Column(String)
