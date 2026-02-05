# Lab 04: AI Prompts and Data Structure Recommendations

This document records the prompts used to consult with AI about data structure selection for Lab 04 problems.

---

## Problem 1: Finding Common Elements Between Two Lists

### Prompt Used

"I need to find which product IDs are present in both of two very large lists of integers. The order doesn't matter. What data structure should I use in Python to solve this efficiently? I want the best performance for this operation."

### AI Recommendation

**Data Structure: Sets (and set intersection)**

**Reasoning:**
Sets are the optimal data structure for this problem because:
1. **Fast intersection operation**: Python sets support the `&` operator for intersection, which is O(n + m) time complexity
2. **Automatic deduplication**: Sets automatically eliminate duplicate values
3. **Efficient for large lists**: Converting lists to sets is O(n), and intersection is very optimized at the C level
4. **No ordering requirement**: Since the problem states order doesn't matter, we don't need to preserve list order

**Implementation approach:**
```
1. Convert list1 to a set
2. Convert list2 to a set
3. Use the & operator to find intersection: set(list1) & set(list2)
4. Convert the result back to a list if needed
```

---

## Problem 2: User Profile Lookup by Username

### Prompt Used

"I have a list of user profile dictionaries, each with 'name', 'age', and 'email' fields. I need to frequently look up users by their username. Performance is critical because this lookup happens many times. What's the best data structure to use in Python?"

### AI Recommendation

**Data Structure: Dictionary (Hash Map)**

**Reasoning:**
Dictionaries are perfect for this use case because:
1. **O(1) average lookup time**: Dictionary lookups by key are constant time, much faster than linear searches through a list
2. **Key-value mapping**: The username naturally becomes the key, making lookups intuitive
3. **Direct access**: You can directly access the user dictionary using the name as key
4. **One-time conversion cost**: Convert the list to a dictionary once, then perform many fast lookups

**Implementation approach:**
```
1. Create a dictionary comprehension: {user['name']: user for user in users}
2. Use dict.get(name) to retrieve users, which returns None if not found
3. This provides both safety and convenience
```

**Performance comparison:**
- List search: O(n) - must check each user until found
- Dictionary lookup: O(1) - direct access via key

---

## Problem 3: Filtering Even Numbers While Preserving Order

### Prompt Used

"I have a list of integer sensor readings and I need to extract only the even numbers. The numbers must stay in the same order as they appeared in the original list. What's the best way to do this in Python?"

### AI Recommendation

**Data Structure: List Comprehension**

**Reasoning:**
List comprehension is the ideal approach because:
1. **Preserves order**: Iterates through the original list in sequence, maintaining order
2. **Pythonic and readable**: List comprehensions are the idiomatic Python way to filter and transform lists
3. **Efficient**: Single-pass iteration with O(n) time complexity
4. **Concise**: Much cleaner than writing a for loop with append statements
5. **Functional approach**: Expresses intent clearly (filter even numbers)

**Implementation approach:**
```
[num for num in numbers if num % 2 == 0]
```

**Why this is better than alternatives:**
- **vs. for loop + append**: List comprehension is more concise and Pythonic
- **vs. filter()**: List comprehension is more readable and easier to understand
- **vs. numpy**: Overkill for this simple task and adds dependency

---

## Summary of Data Structures Used

| Problem | Data Structure | Reason |
|---------|----------------|--------|
| Find common elements | **Sets** | Fast intersection, efficient deduplication |
| User lookup | **Dictionary** | O(1) lookups, natural key-value mapping |
| Filter even numbers | **List comprehension** | Preserves order, Pythonic, readable |

## Key Learning Points

1. **Choose the right data structure first**: Before coding, think about the operations you need to perform
2. **Performance matters**: Sets and dictionaries provide significant speedup for the right use cases
3. **Pythonic solutions**: List comprehensions are the idiomatic way to filter and transform data in Python
4. **Trade-offs**: Sometimes you pay a one-time cost (converting list to dict) to get many fast operations later
