# Random Language Study Selector

## Purpose
The Random Language Study Selector is designed to:
- **Diverse Learning**: Facilitate exposure to various programming languages, broadening technical knowledge and adaptability.
- **Study Efficiency**: Strategically select languages, ensuring a balanced learning approach without repetition until all options are exhausted.
- **User-Friendly Design**: Provide simple execution for immediate use in personal or educational settings.

## Getting Started
To discover your next programming language for study or practice, execute the script:

```bash
python language_selector.py
```

## Prerequisites
- Python 3.x environment

## Functionality
- Randomly selects from a list of languages including Lua, Go, Rust, Java, Scala, Clojure, C++, and C.
- Maintains a record of previously selected languages to ensure variety in each cycle.
- Resets the selection process after completing a full cycle of languages.

## File Overview
- `.last_used_languages`: Maintains a record of languages selected in the current cycle, ensuring efficient tracking and variety in learning.

## Testing
To ensure the highest quality and functionality, the Random Language Study Selector includes a suite of unit tests. These tests verify the integrity and correctness of the tool's core features.

### How to Run Tests
- The tests are written using Python's `unittest` framework.
- To run the tests, navigate to the project directory and execute:

  ```bash
  python -m unittest discover
  ```

## TODO:
* Add all necessary tests;
* Convert storage file to database, begin with sqlite;
* Evolve the project to random learner, given a list automaticly choose what to study
* create content tables, in a data folder?
