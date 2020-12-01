# Python: poetry

Start with a new project without skeleton
```
poetry init
```

Install or activate a virtual environment
```
poetry shell
```

Install project dependencies - will install from `poetry.lock` if available,
from `pyproject.toml` if not.
```
poetry install
```

List outdated packages
```
poetry show --outdated
```
