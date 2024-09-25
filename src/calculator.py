# PART 1

# DONE: this should be a fairly trivial class to implement
# the main thing is dealing with user input and parsing the equation
# We make the following assumptions for the input:
# - there is only two operations allowed: addition and subtraction
# - the numbers are integers
# - the equation items are always separated by a space (could be > 1spaces)
# You may not assume that the equation is valid (e.g. "5 ++ 3 - 1" is invalid)


class Calculator:
    def __init__(self, state: int = 0):
        # DONE: (2 pts)
        self.state = state

    def add(self, value: int) -> None:
        """
        Add value to the current state
        """
        # DONE: (2 pts)
        self.state += value

    def subtract(self, value: int) -> None:
        """
        Subtract value from the current state
        """
        # DONE: (2 pts)
        self.state -= value

    def get_state(self) -> int:
        """
        Get the current state
        """
        # DONE: (2 pts)
        return self.state

    def reset(self) -> None:
        """
        Reset the current state to 0
        """
        # DONE: (2 pts)
        self.state = 0


def validate_equation(equation: str) -> bool:
    values = equation.split()

    # nonempty equation
    if len(values) == 0:
        return False

    # numbers and operators alternate
    for i in range(len(values)):
        if i % 2 == 0:
            if not values[i].isdigit():
                return False
        else:
            if values[i] != "+" and values[i] != "-":
                return False

    # last value is a number
    return len(values) % 2 == 1


def process_equation(equation: str) -> int:
    if not validate_equation(equation):
        raise ValueError("Invalid equation")

    values = equation.split()
    if len(values) == 0:
        return 0

    calculator = Calculator(state=int(values[0]))

    op = None
    for i in range(1, len(values), 2):
        if values[i] == "+":
            op = calculator.add
        else:
            op = calculator.subtract
        op(int(values[i + 1]))

    return calculator.get_state()


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
    while True:
        equation = input("Enter an equation: ")
        try:
            value = process_equation(equation)
            print(value)
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
