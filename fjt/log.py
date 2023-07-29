import datetime as dt
import time

import click
import typer
from pytube import YouTube
from simple_term_menu import TerminalMenu
from typing_extensions import Annotated

from fjt.model import VN, Anime, Book, Listening, Manga, Reading, Readtime

app = typer.Typer()


def get_menu(data: list, emoji="🍙", new=True):
    input_data = [f"{emoji} {element}" for element in data]
    if new:
        data += ["New"]
        input_data += ["➕ New"]
    terminal_menu = TerminalMenu(input_data)
    index = terminal_menu.show()
    return data[index]


def get_list_of_anime():
    result = []
    for anime in reversed(list(Anime.select(Anime.title))):
        if anime.title not in result:
            result.append(anime.title)
    return result


def get_start_episode(title):
    anime = Anime.select(Anime.end, Anime.date_time).where(Anime.title == title)
    if anime.count():
        anime = list(anime)[-1]
    else:
        return 1
    return anime.end + 1


@app.command()
def anime(
    date_time: Annotated[dt.datetime, typer.Option()] = dt.datetime.utcnow(),
    title: Annotated[str, typer.Option()] = None,
    start: Annotated[int, typer.Option(min=1)] = None,
    end: Annotated[int, typer.Option(min=1)] = None,
    duration: Annotated[float, typer.Option(min=1.0)] = None,
):
    if not title:
        data = get_list_of_anime()
        title = "New" if not data else get_menu(data, new=True)
        if title == "New":
            title = click.prompt(text="Title")
        title = title.strip()
    start_episode = get_start_episode(title)
    start = (
        click.prompt(
            f"Start episode", type=click.types.IntRange(1), default=start_episode
        )
        if not start
        else start
    )
    end = (
        click.prompt(f"End episode", type=click.types.IntRange(1), default=start)
        if not end
        else end
    )
    duration = (
        click.prompt(
            f"Average episode duration", type=click.types.FloatRange(), default=21.0
        )
        if not duration
        else duration
    )
    anime = Anime.create(
        date_time=date_time, title=title, start=start, end=end, duration=duration
    )
    anime.log()
    print(f"9.5 points per episode ➡️ +{anime.points} points")


@app.command()
def listening(
    date_time: Annotated[dt.datetime, typer.Option()] = dt.datetime.utcnow(),
    url: Annotated[str, typer.Option()] = None,
    title: Annotated[str, typer.Option()] = None,
    duration: Annotated[float, typer.Option(min=1.0)] = None,
):
    url = click.prompt(text="URL", default="") if not url else url
    if not url:
        title = click.prompt(text="Title")
    else:
        title = YouTube(url).title
        time.sleep(1)
    duration = (
        click.prompt(f"Duration", type=click.types.FloatRange(), default=21.0)
        if not duration
        else duration
    )
    listening = Listening.create(
        date_time=date_time, url=url, title=title, duration=duration
    )
    listening.log()
    print(f"0.45 points/min of listening ➡️ +{listening.points} points")


def get_list_of_manga():
    result = []
    for manga in reversed(list(Manga.select(Manga.title))):
        if manga.title not in result:
            result.append(manga.title)
    return result


def get_start_manga_data(title):
    manga = Manga.select(Manga.end, Manga.volume, Manga.chapter).where(
        Manga.title == title
    )
    if manga.count():
        manga = list(manga)[-1]
    else:
        return 1, 1, 1
    return manga.end + 1, manga.volume, manga.chapter


@app.command()
def manga(
    date_time: Annotated[dt.datetime, typer.Option()] = dt.datetime.utcnow(),
    title: Annotated[str, typer.Option()] = None,
    start: Annotated[int, typer.Option(min=1)] = None,
    end: Annotated[int, typer.Option(min=1)] = None,
    volume: Annotated[float, typer.Option(min=1.0)] = None,
    chapter: Annotated[float, typer.Option(min=1.0)] = None,
    amount: Annotated[int, typer.Option(min=1.0)] = None,
):
    if not title:
        data = get_list_of_manga()
        title = "New" if not data else get_menu(data, emoji="🍜", new=True)
        if title == "New":
            title = click.prompt(text="Title")
        title = title.strip()
    start_page, start_volume, start_chapter = get_start_manga_data(title)
    start = (
        click.prompt(f"Start page", type=click.types.IntRange(1), default=start_page)
        if not start
        else start
    )
    end = (
        click.prompt(f"End page", type=click.types.IntRange(1), default=start)
        if not end
        else end
    )
    amount = (
        click.prompt(f"Amount", type=click.types.IntRange(1), default=end - start + 1)
        if not amount
        else amount
    )
    volume = (
        click.prompt(f"Volume", type=click.types.IntRange(1), default=start_volume)
        if not volume
        else volume
    )
    chapter = (
        click.prompt(f"Chapter", type=click.types.IntRange(1), default=start_chapter)
        if not chapter
        else chapter
    )
    manga = Manga.create(
        date_time=date_time,
        title=title,
        start=start,
        end=end,
        amount=amount,
        volume=volume,
        chapter=chapter,
    )
    manga.log()
    print(f"0.2 points per page ➡️ +{manga.points} points")


