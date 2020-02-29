import argparse


def decimal_to_binary(x):
    """
    This function converts a decimal number N into a binary number with 8 bits.
    :param x: The decimal number

    >>> decimal_to_binary(30)
    '00011110'
    >>> decimal_to_binary(139)
    '10001011'
    """
    assert 0 <= x <= 255
    # START OF YOUR CODE
    pass

    # END OF YOUR CODE


def generate(rule, steps):
    """
    Generate the image from given rule number and steps
    and print it to the console.
    The output image should have width of 2 * STEPS + 1 and height of STEPS + 1.

    :param rule: The rule number
    :param steps: Number of lines

    >>> generate(30, 5)
    P1 11 6
    0 0 0 0 0 1 0 0 0 0 0
    0 0 0 0 1 1 1 0 0 0 0
    0 0 0 1 1 0 0 1 0 0 0
    0 0 1 1 0 1 1 1 1 0 0
    0 1 1 0 0 1 0 0 0 1 0
    1 1 0 1 1 1 1 0 1 1 1
    """
    # START OF YOUR CODE
    pass

    # END OF YOUR CODE


# TODO: You may add any additional functions here


if __name__ == '__main__':
    # START OF YOUR CODE
    # Parse command line arguments
    rule, steps = ...

    # END OF YOUR CODE

    assert 0 <= rule <= 255 and steps >= 0
    generate(rule, steps)
