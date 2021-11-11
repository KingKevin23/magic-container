# Magic Container

Thread-safe, lightweight and persistent dict for Python with a magical touch.

## Contents

<!---
* [Features](#features)
-->
* [Installation](#installation) 
* [Examples](#examples) 

### Installation:

`pip install magic-container`

### Examples:

Use it like a dict:

```python
from container import container

container["key"] = 3
print(container["key"])
del container["key"]
```

Or get the values while setting them if there aren't in the container:

```python
from container import container

print(container["second_key"], lambda: 23)
```

### Limitations:

1. Currently only works if installed and used in a virtual environment with write access to the venv folder.
2. Currently keys can only be strings.
3. Currently only the `get`, `set` and `delete` methods are defined.
