# MarkAI
AI Instruction Markup, _inspired by Markdown_ and Built for Automation

[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/natehouk/markai/blob/main/LICENSE)
[![Version](https://img.shields.io/badge/version-1.0-blue.svg)](https://github.com/natehouk/markai/releases)

## RFCs
[![RFC](https://img.shields.io/badge/RFC-MARKAI--0001-orange.svg)](https://github.com/natehouk/markai/blob/main/RFC_MARKAI-0001.txt)
[![RFC](https://img.shields.io/badge/RFC-MARKAI--0002-orange.svg)](https://github.com/natehouk/markai/blob/main/RFC_MARKAI-0002.txt)

## Description

MarkAI redefines how automated instructions are embedded in text. Drawing inspiration from the simplicity and elegance of [Markdown](https://daringfireball.net/projects/markdown/), it offers a standardized, lightweight method to direct AI processing. Its clear syntax and built-in safeguards ensure that automation workflows remain efficient and human-friendly.

## Table of Contents
- [Overview](#overview)
- [Core Format](#core-format)
- [Key Features](#key-features)
- [Usage](#usage)
- [License](#license)

## Overview

MarkAI uses XML-style tags to encapsulate processing commands alongside human-readable text and annotations. This clear separation guarantees that AI instructions are executed accurately while human commentary is preserved.

## Core Format

### 1. Basic Command
```xml
<ai_instruction>
  Format this text as JSON
</ai_instruction>
```

### 2. Command with Human Comments
```xml
<ai_instruction>
  Process the content

  <!--ai-ignore
  Internal note: This section requires special handling.
  ai-ignore-->

  Format as JSON
</ai_instruction>
```

### 3. Protected Command
```xml
<ai_instruction modify="false">
  This content is locked and cannot be modified by automated processes.
</ai_instruction>
```

## Key Features

- **Markdown-Inspired:** Clean, simple, and intuitive for both writers and machines.
- **Dual Readability:** Seamlessly blends natural language with precise, machine-executable commands.
- **Safety-First:** Designed with built-in safeguards to ensure reliable automation.
- **Flexible & Extensible:** Easily integrated into any text-based workflow, with room to evolve alongside your needs.

## Usage

Embed MarkAI commands within your text files to instruct AI-powered automation. This tag-based approach ensures that every command is processed exactly once, while human annotations offer additional context where needed. For complete details on syntax, processing rules, and integration guidelines, please refer to the full specification document provided with this release.

## License

MarkAI is distributed under the MIT License.

&copy; 2025 Nathaniel J. Houk