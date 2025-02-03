# MarkAI Project

**MarkAI** is a tool and a set of specifications for embedding AI instructions within Markdown documents to enable automated workflows across development tools.

## Overview

MarkAI leverages lightweight AI directives embedded in Markdown to enable:
- Automated synchronization of repository data.
- Secure and immutable command definitions.
- Preemptive execution of critical commands.
- Integration with both a VSCode extension and CLI tools.

This repository includes:
- **Specification Files:**
  - [MarkAI v1.0 Specification](./MARKAI_V1.0.md)
  - [MarkAI v1.1 Specification](./MARKAI_V1.1.md)
- **VSCode Extension:**  
  Located in the `markai-extension/` directory, it provides interactive command execution and checkpointing.
- **CLI Tools & Reference Implementation:**  
  Found under `tools/ma/`, including the core engine, plugin management, and tests.

## Features

- **AI Instructions:** Embed commands using the `@ai:` tag to automate workflows.
- **Immutable Commands:** Ensure consistency with immutable and secure command configurations.
- **Remote Execution:** Leverage built-in remote API support (introduced in v1.1) for external command processing.
- **Extensibility:** Customize processing via a plugin architecture.

## Repository Structure

# MarkAI

*AI Instruction Markup, Inspired by [Markdown](https://daringfireball.net/projects/markdown/) and Built for Automation*

![License](https://img.shields.io/badge/license-MIT-green.svg) ![Version](https://img.shields.io/badge/version-1.0-blue.svg)

## 🚀 What is MarkAI?

MarkAI is a **lightweight AI instruction language** that seamlessly embeds **machine-executable commands** inside Markdown-like documents. Inspired by [Markdown](https://daringfireball.net/projects/markdown/), it allows AI-powered automation while preserving human readability.

> **"Think of it as Markdown for AI, where your documents become actionable."**

### ✨ **Key Features**

- **🚀 Markdown-Friendly:** AI instructions (`@ai:`) coexist with normal text.
- **🤖 AI-Powered Automation:** Embed commands directly inside documents.
- **🔒 Secure & Immutable:** Use `locked="true"` to protect commands from modification.
- **⚡ Preemptive Execution:** Prioritize critical instructions with `preempt="true"`.
- **🔄 Auto-Syncing:** Keep automation workflows up-to-date effortlessly.

---

## ��️ Getting Started

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/natehouk/markai.git
    ```

2. **Install Dependencies:**
    - **For the CLI Tool (using Poetry):**
      ```bash
      cd tools/ma
      poetry install
      ```
    - **For the VSCode Extension:**
      Open the `markai-extension` folder in VSCode and run:
      ```bash
      npm install
      ```

3. **Usage:**
    - **Command-Line Tool:**  
      Execute the CLI via:
      ```bash
      poetry run ma [command]
      ```
    - **VSCode Extension:**  
      Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P) and select **MarkAI: Checkpoint**.

## Contributing

Contributions are welcome! Please adhere to the following guidelines:
- Follow the project's coding and documentation standards.
- For major changes, open an issue before submitting a pull request.
- Include necessary tests and documentation updates with your contributions.

## License

This project is licensed under the [MIT License](./LICENSE).

---

**© 2025 Nathaniel J. Houk**
