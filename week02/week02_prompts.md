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

