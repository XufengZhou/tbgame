# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

import numpy as np

import textworld
from textworld.core import EnvInfos
from textworld.utils import make_temp_directory
from textworld.challenges import cooking

import shutil
import os

NB_TRIALS = 10


def test_making_cooking_games():

    options = textworld.GameOptions()
    options.seeds = 1234
    options.file_ext = ".z8"

    nb_ingredients = 2

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

    game = cooking.make(settings, options)
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

    # Check the game can be completed by following the walkthrough.
    # with make_temp_directory() as tmpdir:
    #     options.path = tmpdir
    #
    #     # zxf -s
    #     options.path = './tw_game_env/'
    #     if os.path.exists(options.path):
    #         shutil.rmtree(options.path)
    #     # zxf -e
    #
    #     game_file = textworld.generator.compile_game(game, options)
    #     textworld.play(game_file)
    #     infos = EnvInfos(admissible_commands=True, policy_commands=True)
    #
    #     # agent = textworld.agents.WalkthroughAgent()
    #     # env = textworld.start(game_file, infos)
    #     # agent.reset(env)
    #     # game_state = env.reset()
    #
    #     # reward = 0
    #     # done = False
    #     # while not done:
    #     #     command = agent.act(game_state, reward, done)
    #     #     assert command in game_state.admissible_commands, "Missing command {}".format(command)
    #     #     game_state, reward, done = env.step(command)
    #
    #     # assert done
    #     # assert game_state["won"]
    #
    #     def _assert_still_finishable(env, command):
    #         env = env.copy()
    #         game_state, _, done = env.step(command)
    #
    #         if not game_state["policy_commands"]:
    #             assert game_state.lost
    #             return
    #
    #         while not done:
    #             command = game_state["policy_commands"][0]
    #             game_state, _, done = env.step(command)
    #
    #         assert game_state.won
    #
    #     # Check the game can be completed by following the policy commands.
    #     env = textworld.start(game_file, infos)
    #
    #     game_state = env.reset()
    #
    #     rng = np.random.RandomState(20210510)
    #     done = False
    #     while not done:
    #         # Take a random action.
    #         random_command = rng.choice(game_state["admissible_commands"])
    #         _assert_still_finishable(env, random_command)
    #
    #         # Resume winning policy.
    #         command = game_state["policy_commands"][0]
    #         game_state, _, done = env.step(command)
    #
    #     assert game_state.won


if __name__ == '__main__':
    print('cooking_test')
    test_making_cooking_games()