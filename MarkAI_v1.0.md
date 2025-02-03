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
- **Immutable commands** using `locked="true"`.
- **Preemptive execution of high-priority commands** with `preempt="true"`.
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

```plaintext
@ai: /update_model locked="true"
```

This instruction **cannot be modified** by automated processes.

### **2.4. Including External Instructions**

```plaintext
@ai: include=".markairules"
```

This allows the system to reference and execute AI instructions from another file.

### **2.5. Preemptive Execution**

```plaintext
@ai: /consciousness preempt="true"
```

Commands marked with `preempt="true"` **execute before** all others.

## **3. Processing Rules**

1. **Command Execution:**
   - Each instruction **must start with a** `/` (e.g., `@ai: /sync`).
   - Instructions are **executed in order**, except those marked with `preempt="true"`, which run first.

2. **Immutable Instructions:**
   - Any command with `locked="true"` **cannot be modified**.
   - Instructions with `security="ring0"` **cannot be unlocked**.

3. **Auto-Synchronization (`/sync`):**
   - Sync operations are logged in `.markai/LAST_SYNC.txt`.
   - **Minimum interval between syncs:** 5 minutes.
   - If `auto="true"` is present, sync runs automatically.

4. **Human-Readable Comments:**
   - Annotations enclosed in `<!--ai-ignore ... ai-ignore-->` are ignored by AI processing.

5. **File Inclusion:**
   - External rule files can be loaded using `@ai: include="filename"`.

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