class Reporter:
  def __init__(self, game):
    """Initialize a new Reporter.

    Positional Arguments:
    game -- An instance of a libmorris.game.Game class
    """
    self.game = game
    self.game.update_win_status()

  def is_over(self):
    """Return a True or False to indicate if a game is over."""
    return self.game.is_over()

  def is_in_progress(self):
    """Return a True or False to indicate if a game is still in progress."""
    return self.game.is_in_progress()

  def is_tie(self):
    """Return a True or False to indicate if a game is currently in a tied state."""
    return self.is_over() and not self.winner()

  def last_player(self):
    """Return an int or None representing the last player."""
    player = self.game.last_player
    return self.representation_for(player)

  def current_player(self):
    """Return an int representing the current player."""
    player = self.game.current_player
    return self.representation_for(player)

  def next_player(self):
    """Return an int or None representing the next player."""
    player = self.game.get_next_player()
    return self.representation_for(player)

  def winner(self):
    """Return an int or None representing the winner."""
    player = self.game.winner
    return self.representation_for(player)

  def loser(self):
    """Return an int representing the loser."""
    player = self.game.opponent(self.game.winner)
    return self.representation_for(player)

  def played_moves(self):
    """Return an int representing the number of played moves in total."""
    return self.game.played_moves

  def get_current_board(self):
    """Return a dict representing the current game play space.

    >>> reporter.get_current_board()
    { (1, 1): 1, (1, 2): 2 } # Normally has nine elements
    """
    get_owner = lambda position: self.game.game_space[position]
    get_rep   = lambda position: self.representation_for(get_owner(position))

    return dict(
      (position, get_rep(position))
      for position in self.game.game_space
    )

  def get_free_positions(self):
    """Return a list representing the currently free positions in the game.

    >>> reporter.get_free_positions()
    [(1, 1), (3, 2)]
    """
    return self.game.get_free_positions()

  def representation_for(self, player):
    if player == self.game.player_one:
      return 1
    elif player == self.game.player_two:
      return 2
    else:
      return None
