from libmorris.backend.memory import Memory

from libmorris.game    import Game
from libmorris.errors  import GameExistsError

persistence = Memory()

def register_game(**kwargs):
  return persistence.register(**kwargs)

def destroy_game(game_id):
  return persistence.destroy(game_id)

def game_exists(game_id):
  return find_game(game_id) != None

def find_game(game_id):
  return persistence.find(game_id)
