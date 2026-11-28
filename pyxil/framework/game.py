from pyxil.framework.gametime import GameTime


class Game(object):
    """Base class for creating a Pyxil application.

    Override :meth:`initialize`, :meth:`update`, and :meth:`draw` to configure
    resources, implement game logic, and render the current frame.
    """

    def __init__(self):
        """Initialize a new :class:`Game` instance."""
        self.gameTime: GameTime = GameTime()

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
