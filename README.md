# LiteSlate

**Distraction-free writing for Windows** — the free companion to [TypeSlate](https://typeslate.com).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

LiteSlate gives you a fullscreen, blank canvas to write on with zero distractions. No toolbars, no menus, no formatting options — just you and your words. Your work is autosaved continuously so you never lose a thought.

## Features

- **Fullscreen writing mode** — removes all UI chrome so you can focus
- **Dark mode** — toggle between light and dark themes
- **Continuous autosave** — your writing is saved every second, automatically
- **Save folder selection** — choose where your files are stored
- **Minimal footprint** — pure Python, no external dependencies

## Screenshot

> *Screenshot coming soon*

## Installation

### Quick Start (run from source)

```bash
git clone https://github.com/Josh-writes/LiteSlate.git
cd LiteSlate
python liteslate.py
```

### Install as a Package

```bash
git clone https://github.com/Josh-writes/LiteSlate.git
cd LiteSlate
pip install -e .
liteslate
```

**Requirements:** Python 3.7+ with tkinter (included with most Python installations on Windows).

## Usage

1. Launch the app — you'll be prompted to choose a save folder on first run.
2. Toggle **Dark Mode** if you prefer writing on a dark background.
3. Click **Start Writing** to enter fullscreen mode.
4. Just write. Your work is autosaved every second.
5. Press **ESC** to end your session (you'll be asked to confirm).

## Building a Standalone .exe

```bash
pip install pyinstaller
python build.py
```

The executable will be in the `dist/` folder.

> **Note about Windows Defender:** Because the .exe is not code-signed, Windows may flag it with a SmartScreen warning. This is normal for unsigned executables. You can review the full source code in this repository to verify there is nothing malicious.

## Looking for More?

[TypeSlate](https://typeslate.com) is the premium version with additional features for serious writers.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

## License

[MIT](LICENSE) — Copyright (c) 2025 Josh-writes
