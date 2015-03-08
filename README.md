# Libmorris
A Python implementation of a Tic-Tac-Toe game engine.

## Description
The game engine implemented here provides tools for managing and running games of tic-tac-toe, while assuming nothing about a particular interface consuming it. The engine does not provide a loop, or any driver code; this allows for, potentially, both synchronous and asynchronous play. Registration of a game allows for optional control of one or both players by providing lambda functions that will be called to allow hooking into decisions making.

An implementation of a minimax algorithm "perfect" AI player is also provided. Players that are not given a lambda hook will default to using this AI implementation.

## Installation / Setup
The repository can be cloned locally by running:

```bash
https://github.com/JamesChristie/libmorris.git
```

The repository includes a `.python-version` file to indicate the version of Python that that version was developed against. Other versions may work, but it would be best to check that file in your local version to ensure you have the same version available. By default, `pyenv` will automatically load the correct, installed version into the current `$PATH` when you enter the directory.

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

## Usage
This library can be used by hooking into a small set of simple API calls provided in the `libmorris` namespace. Multiple games can be registered and advanced at the same time, however currently all actions are blocking. This will affect any attempt to execute multiple games when one or more game has an AI player. The brute-force checking and scoring of a game and potential moves will hold up any other actions for the same PID until is is completed.

### Setting Up a Game
To register a new game in the engine, you can simply ask Libmorris to create one for you:

```python
import libmorris

# A super-simple hook example
hook_one = lambda game: return (1, 1)

game_id = libmorris.register_game(
            player_one_hook: hook_one
          )
```

The game registration functionality will return an id of a game, currently a string UUID. This id is a token for referencing the game to advance play and to check on a game's status.

To create a two player game, just provide lambda functions to both players:

```python
import libmorris

# Dueling lambdas!
hook_one = lambda game: return (1, 1)
hook_two = lambda game: return (2, 1)

game_id = libmorris.register_game(
            player_one_hook: hook_one,
            player_two_hook: hook_two
          )
```

Additionally, a game of two AI players can be generated, though this will most likely prove intensely uninteresting since they will both employ the same AI at this time.

```python
import libmorris

game_id = libmorris.register_game()
```

### Lambda Interactions

Lambda functions provided as player hooks will receive a game object (described in the following section) and are expected to return a two-element tuple as a return value. This tuple will be the representation of the space for which a move will be requested.

```python
# Example tuple return
return (3, 2)
```

#### Exceptions

When a move is requested, after a player hook produces a tuple of the position, there are some errors that can be raised. All exceptions inherit from `LibmorrisException` which inherits from `Exception` respectively.

```python
MoveOutOfBounds
```

This exception is raised when the tuple provided lists a position outside of the 3x3 game space.

```python
InvalidMove
```

This exception will be raised when the tuple provided references a space already owned by a player.

```python
CannotMove
```

This exception will be raised is a move is attempted outside of a player's allowed turn.

### Game Interaction

Explanation coming soon! I still need to write the presenter object.....

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
