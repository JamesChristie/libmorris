# NOTE (JamesChristie)
# This is an implementation of the minimax algorithm which
# is relatively common in implementations of tic-tic-toe AI.
# The extra twist of tracking the current depth of the search
# and subsequently using it to weight the score came from the
# delightful folks at Never Stop Building LLC who posted a
# lovely blog article explaining the rationale behind that
# particular quirk. The TestNearLoss example in the suite for
# this functionality is cribbed from his article detailing
# the weaknesses of skipping depth weighting.
#
# Minimax Algorithm
# -----------------
# http://en.wikipedia.org/wiki/Minimax
# https://chessprogramming.wikispaces.com/Minimax (All the sources!)
#
# Credit for depth weighting
# --------------------------
# Source: http://neverstopbuilding.com/minimax
# Author: Jason Fox (https://github.com/jasonrobertfox)

from libmorris.game_updater import GameUpdater

base_score = 10

class Perfect:
  @classmethod
  def get_perfect_move(self, player, game):
    return Perfect(player, game).get_best_move()

  def __init__(self, player, game, depth=0):
    self.player = player
    self.game   = game
    self.depth  = depth
    self.moves  = []

    self.generate_moves()

  def generate_moves(self):
    if self.game.is_in_progress():
      for position in self.game.get_free_positions():
        new_move = Move(position, self.derive_score_for(position))
        self.moves.append(new_move)

  def get_best_move(self):
    best_score   = self.get_best_move_score()
    # NOTE (JamesChristie) Sort by position to acheive predictability
    # among equal scores
    sorted_moves = sorted(self.moves, key=lambda move: move.position)

    return next(
      move.position for move in self.moves
      if move.score == best_score
    )

  def get_best_move_score(self):
    if self.moves:
      return max(move.score for move in self.moves)
    else:
      return 0

  def get_worst_move_score(self):
    if self.moves:
      return min(move.score for move in self.moves)
    else:
      return 0

  def score(self):
    if not self.moves:
      return self.get_self_score()
    elif self.game.current_player == self.player:
      return self.get_best_move_score()
    else:
      return self.get_worst_move_score()

  def get_self_score(self):
    if self.game.is_win_for(self.player):
      return base_score - self.depth
    elif self.game.is_loss_for(self.player):
      return self.depth - base_score
    else:
      return 0

  def derive_score_for(self, position):
    return self.new_ai_step(position).score()

  def new_ai_step(self, position):
    return Perfect(
      self.player,
      self.generate_potential_game(position),
      depth = (self.depth + 1)
    )

  def generate_potential_game(self, position):
    new_game = self.game.get_copy()

    GameUpdater.request_move(
      new_game, self.game.current_player, position
    )

    return new_game

class Move:
  def __init__(self, position, score):
    self.position = position
    self.score    = score
