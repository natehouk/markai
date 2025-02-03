import typer
import re
import logging
import sys  # <-- Added for detecting command-line arguments.
from pathlib import Path
from datetime import datetime
from markdown import Extension
from markdown.preprocessors import Preprocessor

# New import for core engine functions.
from ma.core import parse_markai_file, process_instructions

app = typer.Typer()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class InstructionNode:
    def __init__(self, command, attributes):
        self.command = command
        self.attributes = attributes

    def __repr__(self):
        return f"InstructionNode(command={self.command}, attributes={self.attributes})"

class AttributeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"AttributeNode(key={self.key}, value={self.value})"

class MarkAIPreprocessor(Preprocessor):
    """
    A Preprocessor that extracts MarkAI instructions from markdown lines.
    
    Instructions start with '@ai:' and end with '@endai'.
    """
    INSTRUCTION_START_PATTERN = re.compile(r'^@ai:\s*(.*)$')
    INSTRUCTION_END_PATTERN = re.compile(r'^@endai\s*$')

    def run(self, lines):
        new_lines = []
        instructions = []
        in_instruction_block = False
        instruction_text = []

        for line in lines:
            if self.INSTRUCTION_START_PATTERN.match(line):
                in_instruction_block = True
                instruction_text.append(line)
            elif self.INSTRUCTION_END_PATTERN.match(line):
                if in_instruction_block:
                    instruction_text.append(line)
                    node = self._parse_instruction(instruction_text)
                    if node:
                        instructions.append(node)
                    in_instruction_block = False
                    instruction_text = []
            elif in_instruction_block:
                instruction_text.append(line)
            else:
                new_lines.append(line)

        # Store extracted instructions on the Markdown instance for later use.
        self.md.markai_instructions = instructions
        return new_lines

    def _parse_instruction(self, lines):
        """
        Parse the instruction text into an AST node.
        
        Assumes the first token is the command and subsequent tokens
        may include key="value" pairs.
        """
        full_text = " ".join(lines)
        tokens = full_text.split()
        if len(tokens) < 2:
            logging.error("Malformed instruction: Missing command.")
            return None

        command = tokens[1]
        attr_pattern = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
        attributes = [AttributeNode(m.group(1), m.group(2)) for m in attr_pattern.finditer(full_text)]
        return InstructionNode(command, attributes)

class MarkAIExtension(Extension):
    """
    A Python-Markdown extension to process MarkAI instructions.
    
    This extension scans the document for lines starting with '@ai:' 
    and extracts them into structured instructions before rendering.
    """
    def extendMarkdown(self, md):
        md.registerExtension(self)
        preprocessor = MarkAIPreprocessor(md)
        # Register the preprocessor at a priority that runs early.
        md.preprocessors.register(preprocessor, "markai_preprocessor", 27)

def makeExtension(**kwargs):
    return MarkAIExtension(**kwargs)

# NOTE: Removed core functions (parse_instruction_line, parse_markai_file, 
# execute_instruction, process_instructions) since these have been moved to tools/ma/core.py.

@app.command()
def process(file: Path = typer.Argument(..., exists=True, readable=True, help="Path to the MarkAI file to process")):
    """
    Process a MarkAI-enhanced Markdown file.
    """
    logging.info(f"Processing file: {file}")
    instructions = parse_markai_file(file)
    logging.info(f"Found {len(instructions)} MarkAI instructions.")
    process_instructions(instructions)

@app.command()
def version():
    """
    Display the version of the MarkAI tool.
    """
    typer.echo("MarkAI Reference Implementation v1.0")

# -------------------------------------------------------------------
# New: Interactive Prompt Mode Implementation
# -------------------------------------------------------------------
def interactive_prompt():
    """
    Interactive prompt mode for MarkAI.
    Type 'help' for available commands or 'exit' to quit.
    """
    print("Entering MarkAI prompt mode. Type 'help' for commands, or 'exit' to quit.")
    while True:
        try:
            command_input = input("ma> ").strip()
            if command_input.lower() in ("exit", "quit"):
                print("Exiting prompt mode.")
                break
            elif command_input.lower() == "help":
                print("Available commands: /sync, /update_model, /format_json, /consciousness, help, exit")
                continue
            elif command_input == "":
                continue
            else:
                # Construct a simple instruction dictionary from the input.
                instruction = {"command": command_input, "attributes": {}}
                # Execute the instruction via the core processing engine.
                process_instructions([instruction])
        except (KeyboardInterrupt, EOFError):
            print("\nExiting prompt mode.")
            break

# -------------------------------------------------------------------
# Modified main execution block: Enter interactive prompt mode if no arguments
# -------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_prompt()
    else:
        app() 