#!/usr/bin/env python3
""" Short description of this Python module.

Longer description of this module.

"""
import utils.console_helper as console
import utils.logging_helper as logging
import utils.profiling_helper as profiler

# ******************************************************************************** #

@logging.log
@profiler.profile_func
def add_nums_test (num1: int, num2: int) -> int:
    """adds two numbers as a test

    Args:
        num1 (int): Value 1
        num2 (int): Value 2_description_

    Returns:
        int: sum of numbers
    """	
    return num1 + num2


# ******************************************************************************** #

@profiler.profile_func
def main():
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/


    """

    console.print_ok_message("** This is the main method.** ")

    nums_test = add_nums_test(50,50)
    print (f"Adding nums: {nums_test}")


# ******************************************************************************** #

if __name__ == "__main__":
    main()
