class LibmorrisException(Exception):
  pass

class GameNotfound(LibmorrisException):
  def __init__(self, game_id):
    message = (
      "No game could be found for the id: %s"
    )
    message = message % game_id
    super(GameNotfound, self).__init__(message)

class InvalidMove(LibmorrisException):
  def __init__(self, position):
    message = (
      "A move cannot be made to the position %d, %d "
      "because another player has occupied that space"
    )
    message = message % position
    super(InvalidMove, self).__init__(message)

class MoveOutOfBounds(LibmorrisException):
  def __init__(self, position):
    message = (
      "A move cannot be made to the position %d, %d "
      "because it is out of bounds"
    )
    message = message % position
    super(MoveOutOfBounds, self).__init__(message)

class CannotMove(LibmorrisException):
  def __init__(self, player):
    message = (
      "A move cannot be made for the given player because "
      "it is not their turn"
    )
    super(CannotMove, self).__init__(message)

class AmbiguousVictory(LibmorrisException):
  def __init__(self):
    message = (
      "A winner cannot be determined; victory sequences "
      "can be found for both players"
    )
    super(AmbiguousVictory, self).__init__(message)
