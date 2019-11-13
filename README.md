# Berlin Clock with explcit and named concepts

This is a companion repository to the [Embedding domain concepts in code article](https://www.freecodecamp.org/news/embedding-domain-concepts-in-code/).

Code should clearly reflect the problem it’s solving, and thus openly expose that problem’s domain. Embedding domain concepts in code requires thought and skill, and doesn't drop out automatically from TDD. 

The blog post discusses this, and references this repository as an example of pulling out implicit concepts and naming them, following a couple of earlier solutions to the Berlin Clock kata.

## Running the code

The code is designed for Python 3.x

- `python main.py`
- `python main.py < input.txt`

## Tests

There is no environment at the moment, so you will need to have pytest installed (`pip install pytest`).

- `pytest test_clock.py`
