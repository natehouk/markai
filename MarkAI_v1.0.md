# MarkAI v1.0 Specification

*AI Instruction Markup, Inspired by Markdown and Built for Automation*

**Version:** 1.0\
**Date:** March 2025\
**License:** MIT

---

## **1. Introduction**

MarkAI is a lightweight, structured language for embedding AI instructions into text files. Inspired by Markdown, MarkAI provides a standardized syntax for instructing AI-powered automation while maintaining human readability.

**MarkAI is a strict extension of Markdown.** Traditional Markdown renderers must **ignore** `@ai:` tags, ensuring that MarkAI-enhanced documents remain **fully readable** in non-AI environments.

MarkAI v1.0 introduces:

- **The `@ai:` tag format**.
- **Mandatory leading slashes for commands** (e.g., `@ai: /sync`).
- **Immutable commands** using `locked="true"` (when defined in a block).
- **Preemptive execution of high-priority commands** with `preempt="true"` (when defined in a block).
- **Auto-synchronization and structured logging** for AI-enhanced automation workflows.

This specification formalizes these features and serves as the **definitive reference** for all MarkAI-compatible implementations.

## **2. Core Syntax**

MarkAI instructions follow a **structured tagging system** using `@ai:` directives.

### **2.1. Basic Instruction**

```plaintext
@ai: /sync
```

Executes the `/sync` command.

### **2.2. Instruction with Human-Readable Comment**

```plaintext
@ai: /format_json

<!--ai-ignore
  This section requires special handling.
ai-ignore-->
```

The AI will execute `/format_json` but ignore the annotation.

### **2.3. Protected Commands (Immutable)**

For simple invocation without configuration, use the slash command without attributes:

```plaintext
@ai: /update_model
```

*Note:* To mark a command as immutable (e.g., using `locked="true"`), you **must** define it in a block:
  
```plaintext
@ai:define /update_model locked="true"
{
  // Command configuration goes here.
}
@ai:end
```

This instruction **cannot be modified** by automated processes once defined.

### **2.4. Including External Instructions**

```plaintext
@ai: include=".markairules.ma"
```

This allows the system to reference and execute AI instructions from another file.  
*Note: Rule files must use the `.ma` extension. Ensure your rules file is named accordingly (for example, `.markairules.ma`) so it is correctly recognized and processed.*

### **2.5. Preemptive Execution**

To trigger preemptive execution without specifying attributes, you can use:

```plaintext
@ai: /consciousness
```

*Note:* To ensure a command executes before all others by setting `preempt="true"`, define it using a block:

```plaintext
@ai:define /consciousness preempt="true"
{
  // Command configuration for preemptive execution.
}
@ai:end
```

Commands defined with preemptive attributes execute before others.

### **2.6. Structured Data Instructions**

MarkAI supports embedding structured JSON data to pass configuration and command data to the AI. This enables richer interactions by combining Markdown content with machine-parseable AI instructions.

- **Setup Configuration (`@ai:setup`)**  
  Begins a structured setup block with JSON data. This block **must be closed** with `@ai:end`.

  _Example:_
  ```plaintext
  @ai:setup
  {
    "version": "1.0",
    "description": "This document uses the MarkAI standard to combine Markdown content with embedded AI instructions."
  }
  @ai:end
  ```

- **Command Instructions (`@ai:command`)**  
  Embeds a structured command in JSON format. Use this to define tasks and include parameters.

  _Example:_
  ```plaintext
  @ai:command
  {
    "task": "create_blog_post",
    "topic": "The Importance of Open Standards in Technology",
    "requirements": {
      "structure": [
        "Introduction",
        "Main Discussion",
        "Conclusion"
      ],
      "format": "Markdown",
      "tone": "professional and engaging",
      "include": [
        "at least one code block example",
        "a bullet list summarizing key points"
      ]
    }
  }
  @ai:end
  ```

- **Block Termination (`@ai:end`)**  
  Every structured data block must be terminated with `@ai:end`.

Make sure that all structured data blocks adhere to valid JSON formatting.

