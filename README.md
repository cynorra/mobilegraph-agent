# MobileGraph-Agent 🚀

[![MobileGraph CI](https://github.com/cynorra/mobilegraph-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/cynorra/mobilegraph-agent/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Target: Flutter & Android](https://img.shields.io/badge/target-Flutter%20%7C%20Android-green.svg)](https://flutter.dev)

> **MobileGraph-Agent** is an autonomous developer CLI and maintenance engine designed for modern Flutter and Android codebases. It indexes repository architectures into an **AST Knowledge Graph (Graphify)** to reduce LLM context token consumption by up to **80%**, while enabling automated design modernization, static security scanning, and smart test generation.

---

## 🌟 Key Features

- 🧠 **AST Knowledge Graph (Graphify):** Traverses Flutter/Android directory trees, indexing classes, widgets, and dependencies into semantic graph nodes so coding agents only inspect targeted subtrees instead of full repos.
- 🎨 **2026+ Visual Modernization:** Analyzes legacy mobile UI widgets and refactors them into modern Material 3, dynamic theme-compatible, and adaptive responsive components.
- 🛡️ **Static Security & Vulnerability Auditing:** Scans `AndroidManifest.xml`, build configs, and source files for hardcoded secrets, insecure IPC exports, and sensitive storage leaks.
- 🧪 **Smart Test Weaver:** Generates mock payloads and unit/widget test boilerplates mapped directly to model dependencies.

---

## 🏛️ Architecture Overview

```text
[ Mobile Repository (Flutter / Android) ]
                    │
                    ▼
       [ AST & Dependency Extractor ]
                    │
                    ▼
   [ Lightweight Knowledge Graph (JSON/Nodes) ]
                    │
     ┌──────────────┴──────────────┐
     ▼                             ▼
[ Targeted Node Slices ]    [ Codex Security / LLM ]
 (80% Token Reduction)      (Zero Bloat Context Window)
     │                             │
     └──────────────┬──────────────┘
                    ▼
[ Autonomous Refactor & Security Audit Patch ]
