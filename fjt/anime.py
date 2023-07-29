import typer
from typing_extensions import Annotated

from fjt.model import Anime

app = typer.Typer()


@app.command()
def add(
    name: Annotated[str, typer.Option(prompt=True)],
    episodes: Annotated[int, typer.Option(min=1, prompt=True)],
    duration: Annotated[
        int,
        typer.Option(
            min=1, prompt="Average episode length (excluding OP and ED (24-3=21))"
        ),
    ] = 21,
):
    name = name.strip()
    Anime.create(name=name, episodes=episodes, duration=duration)


@app.command()
def ls():
    pass


@app.command()
def delete():
    pass
