(a) Docstring
def find_max(numbers):
    """
    Find the maximum number in a list.
    Parameters:
        numbers (list): A list of integers or floats.
    Returns:
        int or float: The maximum value in the list.
    Examples:
        >>> find_max([10, 20, 5])
        20
        >>> find_max([-3, -7, -1])
        -1
        >>> find_max([2.5, 7.1, 3.3])
        7.1
    """
    return max(numbers)
if __name__ == "__main__":
    print(find_max([3, 7, 2, 9]))


(b)Inline comments
def find_max(numbers):
    # Use Python's built-in max() function
    # It will return the largest number in the list
    return max(numbers)
# Example run
print(find_max([3, 7, 2, 9]))  # Output: 9


(c) Google-style documentation
def find_max(numbers):
    """
    Find the maximum number in a list.
    Args:
        numbers (list[int | float]): A list of integers or floats.
    Returns:
        int | float: The maximum value in the list.
    Example:
        >>> find_max([3, 7, 2, 9])
        9
    """
    return max(numbers)


###OUTPUT:-
PS C:\Users\Madhava Krishna\OneDrive\Documents\AIAC> python Ass9_1.py
9
PS C:\Users\Madhava Krishna\OneDrive\Documents\AIAC> python -m doctest -v Ass9_1.py
Trying:
    find_max([10, 20, 5])
Expecting:
    20
ok
Trying:
    find_max([-3, -7, -1])
Expecting:
    -1
ok
NAME
    Ass9_1

FUNCTIONS
    find_max(numbers)
        Find the maximum number in a list.
        Parameters:
            numbers (list): A list of integers or floats.
        Returns:
            int or float: The maximum value in the list.
        Examples:
            >>> find_max([10, 20, 5])
            20
            >>> find_max([-3, -7, -1])
            -1
            >>> find_max([2.5, 7.1, 3.3])
            7.1
FILE
    c:\users\madhava krishna\onedrive\documents\aiac\ass9_1.py



Comparison of Documentation Styles
1. Docstring
Advantages:
Built directly into Python, so tools like help() and pydoc can display it.
Can include examples that can be tested with doctest.
Keeps documentation close to the function definition.
Disadvantages:
If too long, it can clutter the function.
Formatting is not standardized (different developers may write differently).
Best Use Case:
Small to medium projects where readability and quick reference are important.
Functions that need examples for testing.

2. Inline Comments
Advantages:
Very simple and beginner-friendly.
Explains logic line by line, useful for teaching or debugging.
Disadvantages:
Not structured; doesn’t integrate with tools like help().
Can make code messy if overused.
Best Use Case:
Small scripts, classroom exercises, or when explaining tricky logic step by step.

3. Google-style Documentation
Advantages:
Clear structure (Args, Returns, Example) makes it professional.
Widely used in industry, especially in large projects.
Works well with automated documentation generators.
Disadvantages:
Slightly longer to write compared to inline comments.
Requires consistency across the project.
Best Use Case:
Large projects, shared libraries, or professional codebases where multiple developers collaborate.


> The Google-style documentation is the most effective choice.

Reasoning:
Mathematical libraries often have many functions with different inputs and outputs.
Google-style provides a clear, standardized format that makes it easy for users to quickly understand what each function does.
It integrates well with automated tools, ensuring the library is examiner-ready and industry-standard.
Examples can still be included, making it useful for both beginners and advanced users.
