# Libmorris
A Python implementation of a Tic-Tac-Toe game engine.

## Description
The game engine implemented here provides tools for managing and running games of tic-tac-toe, while assuming nothing about a particular interface consuming it. The engine does not provide a loop, or any driver code; this allows for, potentially, both synchronous and asynchronous play. Registration of a game allows for optional control of one or both players by providing lambda functions that will be called to allow hooking into decisions making.

An implementation of a minimax algorithm "perfect" AI player is also provided. Players that are not given a lambda hook will default to using this AI implementation. **The current implementation of this AI is the near perfect opposite of performant.** It has an efficiency of roughly O(n!) where n is the number of free spaces on the board. For a completely empty board, this means roughly 350,000 iterations to hazard a guess at a play. On a 2.8Ghz i7, it can take the AI up to 20 seconds to decide what to do on a blank board. However, performance increases exponentially with each claimed space in the game.

## Installation / Setup
The repository can be cloned locally by running:

```bash
git clone https://github.com/JamesChristie/libmorris.git
```

The repository includes a `.python-version` file to indicate the version of Python that was used during development. Other versions may work, but it would be best to check that file in your local version to ensure you have the same version available. By default, `pyenv` will automatically load the correct, installed version into the current `$PATH` when you enter the directory.

### Running the Test Suite

The provided `Makefile` includes tasks for most, if not all, common functions provided for managing the source code.

* Installing Dependencies

The provided `init` make task will install requirements for the test suite.

```bash
make init
```

* Executing Tests

There are two ways to execute the provided tests. The make task is highly recommended as it also runs linting of all code (and tests as well). Tests are executed via the normal unittest discovery as laid out in `pyspec.sh`.

```bash
# Execute tests and lint code
make dev

# Execute tests, skipping code checks
./pyspec.sh
```

Given that the AI player is slow and is also involed in the tests (with a couple empty board scenarios), you can expect the entire suite to take anywhere from 30 to 90 seconds to complete.

## Usage
This library can be used by hooking into a small set of simple API calls provided in the `libmorris` namespace. Multiple games can be registered and advanced at the same time, however currently all actions are blocking. This will affect any attempt to execute multiple games when one or more game has an AI player. The brute-force checking and scoring of a game and potential moves will hold up any other actions for the same PID until is is completed.

### Setting Up a Game
To register a new game in the engine, you can simply ask Libmorris to create one for you:

```python
import libmorris

# A super-simple hook example
player_hook = lambda game: return (1, 1)

game_id = libmorris.register_game(
            hook_one: player_hook
          )
```

The game registration functionality will return an id of a game, currently a string UUID. This id is a token for referencing the game to advance play and to check on a game's status.

To create a two player game, just provide lambda functions to both players:

```python
import libmorris

# Dueling lambdas!
player_one_hook = lambda game: return (1, 1)
player_two_hook = lambda game: return (2, 1)

game_id = libmorris.register_game(
            hook_one: player_one_hook,
            hook_two: player_two_hook
          )
```

Additionally, a game of two AI players can be generated, though this will most likely prove intensely uninteresting since they will both employ the same AI at this time.

```python
import libmorris

game_id = libmorris.register_game()
```

### Hook Interactions

Player hooks, will receive a game object (described in the following section) and are expected to return a two-element tuple as a return value. This tuple will be the representation of the space for which a move will be requested.

Hook functions are provided a decorated instance of a game (which is described in the Game Reporter section), they can use this representation of a game to make whatever move decisions are appropriate. The hook can also (as it is generally intended) reference interface code that can read synchronous, event-driven or queued user input to allow a human player to select their desired move.

```python
import libmorris

# Example super-simple lambda
player_hook = lambda game: game.get_free_positions()[0]

game_id = libmorris.register_game(
            hook_one: player_hook
          )

# Same functionality expressed as a function instead
def determine_move(game):
  free_positions = game.get_free_positions
  return free_positions[0]

game_id = libmorris.register_game(
            hook_one: determine_move
          )
```

#### Exceptions

When a move is requested, after a player hook produces a tuple of the position, there are some errors that can be raised. All exceptions inherit from `LibmorrisException` which inherits from `Exception` respectively.

* `MoveOutOfBounds`

This exception is raised when the tuple provided lists a position outside of the 3x3 game space.

* `InvalidMove`

This exception will be raised when the tuple provided references a space already owned by a player.

* `CannotMove`

This exception will be raised is a move is attempted outside of a player's allowed turn.

### Game Reporter

Libmorris provides a `Reporter` class to represent games in a particular state. It is intended that the reporter be used to interact with games in a non-destructive way. (No cheating dangit!)

#### Finding Games

Game representations can be obtained at any time from their id. Asking to get a game will return a `Reporter` instance wrapping the game in its current state. It returns `None` if not game matches that id.

```python
import libmorris

libmorris.get_game(game_id) # => <libmorris.reporter.Reporter object at ...>
```

You can also check for presense of games via:

```python
import libmorris

libmorris.game_exists(game_id) # => True / False
```

#### Reporter Interfaces

The `Reporter` class provides a set of interfaces to allow hook functions and interface code to obtain comprehensive and current information about game state. Players are represented by an `int` of `1` or `2`. For a game that has just been won by player 2, the interfaces will respond as such:

```python
import libmorris

report = libmorris.get_game(game_id)

report.is_over()        # => True
report.is_in_progress() # => False
report.is_tie()         # => False
report.last_player()    # => 1
report.current_player() # => 2
report.next_player()    # => None
report.winner()         # => 2
report.loser()          # => 1
```

The `Reporter` class also provides inspection of the current game state. You can obtain both a list of tuples representing the currently free positions as well as a dict representation of the entire play space:

```python
import libmorris

report = libmorris.get_game(game_id)

report.get_free_positions() # => [(1, 1), (2,3), ...etc]
report.get_current_board()  # => { (1, 2): 1, (2, 2): 2, ...etc}
```

### Advancing a Game

Since Libmorris assumes nothing about the interface and driving needs of its consumer, the interface itself is responsible for informing Libmorris when the state of a game should be advanced. This can be done by providing the id of the desired game to the advancement function:

```python
import libmorris

libmorris.advance_game(game_id)
```

This will advance the game a single turn (invoking any applicable player hooks provided), validate actions, swap current players, check victory conditions, and then halt before the next turn.

### Destroying a Game

A game can be unregistered and removed at any time by providing the game id to the destroy function:

```python
import libmorris

libmorris.destroy_game(game_id)
```

## Storage

Currently Libmorris only stores an in-memory registry of games. This can be altered be re-assigning the global `libmorris.persistence` with an instance of a class that supports current interfaces and will persist the game upon state changes (or when desired).

## Contributing or Modifying
Getting set up to modify or contribute to the codebase is as easy as forking the repository, stepping through the provided setup instructions, and then (optionally) opening a pull request on Github once your changes are done and tests are passing.

### Building a Python Egg
A distributable version of this library, complete with `setup.py` file can be generated by running:

```bash
make
```
