import unittest

import pyxil.framework as framework


class GameTest(framework.Game):
    def __init__(self):
        super().__init__()

    def initialize(self):
        return super().initialize()

    def update(self, gameTime: None):
        return super().update(gameTime)

    def draw(self, spriteBatch: None):
        return super().draw(spriteBatch)


class TestGameClass(unittest.TestCase):

    def test_create_game_instance(self):
        game = GameTest()
        self.assertIsInstance(game, framework.Game)
