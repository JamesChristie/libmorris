# NOTE (Jameschristie) Win detection is not implemented
# in constant time, since this library has support for
# unlooped, asynchronous play. The only alternative is
# to just check the entire board each time. This also
# results in the possibility of clients consuming
# libmorris producing circumstances that could be
# considered wins for both players. Given all that, it
# means this module has to be capable of an exhaustive,
# brute-force check of the entire board and all potential
# victory sequences.

from libmorris import traversal
from libmorris import sequencer

from libmorris.errors import AmbiguousVictory

class WinDetector:
  def __init__(self, game_space):
    self.game_space         = game_space
    self.eligible_sequences = sequencer.eligible_sequences(game_space)
    self.selected_victory   = []

  def winning_player(self):
    owners = traversal.get_owners(
      self.selected_victory,
      self.game_space
    )

    if len(owners) == 1:
      return list(owners)[0]
    else:
      return None

  def winning_positions(self):
    if self.game_is_won():
      self.selected_victory = self.eligible_sequences[0]
    elif self.eligible_sequences and not self.game_is_won():
      raise AmbiguousVictory()
    else:
      self.selected_victory = []

    return self.selected_victory

  def game_is_won(self):
    return self.single_victory() or self.same_winner()

  def single_victory(self):
    return len(self.eligible_sequences) == 1

  def same_winner(self):
    return traversal.single_owner(
      set([position for sequence in self.eligible_sequences
           for position in sequence]),
      self.game_space
    )
