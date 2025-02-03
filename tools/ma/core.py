import re
import logging
from pathlib import Path
from datetime import datetime
from plugins import PluginManager

plugin_manager = PluginManager()  # Global instance for plugin management

def parse_instruction_line(line: str):
    """
    Parse a line starting with '@ai:' into a command and its attributes.
    
    Returns:
        A dictionary with "command" and "attributes", or None if the line does not
        contain a valid MarkAI instruction.
    """
    if not line.strip().startswith("@ai:"):
        return None
    content = line.strip()[4:].strip()  # Remove the '@ai:' prefix
    if not content:
        return None

    # The first token (which may start with a slash) is the command.
    tokens = content.split()
    command = tokens[0]

    # Use regex to extract key="value" attribute pairs.
    attr_pattern = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
    attributes = {match.group(1): match.group(2) for match in attr_pattern.finditer(content)}
    
    return {"command": command, "attributes": attributes}

def parse_markai_file(file_path: Path):
    """
    Parse a MarkAI-enhanced file and return a list of instructions.
    """
    instructions = []
    try:
        with file_path.open("r", encoding="utf-8") as f:
            for line in f:
                instr = parse_instruction_line(line)
                if instr:
                    instructions.append(instr)
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
    return instructions

def execute_instruction(instr: dict):
    """
    Execute a single MarkAI instruction based on the provided command and attributes.
    """
    command = instr.get("command", "")
    attributes = instr.get("attributes", {})
    logging.info(f"Executing command '{command}' with attributes {attributes}")

    if command == "/sync":
        # Write the current timestamp to .markai/LAST_SYNC.txt
        last_sync_dir = Path(".markai")
        last_sync_dir.mkdir(exist_ok=True)
        last_sync_file = last_sync_dir / "LAST_SYNC.txt"
        timestamp = datetime.now().isoformat()
        last_sync_file.write_text(f"Last sync: {timestamp}\n", encoding="utf-8")
        logging.info(f"Sync performed at {timestamp}")
    elif command == "/update_model":
        if attributes.get("locked") == "true":
            logging.info("Executing locked update model command (immutable).")
        else:
            logging.info("Updating model.")
    elif command == "/format_json":
        logging.info("Formatting JSON as per instruction.")
    elif command == "/consciousness":
        logging.info("Executing preemptive consciousness command.")
    elif command == "include":
        included_file = attributes.get("include", "")
        logging.info(f"Including external file: {included_file}")
        # Here you might process the included file.
    else:
        logging.info(f"Unrecognized command '{command}'. No action taken.")

def process_instructions(instructions: list):
    """
    Process a list of instructions, ensuring that preemptive commands execute first,
    and allowing plugin hooks to run before, during, and after instruction processing.
    """
    # Execute pre-processing hooks to allow plugins to modify the instructions.
    instructions = plugin_manager.execute_pre_process(instructions)

    # Separate preempt and normal instructions.
    preempt_instructions = [instr for instr in instructions if instr.get("attributes", {}).get("preempt") == "true"]
    normal_instructions = [instr for instr in instructions if instr.get("attributes", {}).get("preempt") != "true"]

    for instr in preempt_instructions:
        # Allow plugins to hook into each instruction.
        plugin_manager.execute_on_instruction(instr)
        try:
            execute_instruction(instr)
        except Exception as e:
            logging.error(f"Error executing preempt command {instr.get('command')}: {e}")

    for instr in normal_instructions:
        plugin_manager.execute_on_instruction(instr)
        try:
            execute_instruction(instr)
        except Exception as e:
            logging.error(f"Error executing command {instr.get('command')}: {e}")

    # Execute post-processing hooks after instructions are processed.
    plugin_manager.execute_post_process(instructions) 