import pytest
from pathlib import Path
import tempfile

# Test the preprocessor
from markdown import Markdown
from tools.ma.main import MarkAIPreprocessor
import typer.testing

def test_preprocessor_extracts_instructions():
    # Create a dummy Markdown instance for testing
    class DummyMD:
        pass

    md = DummyMD()
    # Instantiate the preprocessor with our dummy md
    preprocessor = MarkAIPreprocessor(md)
    
    # Sample input lines containing some text and @ai: directives
    lines = [
        "This is some text.",
        "@ai: /sync auto=\"true\"",
        "Some more text.",
        "@ai: /update_model locked=\"true\""
    ]
    
    # Run the preprocessor, which should remove the @ai: lines
    new_lines = preprocessor.run(lines)
    
    # Check that non-directive lines remain
    assert "This is some text." in new_lines
    assert "Some more text." in new_lines
    
    # The instructions should have been extracted from the @ai: directives
    assert hasattr(md, "markai_instructions")
    assert len(md.markai_instructions) == 2

    # Verify the first instruction
    instr1 = md.markai_instructions[0]
    assert instr1["command"] == "/sync"
    assert instr1["attributes"]["auto"] == "true"

# Test for the CLI version command using Typer's CliRunner.
def test_cli_version():
    from tools.ma.main import app
    runner = typer.testing.CliRunner()
    result = runner.invoke(app, ["version"])
    assert "MarkAI Reference Implementation v1.0" in result.output

# Test parsing a MarkAI file using a temporary file.
def test_parse_markai_file(tmp_path: Path):
    # Create a temporary file with sample MarkAI instructions and plain text.
    test_file = tmp_path / "test.ma"
    test_file.write_text("@ai: /sync auto=\"true\"\nJust some text\n@ai: /update_model locked=\"true\"\n")
    
    # Import and use the core parse function.
    from tools.ma.core import parse_markai_file
    instructions = parse_markai_file(test_file)
    
    # Expect two instructions extracted from the file.
    assert len(instructions) == 2
    # Verify each instruction's basic structure.
    assert instructions[0]["command"] == "/sync"
    assert instructions[1]["command"] == "/update_model" 