### **2.7. Invocation vs. Definition**

- **Slash Commands:**  
  Commands initiated with `@ai: /command` are used to trigger the execution of a pre-defined command. They serve as a call to action and are typically simple, self-contained triggers.

  _Example:_
  ```plaintext
  @ai: /sync
  ```

- **Define Blocks:**  
  Commands defined using `@ai:define /command` ... `@ai:end` are used to specify the logic, configuration, or details of a command. This is where you provide a complete definition that can later be triggered by its corresponding slash command.

  _Example:_
  ```plaintext
  @ai:define /sync locked="false" auto="true"
  {
    "action": "synchronize repository data",
    "destination": ".markai/LAST_SYNC.txt"
  }
  @ai:end
  ```

This separation ensures that the mechanism for invoking a command is distinct from the detailed definition of the command, promoting clarity and maintainability.

**Note:** ALL commands MUST be defined using a define block (i.e., with `@ai:define` ... `@ai:end`). Any command that is invoked using a simple slash command without a corresponding definition will be discarded.

## **3. Processing Rules**

1. **Command Execution:**
   - Each instruction **must start with a** `/` (e.g., `@ai: /sync`).
   - Instructions are **executed in order**, except those marked with `preempt="true"`, which run first.

2. **Immutable Instructions:**
   - Any command defined with `locked="true"` **cannot be modified**.
   - Instructions with `security="ring0"` **cannot be unlocked**.

3. **Auto-Synchronization (`/sync`):**
   - Sync operations are logged in `.markai/LAST_SYNC.txt`.
   - **Minimum interval between syncs:** 5 minutes.
   - If `auto="true"` is present, sync runs automatically.

4. **Human-Readable Comments:**
   - Annotations enclosed in `<!--ai-ignore ... ai-ignore-->` are ignored by AI processing.

5. **File Inclusion:**
   - External rule files can be loaded using `@ai: include="filename"`.
   - *Note: As with all rule files, the referenced file must end with the `.ma` extension.*

## **4. Security & Compliance**

| **Attribute**      | **Effect**                                               |
| ------------------ | -------------------------------------------------------- |
| `locked="true"`    | The instruction **cannot be modified**.                  |
| `security="ring0"` | The instruction is **immutable and cannot be unlocked**. |
| `preempt="true"`   | This command executes **before all others**.             |
| `auto="true"`      | Enables **auto-synchronization** for `/sync` commands.   |

Security is further reinforced by:

- **Audit logging** in `.markai/ERRORS.txt`.
- **Strict validation of syntax and execution order.**

## **5. Versioning & Future Updates**

MarkAI follows **Semantic Versioning (SemVer)**:

- **Patch updates (1.0.x):** Bug fixes and refinements.
- **Minor updates (1.x.0):** New features, maintaining backwards compatibility.
- **Major updates (x.0.0):** Breaking changes, significant enhancements.

## **6. Tooling & Ecosystem**

MarkAI is designed for integration with **AI-enhanced editors, GitHub automation, and CI/CD pipelines**. Future enhancements include:

- **CLI tools** for validating `.ma` files.
- **GitHub support** for syntax highlighting.
- **AI-enhanced IDE plugins** for real-time processing.

## **7. Best Practices for Writing MarkAI Documents**

- **Use comments** (`<!--ai-ignore ... ai-ignore-->`) to explain AI commands.
- **Keep AI instructions at the top** of the file for clarity.
- **Use `preempt="true"` sparingly**, only for critical commands.
- **Avoid excessive `locked="true"` usage**, unless immutability is necessary.

## **8. Conclusion**

MarkAI **revolutionizes AI-powered automation** by providing a **human-friendly, machine-readable format**. By adopting **@ai:** directives, structured execution, and strong security controls, MarkAI ensures that AI instructions remain clear, safe, and efficient.

MarkAI v1.0 is now the **official standard** for AI automation workflows.

---

### **References**

- **MarkAI v1.0 Specification:** [GitHub Repository](https://github.com/natehouk/markai)
- **License:** MIT License (© 2025 Nathaniel J. Houk)
