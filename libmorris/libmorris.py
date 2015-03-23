from libmorris.backend.memory import Memory

from libmorris.game          import Game
from libmorris.reporter      import Reporter
from libmorris.game_advancer import GameAdvancer

persistence = Memory()

def register_game(**kwargs):
  """Register a new game with libmorris, returns a game id str.

  Keyword Arguments:
  hook_one -- A function or lambda to determine player 1's next move
  hook_two -- A function or lambda to determine player 2's next move
  """
  return persistence.register(**kwargs)

def advance_game(game_id, position=None):
  """Request a game, found by the given id, advance a single turn.
  
  Positional Arguments:
  game_id -- A str representing a game id
  """
  game = persistence.find(game_id)
  GameAdvancer.resolve_next_turn(game, position=position)

def destroy_game(game_id):
  """Request a game, found by the given id, be deleted from the registry.
  
  Positional Arguments:
  game_id -- A str representing a game id
  """
  return persistence.destroy(game_id)

def game_exists(game_id):
  """Return a True or False to indicate existance of a game for the given id.
  
  Positional Arguments:
  game_id -- A str representing a game id
  """
  return get_game(game_id) != None

def get_game(game_id):
  """Return a Reporter for a game of the given id.
  
  Positional Arguments:
  game_id -- A str representing a game id
  """
  game = persistence.find(game_id)
  return Reporter(game) if game else None
