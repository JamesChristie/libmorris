import unittest

from libmorris.win_detector import WinDetector
from libmorris.errors       import AmbiguousVictory

class TestEmptyGame(unittest.TestCase):
  def setUp(self):
    self.game_space = {
      (1, 3): None, (2, 3): None, (3, 3): None,
      (1, 2): None, (2, 2): None, (3, 2): None,
      (1, 1): None, (2, 1): None, (3, 1): None
    }

    self.win_detector    = WinDetector(self.game_space)
    self.expected_series = []

  def test_winning_positions(self):
    self.assertCountEqual(
      self.win_detector.winning_positions(),
      self.expected_series
    )

class TestTiedGame(unittest.TestCase):
  def setUp(self):
    self.game_space = {
      (1, 3): 'X', (2, 3): 'O', (3, 3): 'X',
      (1, 2): 'O', (2, 2): 'X', (3, 2): 'O',
      (1, 1): 'O', (2, 1): 'X', (3, 1): 'O'
    }

    self.win_detector    = WinDetector(self.game_space)
    self.expected_series = []

  def test_winning_positions(self):
    self.assertCountEqual(
      self.win_detector.winning_positions(),
      self.expected_series
    )

class TestTopHorizontalWin(unittest.TestCase):
  def setUp(self):
    self.game_space = {
      (1, 3): 'X', (2, 3): 'X', (3, 3): 'X',
      (1, 2): 'X', (2, 2): 'O', (3, 2): 'O',
      (1, 1): 'O', (2, 1): 'O', (3, 1): 'X'
    }

    self.win_detector    = WinDetector(self.game_space)
    self.expected_series = [(1, 3), (2, 3), (3, 3)]

  def test_winning_positions(self):
    self.assertCountEqual(
      self.win_detector.winning_positions(),
      self.expected_series
    )

class TestMiddleHorizontalWin(unittest.TestCase):
  def setUp(self):
    self.game_space = {
      (1, 3): 'X', (2, 3): 'O', (3, 3): 'O',
      (1, 2): 'X', (2, 2): 'X', (3, 2): 'X',
      (1, 1): 'O', (2, 1): 'X', (3, 1): 'O'
    }

    self.win_detector    = WinDetector(self.game_space)
    self.expected_series = [(1, 2), (2, 2), (3, 2)]

  def test_winning_positions(self):
    self.assertCountEqual(
      self.win_detector.winning_positions(),
      self.expected_series
    )

class TestBottomHorizontalWin(unittest.TestCase):
  def setUp(self):
    self.game_space = {
      (1, 3): 'X', (2, 3): 'O', (3, 3): 'O',
      (1, 2): 'O', (2, 2): 'O', (3, 2): 'X',
      (1, 1): 'X', (2, 1): 'X', (3, 1): 'X'
    }

    self.win_detector    = WinDetector(self.game_space)
    self.expected_series = [(1, 1), (2, 1), (3, 1)]

  def test_winning_positions(self):
    self.assertCountEqual(
      self.win_detector.winning_positions(),
      self.expected_series
    )

class TestLeftVerticalWin(unittest.TestCase):
  def setUp(self):
    self.game_space = {
      (1, 3): 'X', (2, 3): 'X', (3, 3): 'O',
      (1, 2): 'X', (2, 2): 'O', (3, 2): 'O',
      (1, 1): 'X', (2, 1): 'O', (3, 1): 'X'
    }

    self.win_detector    = WinDetector(self.game_space)
    self.expected_series = [(1, 1), (1, 2), (1, 3)]

  def test_winning_positions(self):
    self.assertCountEqual(
      self.win_detector.winning_positions(),
      self.expected_series
    )

