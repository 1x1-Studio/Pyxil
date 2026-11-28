import os
import unittest

os.path.join(os.path.dirname(__file__), '../pyxil/framework/game.py')

import pyxil.framework as framework


class GameTest(framework.Game):
    def __init__(self):
        super().__init__()

    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        pass


class TestGameClass(unittest.TestCase):

    def test_create_game_instance(self):
        game = GameTest()
        self.assertIsInstance(game, framework.Game)
