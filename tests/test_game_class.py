import unittest

import pyxil.framework
from pyxil.framework.graphics import SpriteBatch


class GameTest(pyxil.framework.Game):
    def __init__(self, console: bool = False):
        super().__init__(console=console)

    def initialize(self):
        return super().initialize()

    def update(self, gameTime: None):
        return super().update(gameTime)

    def draw(self, spriteBatch: None):
        return super().draw(spriteBatch)


class GameTestWithError(pyxil.framework.Game):
    def __init__(self, console: bool = False):
        super().__init__(console=console)

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

    def test_create_game_console(self):
        game = GameTest(console=True)

        self.assertIsInstance(game, pyxil.framework.Game)
        self.assertIsInstance(game.spriteBatch, type(None))
        self.assertIsInstance(game.gameTime, pyxil.framework.GameTime)
        self.assertIsInstance(game.gameWindow, pyxil.framework.GameConsole)

    def test_game_loop(self):
        game = GameTest(console=True)
        counter_update = 0
        i = 5

        while i >= 1:
            game.update(game.gameTime)
            game.draw(None)
            counter_update = counter_update + 1
            i = i - 1
        
        self.assertEqual(counter_update, 5)
