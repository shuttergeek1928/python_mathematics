# Basic Python Project

This project is a simple Python package that provides a class for performing basic mathematical operations. The `MathematicalOperation` class includes methods for addition, subtraction, and multiplication.

## Project Structure

```
basic-python-project
├── src
│   └── main.py
├── tests
│   └── test_main.py
├── setup.py
└── README.md
```

## Installation

To install the package, you can use the following command:

```bash
pip install .
```

Make sure you are in the root directory of the project when you run this command.

## Usage

To use the `MathematicalOperation` class, you can import it from the `src` module. Here is an example of how to use the class:

```python
from src.main import MathematicalOperation

math_op = MathematicalOperation()

# Addition
result_add = math_op.add(5, 3)
print(f"Addition: {result_add}")

# Subtraction
result_subtract = math_op.subtract(5, 3)
print(f"Subtraction: {result_subtract}")

# Multiplication
result_multiply = math_op.multiply(5, 3)
print(f"Multiplication: {result_multiply}")
```

## Running Tests

To run the tests for this project, you can use the following command:

```bash
pytest tests/
```

This will execute the test cases defined in the `tests/test_main.py` file.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request or open an issue for discussion.