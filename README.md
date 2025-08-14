# I AM Root
> A motivational CLI program that combines quotes, breathing exercises, and system checks to help you stay focused and grounded.

![CI](https://github.com/ramangupta/I-AM-Root/actions/workflows/ci.yml/badge.svg)

<!--
   ┌───────────────────────────────────────────────────────────┐
   │  I AM ROOT — because sometimes you don’t just grow,       │
   │  you take control.                                        │
   └───────────────────────────────────────────────────────────┘
-->

<p align="center">
  <pre>
   ██╗ █████╗ ███╗   ███╗      ██████╗  ██████╗  ██████╗  ██████╗ ████████╗
   ██║██╔══██╗████╗ ████║      ██╔══██╗██╔═══██╗██╔════╝ ██╔═══██╗╚══██╔══╝
   ██║███████║██╔████╔██║█████╗██████╔╝██║   ██║██║  ███╗██║   ██║   ██║
██  ██║██╔══██║██║╚██╔╝██║╚════╝██╔══██╗██║   ██║██║   ██║██║   ██║   ██║
╚█████╔╝██║  ██║██║ ╚═╝ ██║      ██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝   ██║
 ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝      ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝    ╚═╝
  </pre>
  <em>“Access is responsibility. Mastery is freedom.”</em>
</p>

[![Sponsor via GitHub](https://img.shields.io/badge/Sponsor-GitHub-blue)](https://github.com/sponsors/ramangupta)
[![Sponsor via Ko-fi](https://img.shields.io/badge/Sponsor-Ko--fi-orange)](https://ko-fi.com/ramangupta)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-yellow)](https://github.com/ramangupta/I-AM-Root)

<p align="center">
  <a href="#-about">About</a> •
  <a href="#-features">Features</a> •
  <a href="#-quickstart">Quickstart</a> •
  <a href="#-project-structure">Structure</a> •
  <a href="#-roadmap">Roadmap</a> •
  <a href="#-contributing">Contributing</a>
</p>

<p align="center">
  <img alt="status" src="https://img.shields.io/badge/status-in%20progress-222"/>
  <img alt="license" src="https://img.shields.io/badge/license-MIT-222"/>
  <img alt="built-with" src="https://img.shields.io/badge/built%20by-Raman%20Gupta-222"/>
</p>

---

## 🧠 About
**I AM Root** is a living toolkit for builders who like to pop the hood:
automation, security-minded scripts, and high-performance experiments that
give you root-level clarity over your stack.

> Not just code—an operating philosophy.

---

## ⚡ Features
- 🛠️ **Automation Primitives:** shell & Python utilities that save keystrokes.
- 🔐 **Security-First Defaults:** safe configs, least-privilege patterns.
- 🚀 **Performance Experiments:** benchmarks, profiling recipes.
- 🧩 **Modular Design:** drop in only what you need.
- 💡 **CLI Modes:** `--quote`, `--breathe`, `--syscheck`, `--help`
- 🧪 **Automated Test Suite:** run `make test` for full verification

---

## 🚀 Quickstart
```bash
# 1) Clone the repository
git clone https://github.com/ramangupta/I-AM-Root.git
cd I-AM-Root

# 2) (Optional) Create a Python virtualenv if needed
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3) Build the CLI project
make

# 4) Run a sample utility
./bin/iamroot --help        # Shows all available options
./bin/iamroot --quote       # Display a random quote
./bin/iamroot --breathe     # Guided breathing exercise
./bin/iamroot --syscheck    # System health check
./bin/iamroot               # Interactive mode

# 5) Run automated tests
make test

## 📂 Project Structure
I-AM-Root/
├── src/ # Core source (tools, libs, experiments)
│ ├── tools/ # CLI utilities & scripts
│ └── core/ # Reusable modules
├── scripts/ # Dev/ops scripts (bootstrap, setup, lint, etc.)
├── docs/ # Notes, design, research
├── tests/ # Unit/integration tests
├── .gitignore
└── README.md

## 🖥️ Demo
```text
$ ./bin/iamroot
Welcome to I AM Root interactive mode.
Choose an option:
1. Show a quote
2. Start breathing exercise
3. Run system check
q. Quit
> 1
"Access is responsibility. Mastery is freedom."

> 2
Breathe In... 3 2 1
Hold... 3 2 1
Exhale... 3 2 1
Repeat 3 cycles

> q
Goodbye!

