# PART 1

# TODO: this should be a fairly trivial class to implement
# the main thing is dealing with user input and parsing the equation
# We make the following assumptions for the input:
# - there is only two operations allowed: addition and subtraction
# - the numbers are integers
# - the equation items are always separated by a space (could be > 1spaces)
# You may not assume that the equation is valid (e.g. "5 ++ 3 - 1" is invalid)


class Calculator:
    def __init__(self, state: int = 0):
        # TODO: (2 pts)
        pass

    def add(self, value: int) -> None:
        """
        Add value to the current state
        """
        # TODO: (2 pts)
        pass

    def subtract(self, value: int) -> None:
        """
        Subtract value from the current state
        """
        # TODO: (2 pts)
        pass

    def get_state(self) -> int:
        """
        Get the current state
        """
        # TODO: (2 pts)
        pass

    def reset(self) -> None:
        """
        Reset the current state to 0
        """
        # TODO: (2 pts)
        pass


def main():
    """
    Main function that infinitely asks a user for an equation and prints the
    result of the equation (or an error)

    Example:
        Enter an equation: 1 + 1
        2
        Enter an equation: 2 - 3
        -1
        Enter an equation: 5 + 3 - 1
        7
        Enter an equation: 5 ++ 3 - 1
        Error: Invalid equation
    """
    # TODO: (15 pts)
    pass


if __name__ == "__main__":
    main()
