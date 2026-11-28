import pyxil


class Game1(pyxil.framework.Game):

    def __init__(self):
        super().__init__()


    def initialize(self):
        print("Initialize Game1")
        return super().initialize()


    def update(self, gameTime):
        return super().update(gameTime)


    def draw(self, spriteBatch):
        return super().draw(spriteBatch)


if __name__ == "__main__":
    game = Game1()
    game_loop = True

    while game_loop:
        game.update(game.gameTime)
        game.draw(None)
