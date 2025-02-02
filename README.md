# MarkAI
*AI Instruction Markup, _inspired by Markdown_ and Built for Automation*

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