import datetime as dt

import click
import typer
from simple_term_menu import TerminalMenu
from typing_extensions import Annotated

from fjt.model import Anime, Listening

app = typer.Typer()


@app.command()
def anime():
    points = 0
    for anime in Anime.select():
        points += anime.points
        anime.log()
    print(points)


@app.command()
def listening():
    points = 0
    for listening in Listening.select():
        points += listening.points
        listening.log()
    print(points)
