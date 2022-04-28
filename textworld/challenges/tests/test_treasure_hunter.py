# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.
import os

import textworld
from textworld.challenges import treasure_hunter
from textworld.utils import make_temp_directory
import shutil
from textworld.generator import compile_game

CAPACITY = 10

def make_temp_players():
    a = {'name': 'Alice', 'room_id': 0, 'capacity': CAPACITY}
    b = {'name': 'Bob', 'room_id': 3, 'capacity': CAPACITY}
    return [a, b]

def test_hunter_game_play(level=2):
    print('level:{}'.format(level))
    options = textworld.GameOptions()
    options.seeds = 1234

    settings = {"level": level}
    game = treasure_hunter.make(settings, options)
    assert len(game.quests[0].commands) == game.metadata["quest_length"], "Level {}".format(level)
    assert len(game.world.rooms) == game.metadata["world_size"], "Level {}".format(level)

    # players
    players = make_temp_players()
    game.add_player_entities(players)

    options.path = './hunter_game_env/hunter'
    folder, filename = os.path.split(options.path)
    if os.path.exists(folder):
        shutil.rmtree(folder)

    game_file = textworld.generator.compile_game(game, options)
    textworld.play(game_file)


if __name__ == '__main__':
    print('Hunter game：')
    test_hunter_game_play(level=8)