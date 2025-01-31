# Summary of Python `print()` Function

The `print()` function in Python is used to output text or other data to the console. It is one of the most commonly used functions for displaying information. The basic syntax is:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

- **objects**: One or more objects to be printed, separated by a space by default.
- **sep**: Specifies the separator between objects. Default is a space.
- **end**: Specifies what to print at the end. Default is a newline character.
- **file**: Specifies the file or stream to write to. Default is `sys.stdout`.
- **flush**: If `True`, the stream is forcibly flushed. Default is `False`.

Example usage:

```python
print("Hello, World!")
print("Hello", "World", sep=", ", end="!\n")
```

The `print()` function is versatile and can handle multiple data types, including strings, numbers, and more complex objects.