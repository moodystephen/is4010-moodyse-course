def factorial(n):
    """Calculate the factorial of a non-negative integer.

    Parameters
    ----------
    n : int
        The non-negative integer to calculate the factorial of.

    Returns
    -------
    int
        The factorial of n. Returns 1 for n = 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(number):
    """Check if a number is a prime number.

    Parameters
    ----------
    number : int
        The integer to check.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def reverse_string(s):
    """Reverse a given string.

    Parameters
    ----------
    s : str
        The string to be reversed.

    Returns
    -------
    str
        The reversed string.
    """
    return s[::-1]


if __name__ == '__main__':
    # Demo when run directly
    print("✓ lab02.py executed successfully")
    print(f"  factorial(5) = {factorial(5)}")
    print(f"  is_prime(17) = {is_prime(17)}")
    print(f"  reverse_string('hello') = {reverse_string('hello')}")
