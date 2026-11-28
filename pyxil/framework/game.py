from typing import Union

from pyxil.framework.gametime import GameTime
from pyxil.framework.gamewindow import GameWindow
from pyxil.framework.gameconsole import GameConsole

from pyxil.framework.graphics import SpriteBatch


class Game(object):
    """Base class for creating a Pyxil application.

    Override :meth:`initialize`, :meth:`update`, and :meth:`draw` to configure
    resources, implement game logic, and render the current frame.
    """

    def __init__(self, console: bool = False):
        """
        Initialize a new :class:`Game` instance.

        Args:
            console (bool, optional): Whether to use a console window. Defaults to False.
        """
        self.spriteBatch: Union[SpriteBatch, None] = SpriteBatch() if not console else None
        self.gameWindow: Union[GameWindow, GameConsole] = self.__set_window() 
        self.gameTime: GameTime = GameTime()
        self.initialize()

    def initialize(self):
        """Initialize the game and prepare its components.

        Override this method to create resources, configure instance variables,
        and perform one-time setup before the game starts updating.
        """
        pass

    def update(self, gameTime: None):
        """Update the game state for the current frame.

        Args:
            gameTime (None | GameTime): Information about the elapsed time and
                the current frame. Pass ``None`` only for applications that do
                not use a game loop.
        """
        pass

    def draw(self, spriteBatch: None):
        """Render the current game frame.

        Args:
            spriteBatch (None | SpriteBatch): The sprite batch used to submit
                graphics for rendering. Pass ``None`` when rendering is not
                needed or is handled by another mechanism.
        """
        pass

    def __set_window(self):
        if self.spriteBatch is not None:
            return GameWindow()
        return GameConsole()
