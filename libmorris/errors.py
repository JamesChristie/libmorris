class LibmorrisException(Exception):
  pass

class MissingAttribute(LibmorrisException):
  def __init__(self, class_name, attribute):
    message = "Cannot create %s without a %s" % class_name, attribute
    super(MissingAttribute, self).__init__(message)

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

class AmbiguousVictory(LibmorrisException):
  def __init__(self):
    message = (
      "A winner cannot be determined; victory sequences "
      "can be found for both players"
    )
    super(AmbiguousVictory, self).__init__(message)
