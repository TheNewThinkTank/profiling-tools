
<a href="https://pypi.org/project/profiling-tools/">
<img src="https://img.shields.io/pypi/v/profiling-tools.svg">
</a>
<a href="https://github.com/TheNewThinkTank/msgspec/blob/main/LICENSE">
<img src="https://img.shields.io/github/license/TheNewThinkTank/profiling-tools.svg">
</a>

![PyPI Downloads](https://img.shields.io/pypi/dm/profiling-tools)
![CI](https://github.com/TheNewThinkTank/profiling-tools/actions/workflows/wf.yml/badge.svg)
[![codecov](https://codecov.io/gh/TheNewThinkTank/profiling-tools/graph/badge.svg?token=Xnca9AfHkt)](https://codecov.io/gh/TheNewThinkTank/profiling-tools)
![commit activity](https://img.shields.io/github/commit-activity/m/TheNewThinkTank/profiling-tools)
[![GitHub repo size](https://img.shields.io/github/repo-size/TheNewThinkTank/profiling-tools?style=flat&logo=github&logoColor=whitesmoke&label=Repo%20Size)](https://github.com/TheNewThinkTank/profiling-tools/archive/refs/heads/main.zip)

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
