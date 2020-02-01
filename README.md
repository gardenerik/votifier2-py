# Votifier2

## Overview

Votifier protocol v2 client for Python.

Based on https://github.com/NuVotifier/votifier2-php/.

## Installation / Usage

To install use pip:

    pip install votifier2


## Example

```python
    from votifier2 import Server, Vote

    v = Vote("SERVICE", "ano95", "127.0.0.1")
    s = Server("127.0.0.1", 8192, "TOKEN")
    s.send_vote(v)
```