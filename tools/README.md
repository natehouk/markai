# MarkAI Reference Implementation

This folder contains the reference implementation for the [MarkAI v1.0 Specification](../MarkAI_v1.0.md). The implementation is designed to process and execute AI instructions embedded in MarkAI-enhanced Markdown files. It serves as both a demonstration and a baseline for further integrations.

## Overview

MarkAI is a lightweight extension to Markdown that introduces a standardized syntax for AI automation. The reference implementation covers the following key features:

- **Structured AI directives:** Instructions begin with `@ai:`, followed by commands (e.g., `/sync`, `/format_json`).
- **Immutable commands:** Commands marked with `locked="true"` cannot be modified.
- **Preemptive execution:** Commands with `preempt="true"` are executed before all other instructions.
- **File inclusion:** External rule files (ending with `.ma`) can be included to extend functionality.
- **Human-readable comments:** Sections surrounded by `<!--ai-ignore ... ai-ignore-->` are ignored during AI processing.

## Components

- **Command Processor:**  
  An engine that identifies, parses, and executes MarkAI directives based on the order of appearance and priority flags.

- **Auto-Synchronization:**  
  A mechanism to execute `/sync` commands at a minimum interval (e.g., every 5 minutes) and log sync data in `.markai/LAST_SYNC.txt`.

- **Security & Compliance:**  
  Immutable commands (e.g., those flagged with `locked="true"` or `security="ring0"`) are enforced by the system, ensuring that they remain unchanged during automated updates.
  
- **Error Logging:**  
  Audit events and potential issues are logged into `.markai/ERRORS.txt` for debugging and compliance purposes.

## Getting Started

1. **MarkAI Files:**  
   Ensure that your MarkAI-enhanced documents include the `@ai:` directives as specified in the [MarkAI v1.0 Specification](../MarkAI_v1.0.md).

2. **Rule Files:**  
   External rule files can be referenced using:
   ```plaintext
   @ai: include=".markairules.ma"
   ```
   For a successful inclusion, make sure your file follows the `.ma` naming convention.

3. **Execution Order:**  
   - **Standard Commands:** Processed in the order they appear.  
   - **Preemptive Commands:** Identified with `preempt="true"` and executed prior to standard commands.

4. **Command Examples:**

   - **Synchronize:**
     ```plaintext
     @ai: /sync auto="true"
     ```
   - **Immutable Update:**
     ```plaintext
     @ai: /update_model locked="true"
     ```
   - **Command with a human-readable comment:**
     ```plaintext
     @ai: /format_json
     
     <!--ai-ignore
       Special formatting is applied here.
     ai-ignore-->
     ```

## How It Works

- **Parsing:**  
  The implementation scans input files for directives starting with `@ai:` and categorizes commands according to their specified attributes.

- **Execution:**  
  Commands marked with `preempt="true"` are executed first, followed by the remaining commands in sequential order. Immutable commands are enforced to prevent unauthorized modifications.

- **Logging & Sync:**  
  Logging mechanisms track each `/sync` operation. The logs are useful for audit trails and ensuring that commands are processed following the minimum interval restrictions.

## Contributing

This reference implementation is a starting point for integrating MarkAI into more sophisticated systems. Contributions in tooling, error handling, and expanded directive support are welcome. Please refer to the [MarkAI v1.0 Specification](../MarkAI_v1.0.md) for detailed operational guidelines.

## License

The reference implementation is licensed under the MIT License. See the [MarkAI v1.0 Specification](../MarkAI_v1.0.md) for licensing details.
