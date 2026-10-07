# Python - Input/Output

## Description

This project introduces Python's input/output mechanisms, focusing on file manipulation: opening, reading, writing and appending to files, and making sure file resources are managed properly with the `with` statement.

Understanding I/O is essential for real-world applications that store results, process external data, or communicate with other systems. It also supports future learning in databases, APIs, and data processing pipelines.

## Learning Objectives

- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What the `with` statement is and how to use it

## Key Concepts

### Opening a file

```python
open(filename, mode, encoding="utf-8")
```

Common modes:

| Mode | Meaning |
|------|---------|
| `"r"` | Read (default) |
| `"w"` | Write (overwrites the file) |
| `"a"` | Append (adds to the end) |
| `"r+"` | Read and write |

### The `with` statement

`with` guarantees the file is closed automatically, even if an error occurs, so there is no need to call `close()` manually.

```python
with open("my_file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### Reading

- `f.read()` reads the full content.
- `f.readline()` reads one line.
- `for line in f:` reads line by line.

### The `print` function and `end`

By default `print` adds a newline (`\n`) after the text. Using `end=""` prints the content exactly as it is, without any extra character.

```python
print(content, end="")
```

## Requirements

- Interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files end with a new line
- The first line of every file is exactly `#!/usr/bin/env python3`
- Code follows `pycodestyle` (version 2.7.*)
- All files are executable
- A `README.md` file at the root of the project folder is mandatory

## Tasks

### 0. Read file

File: `read_file.py`

Function that reads a UTF8 text file and prints it to stdout.

- Prototype: `def read_file(filename=""):`
- Must use the `with` statement
- No need to manage file permission or missing file exceptions
- No module imports allowed

```python
#!/usr/bin/env python3
"""Module that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Read a UTF8 text file and print its content."""
    with open(filename, "r", encoding="utf-8") as f:
        con = f.read()
        print(con, end="")
```

Example:

```
$ cat main.py
#!/usr/bin/env python3
read_file = __import__('read_file').read_file

read_file("my_file_0.txt")

$ ./main.py
We offer a truly innovative approach to education:
...
```

### 1. Write to a file

File: `write_file.py`

Function that writes a string to a UTF-8 text file and returns the number of characters written.

- Prototype: `def write_file(filename="", text=""):`
- Must use the `with` statement
- Creates the file if it doesn't exist
- Overwrites the content of the file if it already exists
- No module imports allowed

```python
#!/usr/bin/env python3
"""Module that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 file and return its length."""
    with open(filename, "w", encoding="utf-8") as f:
        d = f.write(text)
        return d
```

Example:

```
$ cat main.py
#!/usr/bin/env python3
write_file = __import__('write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

$ ./main.py
24
$ cat my_first_file.txt
This School is so cool!
```

### 2. Append to a file

File: `append_write.py`

Function that appends a string at the end of a UTF-8 text file and returns the number of characters added.

- Prototype: `def append_write(filename="", text=""):`
- Creates the file if it doesn't exist
- Must use the `with` statement
- No module imports allowed

```python
#!/usr/bin/env python3
"""Module that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append a string to a UTF8 file and return its length."""
    with open(filename, "a", encoding="utf-8") as f:
        app = f.write(text)
        return app
```

Example:

```
$ cat main.py
#!/usr/bin/env python3
append_write = __import__('append_write').append_write

nb_characters_added = append_write("file_append.txt", "Holberton School!\n")
print(nb_characters_added)

$ ./main.py
18
```

## Usage

```bash
chmod +x read_file.py write_file.py append_write.py main.py
./main.py
pycodestyle read_file.py write_file.py append_write.py
```

## Resources

- Reading and Writing Files (Python tutorial, section 7.2)
- Predefined Clean-up Actions (Python tutorial, section 8.7)
- Dive Into Python 3: Chapter 11. Files
- Learn to Program 8: Reading / Writing Files

## Author

Abdulrhman Saleh Alduqil
