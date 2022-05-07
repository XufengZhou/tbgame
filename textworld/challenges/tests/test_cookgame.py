# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

import numpy as np

import textworld
from textworld.core import EnvInfos
from textworld.utils import make_temp_directory
from textworld.challenges import cookgame

import shutil
import os

NB_TRIALS = 10


def test_making_cooking_games():

    options = textworld.GameOptions()
    options.seeds = 1234
    options.file_ext = ".z8"

    nb_ingredients = 3

    settings = {
        "recipe": nb_ingredients,
        "take": 2,
        "open": True,
        "cook": True,
        "cut": False,
        "drop": True,
        "go": 1,
        "recipe_seed": 123,
        "split": "valid"
    }

    game = cookgame.make(settings, options)
    assert len(game.metadata["ingredients"]) == nb_ingredients

    # zxf -s
    options.path = './cooking_game_env/cooking'
    folder, filename = os.path.split(options.path)
    if os.path.exists(folder):
        shutil.rmtree(folder)
    # zxf -e

    game_file = textworld.generator.compile_game(game, options)
    print('game_file:have:', game_file)
    textworld.play(game_file)


if __name__ == '__main__':
    print('cooking_test')
    test_making_cooking_games()