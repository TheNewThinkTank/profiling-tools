# profiling-tools

Python profiling tools using **cProfile** and **pstats**

## Installation

```BASH
pip install profiling-tools
```

## Usage example

Importing

```Python
from profiling_tools.profiling_utils import profile
```

Usage as decorator

```Python
@profile
def some_function():
    ...
```

Running your function `some_function` with the `profile` decorator
produces a file `stats/some_function.stats` containing the results of the profiling
created with cProfile.
This file can then be analyzed and visualized using the `analyze_stats` module.

<!--
## Create a new release

example:

```BASH
git tag 0.0.1
git push origin --tags
```

release a patch:

```BASH
poetry version patch
```

then `git commit`, `git push` and

```BASH
git tag 0.0.2
git push origin --tags
```
-->
