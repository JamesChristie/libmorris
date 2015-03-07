from libmorris.errors import MissingAttribute

class Player:
  def __init__(self, **kwargs):
    try:
      self.name = kwargs['name']
    except KeyError:
      raise MissingAttribute(self.__class__.__name__, 'name')

    self.router = kwargs.get('router', None)

  def get_move(self, reporter):
    self.router(reporter)
