# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

import textworld
from textworld.challenges import coin_collector
import os
import shutil

def test_making_coin_collector():
    expected = {
        1: {"quest_length": 1, "nb_rooms": 1},
        20: {"quest_length": 20, "nb_rooms": 20},
        100: {"quest_length": 100, "nb_rooms": 100},
        101: {"quest_length": 1, "nb_rooms": 2},
        200: {"quest_length": 100, "nb_rooms": 200},
        201: {"quest_length": 1, "nb_rooms": 3},
        300: {"quest_length": 100, "nb_rooms": 300},
    }
    # for level in [1, 100, 101, 200, 201, 300]:
    level = 20
    options = textworld.GameOptions()
    options.seeds = 1234

    settings = {"level": level}
    game = coin_collector.make(settings, options)
    assert len(game.quests[0].commands) == expected[level]["quest_length"]
    assert len(game.world.rooms) == expected[level]["nb_rooms"]

    # zxf -s
    options.path = './coin_game_env/coin'
    folder, filename = os.path.split(options.path)
    if os.path.exists(folder):
        shutil.rmtree(folder)
    # zxf -e

    game_file = textworld.generator.compile_game(game, options)
    textworld.play(game_file)


if __name__ == '__main__':
    test_making_coin_collector()