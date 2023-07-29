from enum import Enum

import click
import typer
from simple_term_menu import TerminalMenu
from typing_extensions import Annotated

from fjt.app import app
from fjt.model import Anime, Log, LogAnime, MediaType


class MediaTypeEnum(str, Enum):
    book = "book"
    manga = "manga"
    vn = "vn"
    anime = "anime"
    reading = "reading"
    readtime = "readtime"
    listening = "listening"


score_table = {
    "book": 1.0,
    "manga": 0.2,
    "vn": 1.0 / 350.0,
    "anime": 9.5,
    "reading": 1.0 / 350.0,
    "readtime": 0.45,
    "listening": 0.45,
}


def get_min_start_episode(anime):
    start = 1
    logs = LogAnime.select(LogAnime.end).where(LogAnime.anime == anime)
    if logs:
        start = max(log.end for log in logs) + 1
    return start


def float_to_int_or_remove_decimal(number_str):
    try:
        float_number = float(number_str)
        if float_number.is_integer():
            return int(float_number)
        else:
            return float_number
    except ValueError:
        # If the input is not a valid float, return the original string
        return number_str


@app.command()
def log_anime():
    # anime
    anime_list = [anime.name for anime in Anime.select(Anime.name)]
    terminal_menu = TerminalMenu(anime_list)
    index = terminal_menu.show()
    anime = Anime.get(Anime.name == anime_list[index])
    print(anime.name)
    # current episode
    min_start_episode = get_min_start_episode(anime)
    if min_start_episode > anime.episodes:
        return
    start = click.prompt(
        f"The number of the first episode you watched ({1}-{anime.episodes})",
        type=click.types.IntRange(min_start_episode, anime.episodes),
        default=min_start_episode,
    )
    end = click.prompt(
        f"The number of the last episode you watched ({1}-{anime.episodes})",
        type=click.types.IntRange(min_start_episode, anime.episodes),
        default=anime.episodes,
    )
    log_anime = LogAnime.create(anime=anime, start=start, end=end)
    log_command = f".log anime {float_to_int_or_remove_decimal(log_anime.amount)} {anime.name}"
    if log_anime.amount > 1:
        log_command += f" EPS {log_anime.start}-{log_anime.end}"
        if log_anime.end == anime.episodes:
            log_command += f" FIN"
    else:
        log_command += f" EP {log_anime.start}"
    print(log_command)


#     media_type: Annotated[MediaTypeEnum, typer.Argument()] = None,
#     amount: Annotated[int, typer.Option(min=1)] = None,
# ):
#     if not media_type:
#         terminal_menu = TerminalMenu(MediaTypeEnum._member_names_)
#         index = terminal_menu.show()
#         media_type = MediaTypeEnum._member_names_[index]
#     else:
#         media_type = media_type.name
#     # print(f"Media type: {media_type}")
#     if not amount:
#         amount = click.prompt("Amount", type=click.types.IntRange(1))
#     match media_type:
#         case "anime":
#             Log.create()
#
#         case _:
#             print("WIP")

# if not name:
#     name = click.prompt("Name")
# print(f".log {media_type} {amount} {name}")
# print(f"{score_table[media_type] * amount}")


# import datetime as dt
# import json
# from pathlib import Path
#
# import appdirs
#
# from fjt.formatting import print
#
# log_types_short = {"b": "book", "m": "manga", "vn": "vn", ""}
#
# score_table = {
#     "book": 1.0,
#     "manga": 0.2,
#     "vn": 1.0 / 350.0,
#     "anime": 9.5,
#     "reading": 1.0 / 350.0,
#     "readtime": 0.45,
#     "listening": 0.45,
# }
#
# data_path = Path(appdirs.user_data_dir("fjt", "nikohonu"))
# data_path.mkdir(parents=True, exist_ok=True)
#
#
# @click.command()
# @click.option(
#     "-t", "--log-type", type=click.Choice(log_types, case_sensitive=False), prompt=True
# )
# @click.option("-a", "--amount", type=click.IntRange(1), prompt=True)
# @click.option("-n", "--name", type=str, prompt=True)
# def log(log_type, amount, name):
#     file_path = data_path / "data.json"
#     try:
#         with file_path.open(mode="r") as file:
#             data = json.load(file)
#     except FileNotFoundError:
#         data = []
#     row = {
#         "date": dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
#         "type": log_type,
#         "amount": amount,
#         "name": name,
#     }
#     print(data)
#     match log_type:
#         case "book":
#             row["page"] = click.prompt(text="Page", type=click.IntRange(1))
#             row["volume"] = click.prompt(
#                 text="Volume", type=click.IntRange(1), default=4
#             )
#             row["chapter"] = click.prompt(text="Chapter", type=click.IntRange(1))
#         case "manga":
#             row["page"] = click.prompt(text="Page", type=click.IntRange(1))
#             row["volume"] = click.prompt(text="Volume", type=click.IntRange(1))
#             row["chapter"] = click.prompt(text="Chapter", type=click.IntRange(1))
#         case "vn":
#             pass
#         case "anime":
#             row["episode"] = click.prompt(text="Episode", type=click.IntRange(1))
#             pass
#         case "reading":
#             pass
#         case "readtime":
#             pass
#         case "listening":
#             pass
#     row["points"] = amount * score_table[log_type]
#     data.append(row)
#     with file_path.open(mode="w") as file:
#         json.dump(data, file, indent=4)
#
#
# @click.command()
# def dropdb():
#     click.echo("Dropped the database")
