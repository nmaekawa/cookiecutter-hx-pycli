# -*- coding: utf-8 -*-

"""Console script for hxann."""
import contextlib
import os
import sys

import click
from dotenv import load_dotenv

# if dotenv file, load it
dotenv_path = os.environ.get("{{cookiecutter.project_prefix}}_DOTENV_PATH", None)
if dotenv_path:
    # BEWARE that dotenv overrides what's already in env
    load_dotenv(dotenv_path, override=True)


@click.command()
@click.option(
    "--arg",
    default="value",
    help="some argument for this command",
)
def cli(arg):
    click.echo("arg is {}".format(arg))


# from http://stackoverflow.com/a/29824059
@contextlib.contextmanager
def _smart_open(filename, mode="Ur"):
    if filename == "-":
        if mode is None or mode == "" or "r" in mode:
            fhandle = sys.stdin
        else:
            fhandle = sys.stdout
    else:
        fhandle = open(filename, mode)

    try:
        yield fhandle
    finally:
        if filename != "-":
            fhandle.close()


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
