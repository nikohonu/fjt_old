import typer

import fjt.anime
import fjt.log
import fjt.stats
from fjt.app import app

app.add_typer(fjt.log.app, name="log")
app.add_typer(fjt.stats.app, name="stats")


def main():
    app()


if __name__ == "__main__":
    main()
