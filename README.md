# Neko

This repository is for testing GitHub Actions that block merging when unit tests fail.

### Installing dependencies

```bash
# Example: install uv on Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Example: install uv on Windows
pip install uv

# Check version (tested with uv 0.8.3)
uv --version  # e.g. uv 0.8.3

# Install dependencies
uv sync

# Run tests
uv run pytest
```
