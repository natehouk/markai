# MarkAI Extension

The MarkAI Extension is a Visual Studio Code extension designed to streamline your development workflow. It provides a customizable checkpoint command that integrates directly into your editor, enabling quick save points and additional automation.

## Features

- **Custom Checkpoint Command:** Executes the `markai.checkpoint` command, which can be extended to perform additional tasks.
- **Extensible Architecture:** Easily integrate new features or modify existing functionality.
- **Command-Based Workflow:** Quickly access the command through the Command Palette to boost productivity.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/natehouk/markai.git
    ```

2. **Open in VSCode:**
   - Launch the repository in Visual Studio Code.
3. **Navigate to the Extension Directory and Install Dependencies:**

    ```bash
    cd markai-extension
    npm install
    ```

4. **Launch the Extension:**
   - Press `F5` in VSCode to start the extension in Extension Development Host mode.

## Usage

To trigger a checkpoint:

- Open the Command Palette (Ctrl+Shift+P on Windows/Linux or Cmd+Shift+P on macOS).
- Run the command: **MarkAI: Checkpoint** (this internally calls `markai.checkpoint`).
- An information message will confirm that the checkpoint has been activated.

To extend or customize its functionality, modify the source code in `extension.js` as needed.

## Repository Structure

```
markai/
├─ markai-extension/
│  ├─ extension.js       // Main extension logic
│  ├─ package.json       // Extension metadata and configuration
│  └─ README.md          // Project overview and usage instructions (this file)
├─ .gitignore
├─ LICENSE
└─ README.md             // Root README (additional info)
```

## Contributing

Contributions are welcome! Please follow these guidelines:

- Ensure your changes adhere to the project's coding and documentation standards.
- Open an issue before submitting a pull request for significant changes.
- Include tests and documentation updates with your pull request.

## License

This project is licensed under the MIT License.

---

Thank you for using the MarkAI Extension!
