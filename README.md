# MarkAI - Intelligent Instruction Approach

[![RFC](https://img.shields.io/badge/RFC-AI--0001-blue.svg)](https://github.com/natehouk/markai/blob/main/RFC_AI-0001.txt)
[![RFC](https://img.shields.io/badge/RFC-AI--0002-blue.svg)](https://github.com/natehouk/markai/blob/main/RFC_AI-0002.txt)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/natehouk/markai/blob/main/LICENSE)
[![Version](https://img.shields.io/badge/version-1.0-blue.svg)](https://github.com/natehouk/markai/releases)  

---

## Description

MarkAI redefines how automated instructions are embedded in text. Inspired by the simplicity and elegance of [Markdown](https://daringfireball.net/projects/markdown/), MarkAI provides a standardized, lightweight method to direct AI processing. Its clear syntax and built-in safeguards ensure efficient automation while preventing unwanted recursive processing.

## Table of Contents
- [Overview](#overview)
- [Core Format](#core-format)
- [Key Features](#key-features)
- [Usage](#usage)
- [License](#license)

## Overview

MarkAI uses XML-style tags to encapsulate processing commands alongside human-friendly text and annotations. By clearly separating machine instructions from commentary, it maintains clarity and reliability in automation workflows.

## Core Format

1. **Basic Command:**
   ```xml
   <ai_instruction>
     Format this text as JSON
   </ai_instruction>
   ```

2. **Command with Human Comments:**
   ```xml
   <ai_instruction>
     Process the content

     <!--ai-ignore
     Internal note: This section requires special handling.
     ai-ignore-->

     Format as JSON
   </ai_instruction>
   ```

3. **Protected Command:**
   ```xml
   <ai_instruction modify="false">
     This content is locked and cannot be modified by automated processes.
   </ai_instruction>
   ```

## Key Features

- **Markdown-inspired:** Clean, simple, and intuitive for both writers and machines.
- **Dual Readability:** Combines natural language with precise, machine-executable commands.
- **Safety-First:** Prevents recursive processing and potential automation loops.
- **Flexible:** Easily integrated into any text-based workflow or project.
- **Extensible:** Designed to evolve with expanding AI processing needs.

## Usage

Embed MarkAI commands within your text files to instruct AI-powered automation. The tag-based approach ensures that each command is processed exactly once while human annotations provide extra context where needed.

For detailed information on syntax, processing rules, and integration guidelines, please refer to the full specification document provided with this release.

## License

MarkAI is distributed under the MIT License.

&copy; 2025 Nathaniel J. Houk