import logging

class Plugin:
    """
    Base class for MarkAI plugins.
    
    Plugin developers can override any of these methods:
    - pre_process: Modify the full list of instructions before processing.
    - on_instruction: Hook into each instruction before it is executed.
    - post_process: Perform actions after processing all instructions.
    """
    def pre_process(self, instructions):
        # Optionally modify and return instructions
        return instructions

    def on_instruction(self, instruction):
        # Called before each instruction is executed
        pass

    def post_process(self, instructions):
        # Called after all instructions have been processed
        pass

class PluginManager:
    def __init__(self):
        self.plugins = []
    
    def register(self, plugin: Plugin):
        self.plugins.append(plugin)
        logging.info(f"Registered plugin: {plugin.__class__.__name__}")
    
    def execute_pre_process(self, instructions):
        for plugin in self.plugins:
            try:
                instructions = plugin.pre_process(instructions) or instructions
            except Exception as e:
                logging.error(f"Error in plugin {plugin.__class__.__name__} pre_process: {e}")
        return instructions
    
    def execute_on_instruction(self, instruction):
        for plugin in self.plugins:
            try:
                plugin.on_instruction(instruction)
            except Exception as e:
                logging.error(f"Error in plugin {plugin.__class__.__name__} on_instruction: {e}")
    
    def execute_post_process(self, instructions):
        for plugin in self.plugins:
            try:
                plugin.post_process(instructions)
            except Exception as e:
                logging.error(f"Error in plugin {plugin.__class__.__name__} post_process: {e}") 