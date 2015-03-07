class LibmorrisException(Exception):
  pass

class GameExistsError(LibmorrisException):
  def __init__(self, game_name):
    message = "A game already exists with the name: %s" % game_name
    super(GameExistsError, self).__init__(message)

class InvalidMove(LibmorrisException):
  def __init__(self, position):
    message = (
      "A move cannot be made to the position %d, %d "
      "because another player has occupied that space"
    )
    super(InvalidMove, self).__init__(message)

class MoveOutOfBounds(LibmorrisException):
  def __init__(self, position):
    message = (
      "A move cannot be made to the position %d, %d "
      "because it is out of bounds"
    )
    super(MoveOutOfBounds, self).__init__(message)
