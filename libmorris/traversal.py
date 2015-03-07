board_range = range(1, 4)

def columns():
  return [
    [(column, y) for y in board_range] for column
    in board_range
  ]

def rows():
  return [
    [(x, row) for x in board_range] for row
    in board_range
  ]

def diagonals():
  return [
    [(column, diagonal[column-1]) for column in board_range] for diagonal
    in [list(reversed(board_range)), board_range]
  ]

def get_owners(positions, game_space):
  return set(
    game_space[position] for position
    in game_space
    if position in positions
  )

def single_owner(positions, game_space):
  unique_players = get_owners(positions, game_space)
  return len(unique_players) == 1 and (None not in unique_players)
