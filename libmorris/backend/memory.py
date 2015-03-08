from uuid import uuid4

from libmorris.player import Player
from libmorris.game   import Game

class Memory:
  def __init__(self):
    self.game_registry = {}

  def register(self):
    new_id = str(uuid4())
    self.game_registry[new_id] = Game()
    return new_id

  def find(self, game_id):
    return self.game_registry.get(game_id, None)

  def destroy(self, game_id):
    try:
      del self.game_registry[game_id]
      return True
    except KeyError:
      return False
