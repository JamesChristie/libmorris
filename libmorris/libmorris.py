from libmorris.game   import Game
from libmorris.player import Player
from libmorris.errors import GameExistsError

game_registry = {}

def build_player(player_name, move_generator):
  return Player(player_name, move_generator)

def register_game(game_name):
  if game_exists(game_name):
    raise GameExistsError(game_name)
  else:
    game_registry[game_name] = Game()

def destroy_game(game_name):
  try:
    del game_registry[game_name]
    return True
  except KeyError:
    return False

def game_exists(game_name):
  if game_name in game_registry:
    return True
  else:
    return False
