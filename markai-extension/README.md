MarkAI Extension
================

The MarkAI Extension is a VSCode extension designed to streamline your workflow by providing a custom save command integrated directly into your development environment.

Features:
---------
- **Custom Save Command:** Triggers a custom save action (`markai.runSaveCommand`) that can be extended for additional functionalities.
- **Extendable Architecture:** Serves as a foundation for further integration and automation within your development process.
- **Command-based Workflow:** Easily invoked from the command palette to enhance productivity.

Installation:
-------------
1. Clone or download the repository.
2. Open the repository in VSCode.
3. Install any required dependencies.
4. Launch the extension using VSCode's debugging tools.

Usage:
------
- Open the command palette (Ctrl+Shift+P / Cmd+Shift+P) and run the "Run Save Command" command.
- The extension will trigger an information message indicating that the save command has been activated.
- Customize or extend the functionality by editing the source code in `cursor-extension/extension.js`.

Contributing:
-------------
- We welcome contributions to improve and extend this extension.
- Please follow the project's coding and documentation guidelines.
- Submit pull requests with appropriate tests and documentation updates.

License:
--------
This project is licensed under the MIT License.

Repository Structure:
---------------------
markai/
├─ cursor-extension/
│  ├─ extension.js       // Main extension logic
│  └─ package.json       // Extension metadata and configuration
└─ README.txt             // Project overview and usage instructions

Thank you for using the MarkAI Extension!