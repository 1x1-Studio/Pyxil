import unittest

import pyxil.framework
from pyxil.framework.graphics import SpriteBatch


class GameTest(pyxil.framework.Game):
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
        
        self.assertIsInstance(game, pyxil.framework.Game)
        self.assertIsInstance(game.spriteBatch, SpriteBatch)
        self.assertIsInstance(game.gameTime, pyxil.framework.GameTime)
        self.assertIsInstance(game.gameWindow, (pyxil.framework.GameWindow, pyxil.framework.GameConsole))