def get_list_of_book():
    result = []
    for book in reversed(list(Book.select(Book.title))):
        if book.title not in result:
            result.append(book.title)
    return result


def get_start_book_data(title):
    book = Book.select(Book.end, Book.volume, Book.chapter).where(Book.title == title)
    if book.count():
        book = list(book)[-1]
    else:
        return 1, 1, 1
    return book.end + 1, book.volume, book.chapter


@app.command()
def book(
    date_time: Annotated[dt.datetime, typer.Option()] = dt.datetime.utcnow(),
    title: Annotated[str, typer.Option()] = None,
    start: Annotated[int, typer.Option(min=1)] = None,
    end: Annotated[int, typer.Option(min=1)] = None,
    volume: Annotated[float, typer.Option(min=1.0)] = None,
    chapter: Annotated[float, typer.Option(min=1.0)] = None,
    amount: Annotated[int, typer.Option(min=1.0)] = None,
):
    if not title:
        data = get_list_of_book()
        title = "New" if not data else get_menu(data, emoji="🍘", new=True)
        if title == "New":
            title = click.prompt(text="Title")
        title = title.strip()
    start_page, start_volume, start_chapter = get_start_book_data(title)
    start = (
        click.prompt(f"Start page", type=click.types.IntRange(1), default=start_page)
        if not start
        else start
    )
    end = (
        click.prompt(f"End page", type=click.types.IntRange(1), default=start)
        if not end
        else end
    )
    amount = (
        click.prompt(f"Amount", type=click.types.IntRange(1), default=end - start + 1)
        if not amount
        else amount
    )
    volume = (
        click.prompt(f"Volume", type=click.types.IntRange(1), default=start_volume)
        if not volume
        else volume
    )
    chapter = (
        click.prompt(f"Chapter", type=click.types.IntRange(1), default=start_chapter)
        if not chapter
        else chapter
    )
    book = Book.create(
        date_time=date_time,
        title=title,
        start=start,
        end=end,
        amount=amount,
        volume=volume,
        chapter=chapter,
    )
    book.log()
    print(f"1 points per page ➡️ +{book.points} points")


def get_list_of_reading():
    result = []
    for reading in reversed(list(Reading.select(Reading.title))):
        if reading.title not in result:
            result.append(reading.title)
    return result


@app.command()
def reading(
    date_time: Annotated[dt.datetime, typer.Option()] = dt.datetime.utcnow(),
    title: Annotated[str, typer.Option()] = None,
    amount: Annotated[int, typer.Option(min=1.0)] = None,
):
    if not title:
        data = get_list_of_reading()
        title = "New" if not data else get_menu(data, emoji="🍡", new=True)
        if title == "New":
            title = click.prompt(text="Title")
        title = title.strip()
    amount = (
        click.prompt(f"Amount", type=click.types.IntRange(1), default=1)
        if not amount
        else amount
    )
    reading = Reading.create(
        date_time=date_time,
        title=title,
        amount=amount
    )
    reading.log()
    print(f"1/350 points/character ➡️ +{reading.points} points")


def get_list_of_vn():
    result = []
    for vn in reversed(list(VN.select(VN.title))):
        if vn.title not in result:
            result.append(vn.title)
    return result


@app.command()
def vn(
    date_time: Annotated[dt.datetime, typer.Option()] = dt.datetime.utcnow(),
    title: Annotated[str, typer.Option()] = None,
    amount: Annotated[int, typer.Option(min=1.0)] = None,
):
    if not title:
        data = get_list_of_vn()
        title = "New" if not data else get_menu(data, emoji="🍡", new=True)
        if title == "New":
            title = click.prompt(text="Title")
        title = title.strip()
    amount = (
        click.prompt(f"Amount", type=click.types.IntRange(1), default=1)
        if not amount
        else amount
    )
    vn= VN.create(
        date_time=date_time,
        title=title,
        amount=amount
    )
    vn.log()
    print(f"1/350 points/character ➡️ +{vn.points} points")
