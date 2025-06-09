# MiniInterpreter

This project implements a simple interpreter for evaluating basic arithmetic expressions and handling variable assignments and conditional statements. The interpreter supports variable declarations, arithmetic operations, and `if-then-else` constructs.

## Features

- Supports variable assignment using the `let` statement.
- Evaluates arithmetic expressions involving addition, subtraction, multiplication, and division.
- Handles conditional statements with `if-then-else` syntax.
- Allows for nested expressions and variable references.

## Installation

No external dependencies are required beyond Python 3.6 or newer.

## Usage

1. Create an instance of the `MiniInterpreter` class.
2. Call the `run` method with a list of commands to execute.

### Example

```python
from mini_interpreter import MiniInterpreter

commands = [
    "let x = 5",
    "let y = x + 3",
    "if x > 3 then x else y"
]

interpreter = MiniInterpreter()
interpreter.run(commands)