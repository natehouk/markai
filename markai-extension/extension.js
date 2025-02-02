'use strict';

const vscode = require('vscode');

/**
 * Activates the Markai extension.
 *
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
    const commandId = 'markai.runCheckpointCommand';
    const disposable = vscode.commands.registerCommand(commandId, () => {
        // Integrate the MarkAI "checkpoint" command functionality
        vscode.window.showInformationMessage('MarkAI Checkpoint Command triggered!');
        
        // Example: Execute a terminal command if needed
        // const terminal = vscode.window.createTerminal('MarkAI Checkpoint');
        // terminal.sendText('git add . && git commit -m "refactor(all): 🤖💫 Automated MarkAI magic at work"');
        // terminal.show();
    });

    context.subscriptions.push(disposable);
}

/**
 * Deactivates the Markai extension.
 */
function deactivate() {}

module.exports = {
    activate,
    deactivate
}; 