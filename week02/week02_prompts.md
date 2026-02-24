# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**Context**:
```text
I have a function that's supposed to calculate the sum of all even numbers in a list, but it returns the wrong result. Here's the code:

def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total
```

**Persona**: You are a senior Python developer and debugging coach.

**Task**: Identify the bug, explain why it fails, and provide a corrected implementation.

**Format**: Short explanation followed by corrected code block.

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Return the sum of even integers in `numbers`.

    The original function added odd numbers because it checked `num % 2 == 1`.
    The fix is to check for evenness with `num % 2 == 0`.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total
```

**What I Learned:**
- Small boolean mistakes invert behavior; writing a short test (e.g., [1,2,3,4]) quickly exposes the bug.

---

## Problem 2: Refactoring

**Context**:
```text
This function returns the names of users aged 18 or older but is written in a non-Pythonic style.

def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
```

**Persona**: You are a senior Python engineer focusing on readability and idiomatic code.

**Task**: Refactor the function to be more Pythonic and concise while preserving behavior.

**Format**: Provide the refactored code and a one-line explanation of the improvement.

**AI's Refactored Code:**
```python
def get_names_of_adults(users):
    """Return names of users aged 18 or older.

    Uses a list comprehension for clarity and concise iteration.
    """
    return [user['name'] for user in users if user.get('age', 0) >= 18]
```

**What I Learned:**
- List comprehensions express transformation+filter logic clearly and avoid index-based access.

---

## Problem 3: Documenting

**Context**:
```text
A working function has no docstring. Add a NumPy-style docstring that documents parameters, return value, and the ValueError raised for invalid inputs.

def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**Persona**: You are a technical writer and senior Python developer who writes clear NumPy-style docstrings.

**Task**: Provide a NumPy-style docstring for `calculate_area` explaining params, return, and exceptions.

**Format**: Provide only the function with the docstring filled in.

**AI's Documented Code:**
```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Parameters
    ----------
    length : float
        The length of the rectangle (must be positive).
    width : float
        The width of the rectangle (must be positive).

    Returns
    -------
    float
        The area computed as `length * width`.

    Raises
    ------
    ValueError
        If `length` or `width` is not a positive number.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**What I Learned:**
- A clear docstring communicates function contract to humans and tools (including AI).

---

## Submission notes

- `week02/lab02.py` implements the three functions and can be validated interactively.
- `week02/week02_prompts.md` documents prompts and the AI-provided solutions as required by the lab.
# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
> You are a senior Python developer.  
>
> I have a function that is supposed to calculate the sum of all **even**
> numbers in a list, but it is returning incorrect results.
>
> Here is the code:
>
> ```python
> def sum_of_evens(numbers):
>     total = 0
>     for num in numbers:
>         if num % 2 == 1:
>             total += num
>     return total
# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
> You are a senior Python developer.  
>
> I have a function that is supposed to calculate the sum of all **even**
> numbers in a list, but it is returning incorrect results.
>
> Here is the code:
>
> ```python
> def sum_of_evens(numbers):
>     total = 0
>     for num in numbers:
>         if num % 2 == 1:
>             total += num
>     return total
> ```
# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
> You are a senior Python developer.  
>
> I have a function that is supposed to calculate the sum of all **even**
> numbers in a list, but it is returning incorrect results.
>
> Here is the code:
>
> ```python
> def sum_of_evens(numbers):
>     total = 0
>     for num in numbers:
>         if num % 2 == 1:
>             total += num
>     return total
> ```
>
> Can you identify the logical bug and provide the corrected version of
> the function in a Python code block?

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total
def get_names_of_adults(users):
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results

def get_names_of_adults(users):
    return [user["name"] for user in users if user["age"] >= 18]
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Parameters
    ----------
    length : int or float
        The length of the rectangle. Must be positive.
    width : int or float
        The width of the rectangle. Must be positive.

    Returns
    -------
    int or float
        The area of the rectangle.

    Raises
    ------
    ValueError
        If length or width is less than or equal to zero.

    Examples
    --------
    >>> calculate_area(5, 3)
    15
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

