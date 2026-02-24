"""
Top-level shim for Lab 00 that re-exports functions from `week00/lab00.py`.
This allows tests that import `lab00` to work without changing test code.
"""

from week00.lab00 import hello_world, add_numbers

__all__ = ["hello_world", "add_numbers"]