class TestMiddleVerticalWin(unittest.TestCase):
  def setUp(self):
    self.game_space = {
      (1, 3): 'X', (2, 3): 'X', (3, 3): 'O',
      (1, 2): 'O', (2, 2): 'X', (3, 2): 'X',
      (1, 1): 'O', (2, 1): 'X', (3, 1): 'O'
    }

    self.win_detector    = WinDetector(self.game_space)
    self.expected_series = [(2, 1), (2, 2), (2, 3)]

  def test_winning_positions(self):
    self.assertCountEqual(
      self.win_detector.winning_positions(),
      self.expected_series
    )

class TestRightVerticalWin(unittest.TestCase):
  def setUp(self):
    self.game_space = {
      (1, 3): 'X', (2, 3): 'O', (3, 3): 'X',
      (1, 2): 'O', (2, 2): 'O', (3, 2): 'X',
      (1, 1): 'O', (2, 1): 'X', (3, 1): 'X'
    }

    self.win_detector    = WinDetector(self.game_space)
    self.expected_series = [(3, 1), (3, 2), (3, 3)]

  def test_winning_positions(self):
    self.assertCountEqual(
      self.win_detector.winning_positions(),
      self.expected_series
    )

class TestLeftDiagonalWin(unittest.TestCase):
  def setUp(self):
    self.game_space = {
      (1, 3): 'X', (2, 3): 'O', (3, 3): 'X',
      (1, 2): 'O', (2, 2): 'X', (3, 2): 'O',
      (1, 1): 'O', (2, 1): 'O', (3, 1): 'X'
    }

    self.win_detector    = WinDetector(self.game_space)
    self.expected_series = [(1, 3), (2, 2), (3, 1)]

  def test_winning_positions(self):
    self.assertCountEqual(
      self.win_detector.winning_positions(),
      self.expected_series
    )

class TestRightDiagonalWin(unittest.TestCase):
  def setUp(self):
    self.game_space = {
      (1, 3): 'O', (2, 3): 'O', (3, 3): 'X',
      (1, 2): 'O', (2, 2): 'X', (3, 2): 'O',
      (1, 1): 'X', (2, 1): 'O', (3, 1): 'X'
    }

    self.win_detector    = WinDetector(self.game_space)
    self.expected_series = [(1, 1), (2, 2), (3, 3)]

  def test_winning_positions(self):
    self.assertCountEqual(
      self.win_detector.winning_positions(),
      self.expected_series
    )

class TestTwoWinSequences(unittest.TestCase):
  def setUp(self):
    self.game_space = {
      (1, 3): 'X', (2, 3): 'X', (3, 3): 'X',
      (1, 2): 'O', (2, 2): 'X', (3, 2): 'O',
      (1, 1): 'O', (2, 1): 'O', (3, 1): 'X'
    }

    self.win_detector    = WinDetector(self.game_space)
    self.expected_series = [(1, 3), (2, 3), (3, 3)]

  def test_winning_positions(self):
    self.assertCountEqual(
      self.win_detector.winning_positions(),
      self.expected_series
    )

class TestThreeWinSequences(unittest.TestCase):
  def setUp(self):
    self.game_space = {
      (1, 3): 'X', (2, 3): 'X', (3, 3): 'X',
      (1, 2): 'X', (2, 2): 'X', (3, 2): 'X',
      (1, 1): 'X', (2, 1): 'X', (3, 1): 'X'
    }

    self.win_detector    = WinDetector(self.game_space)
    self.expected_series = [(1, 1), (1, 2), (1, 3)]

  def test_winning_positions(self):
    self.assertCountEqual(
      self.win_detector.winning_positions(),
      self.expected_series
    )

class TestAmbiguousWin(unittest.TestCase):
  def setUp(self):
    self.game_space = {
      (1, 3): 'X', (2, 3): 'X', (3, 3): 'X',
      (1, 2): None, (2, 2): None, (3, 2): None,
      (1, 1): 'O', (2, 1): 'O', (3, 1): 'O'
    }

    self.win_detector = WinDetector(self.game_space)

  def test_winning_positions(self):
    with self.assertRaises(AmbiguousVictory):
      self.win_detector.winning_positions()
