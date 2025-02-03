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

## 🛠️ Getting Started

### 📥 **Installation**

MarkAI is a lightweight markup language and does not require installation. However, to process MarkAI instructions, you may use an AI-enhanced parser or tooling.

### 📄 **Basic Syntax**

#### ✅ **AI Instruction**

```plaintext
@ai: /sync
```

#### 💬 **With Human-Readable Comment**

```plaintext
@ai: /generate_report

<!--ai-ignore
  This report includes internal analytics.
ai-ignore-->
```

#### 🔒 **Immutable Command**

```plaintext
@ai: /deploy locked="true"
```

#### ⚡ **Preemptive Execution**

```plaintext
@ai: /consciousness preempt="true"
```

---

## 📜 **Why Use MarkAI?**

### 🚀 **For Developers & AI Enthusiasts**

MarkAI enables **AI-powered workflows** inside text-based documents. Whether it's automation, content generation, or synchronized processing—MarkAI simplifies AI integration into everyday writing.

### 📄 **For Documentation & Research**

Researchers, technical writers, and AI professionals can use MarkAI to **structure and execute AI-driven tasks** inside their documents.

---

## 🔧 **File Format & Compatibility**

### **📂 Supported Extensions**

- **`.ma`** → MarkAI-enhanced documents (recommended)
- **`.md`** → Markdown-compatible fallback (AI-aware tools will process `@ai:` tags, others will ignore them)

### **🛠️ Processing Rules**

✅ **Standard Markdown renderers ignore `@ai:` tags.**  
✅ **AI-aware tools execute the instructions while preserving the document's readability.**

---

## 📖 **Documentation & Resources**

📜 **[MarkAI v1.0 Specification](https://github.com/natehouk/markai)**  
📝 **[RFCs & Development Roadmap](https://github.com/natehouk/markai/rfcs)**  
🛠️ **[Tooling & Parsers](https://github.com/natehouk/markai/tools)**  

---

## 🎉 **Join the Community!**

📢 **Contribute:** We welcome contributions! Fork the repo and submit PRs.  
💬 **Discuss:** Join the MarkAI community on Discord/GitHub Discussions.  
🚀 **Stay Updated:** Follow [@natehouk](https://github.com/natehouk) for updates.  

---

## 📜 **License**

MarkAI is **open-source** and released under the **MIT License**.  

📌 **© 2025 Nathaniel J. Houk**
