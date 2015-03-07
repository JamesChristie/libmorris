from uuid import uuid4

from libmorris.player import Player
from libmorris.game   import Game

class Memory:
  def __init__(self):
    self.game_registry = {}

  def register(self, **kwargs):
    new_game = self.build_game(**kwargs)
    new_id   = str(uuid4())
    self.game_registry[new_id] = new_game
    return new_id

  def find(self, game_id):
    return self.game_registry.get(game_id, None)

  def destroy(self, game_id):
    try:
      del self.game_registry[game_id]
      return True
    except KeyError:
      return False

  def build_game(self, **kwargs):
    return Game(
      name = kwargs.get('game_name', None),
      player_one = Player(
        name   = kwargs.get('player_one_name',   None),
        router = kwargs.get('player_one_router', None)
      ),
      player_two = Player(
        name   = kwargs.get('player_two_name',   None),
        router = kwargs.get('player_two_router', None)
      )
    )
