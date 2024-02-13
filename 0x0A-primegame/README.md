# Prime Game

## Description
This program implements the Prime Game, where two players take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n. The player who cannot make a move loses the game. The program determines the winner of each round of the game.

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)

## Usage
1. Clone the repository:
    ```
    git clone https://github.com/Donphili/alx-interview.git
    ```

2. Navigate to the project directory:
    ```
    cd alx-interview/0x0A-primegame
    ```

3. Run the main script:
    ```
    ./main.py
    ```

4. Adjust the input parameters in the main script (`main.py`) to test different scenarios.

## Example
```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

# Author

https://github.com/Donphili
