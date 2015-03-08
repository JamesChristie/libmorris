from libmorris.backend.memory import Memory

from libmorris.game          import Game
from libmorris.reporter      import Reporter
from libmorris.game_advancer import GameAdvancer

persistence = Memory()

def register_game(**kwargs):
  return persistence.register(**kwargs)

def advance_game(game_id):
  game = persistence.find(game_id)
  GameAdvancer.resolve_next_turn(game)

def destroy_game(game_id):
  return persistence.destroy(game_id)

def game_exists(game_id):
  return get_game(game_id) != None

def get_game(game_id):
  game = persistence.find(game_id)
  return Reporter(game) if game else None
