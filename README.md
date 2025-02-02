# 🤖 AI Instruction Tag Format (RFC_AI-0001)
[![RFC](https://img.shields.io/badge/RFC-AI--0001-blue.svg)](https://github.com/natehouk/RFC_AI-0001-ai-instruction-tag/blob/main/RFC_AI-0001.txt)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/natehouk/RFC_AI-0001-ai-instruction-tag/blob/main/LICENSE)

A standardized format for embedding AI instructions in text files using simple tag notation.

## 📖 Overview

The AI Instruction Tag Format (RFC_AI-0001) defines a standard method for embedding AI processing instructions within text files. The format uses XML-style tags for instructions and HTML-style comments for human annotations. It solves the halting problem in AI instruction processing by creating explicit boundaries between processable instructions and human meta-commentary.

## 🎯 Core Format

### Basic Instruction
```xml
<ai_instruction>
Format this text as JSON
</ai_instruction>
```

### With Human Comments
```xml
<ai_instruction>
Process this content

<!--ai-ignore
Internal note: This section requires special handling
ai-ignore-->

Format as JSON
</ai_instruction>
```

### Protected Content
```xml
<ai_instruction modify="false">
This content cannot be modified by AI processing
</ai_instruction>
```

## ✨ Key Features

- 📜 **RFC Standard**: Follows RFC_AI-0001 specification
- 🎨 **Simple & Standard**: Clear, intuitive tag notation
- 🔄 **Halting Problem Solution**: Prevents recursive processing loops
- 👥 **Human-Readable**: Built-in support for human comments
- 🤖 **Machine-Processable**: Directly parseable by AI systems
- 🛡️ **Safe Processing**: Protection against recursive processing
- 🔧 **Flexible**: Works with any text-based content

## 📚 Specification

For complete technical details, see [RFC_AI-0001](https://github.com/natehouk/RFC_AI-0001-ai-instruction-tag/blob/main/RFC_AI-0001.txt).

## 📄 License

Copyright (C) 2025 Nathaniel J. Houk  
Licensed under MIT License. See [LICENSE](https://github.com/natehouk/RFC_AI-0001-ai-instruction-tag/blob/main/LICENSE) for details.