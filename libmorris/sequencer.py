from libmorris import traversal

def eligible_sequences(game_space):
  return (
    vertical_wins(game_space)   +
    horizontal_wins(game_space) +
    diagonal_wins(game_space)
  )

def vertical_wins(game_space):
  return [
    column for column in traversal.columns()
    if traversal.single_owner(column, game_space)
  ]

def horizontal_wins(game_space):
  return [
    row for row in traversal.rows()
    if traversal.single_owner(row, game_space)
  ]

def diagonal_wins(game_space):
  return [
    sequence for sequence in traversal.diagonals()
    if traversal.single_owner(sequence, game_space)
  ]
