from libmorris.backend.memory import Memory

from libmorris.game     import Game
from libmorris.reporter import Reporter

persistence = Memory()

def register_game():
  return persistence.register()

def destroy_game(game_id):
  return persistence.destroy(game_id)

def game_exists(game_id):
  return find_game(game_id) != None

def find_game(game_id):
  return persistence.find(game_id)

def build_reporter(game):
  return Reporter(game)
