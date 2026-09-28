"""Solve the FizzBuzz challenge for one user-entered number."""


def classify_number(number: int) -> str:
    """Return the required FizzBuzz result for a number from 1 to 100."""
    if not 1 <= number <= 100:
        raise ValueError("number must be between 1 and 100")

    # Check both divisors first so multiples of 15 are not labelled only "fizz".
    if number % 5 == 0 and number % 3 == 0:
        return "fizzbuzz"
    if number % 5 == 0:
        return "fizz"
    if number % 3 == 0:
        return "buzz"
    return f"{number} is not divisible by 3"


def main() -> None:
    """Read one integer, validate it and display its classification."""
    try:
        number = int(input("Enter a whole number from 1 to 100: "))
        print(classify_number(number))
    except ValueError:
        print("Please enter a whole number from 1 to 100.")


if __name__ == "__main__":
    main()
