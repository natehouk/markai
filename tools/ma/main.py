import typer
import re
import logging
from pathlib import Path
from datetime import datetime
from markdown import Extension
from markdown.preprocessors import Preprocessor

# New import for core engine functions.
from core import parse_markai_file, process_instructions

app = typer.Typer()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class MarkAIPreprocessor(Preprocessor):
    """
    A Preprocessor that extracts MarkAI instructions from markdown lines.
    
    Lines starting with '@ai:' are removed from the document and parsed
    into command and attribute dictionaries.
    """
    INSTRUCTION_PATTERN = re.compile(r'^@ai:\s*(.*)$')

    def run(self, lines):
        new_lines = []
        instructions = []
        for line in lines:
            match = self.INSTRUCTION_PATTERN.match(line)
            if match:
                instruction_text = match.group(1).strip()
                command, attributes = self._parse_instruction(instruction_text)
                instructions.append({
                    "command": command,
                    "attributes": attributes
                })
            else:
                new_lines.append(line)
        # Store extracted instructions on the Markdown instance for later use.
        self.md.markai_instructions = instructions
        return new_lines

    def _parse_instruction(self, text):
        """
        Parse the instruction text into its command and attributes.
        
        Assumes the first token is the command and subsequent tokens
        may include key="value" pairs.
        """
        tokens = text.split()
        command = tokens[0] if tokens else ""
        attr_pattern = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
        attributes = {m.group(1): m.group(2) for m in attr_pattern.finditer(text)}
        return command, attributes

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

if __name__ == "__main__":
    app() 