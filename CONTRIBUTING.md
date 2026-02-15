# Contributing to LiteSlate

Thanks for your interest in contributing to LiteSlate!

## Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/Josh-writes/LiteSlate.git
   cd LiteSlate
   ```

2. **Set up a virtual environment** (optional but recommended)
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   ```

3. **Install in development mode**
   ```bash
   pip install -e .
   ```

## Running Locally

```bash
# Quick launch
python liteslate.py

# Or as a module
python -m liteslate
```

## Building the .exe

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Run the build script:
   ```bash
   python build.py
   ```

   The executable will be in the `dist/` folder.

## Code Style

- Keep it simple. LiteSlate is intentionally minimal.
- Use standard library only — no external dependencies.
- Follow PEP 8 where reasonable.

## Submitting Changes

1. Fork the repo and create a feature branch.
2. Make your changes.
3. Test that the app launches and basic functionality works.
4. Open a pull request with a clear description of what you changed and why.
