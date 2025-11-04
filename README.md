# ShellMate — Your Gemini-Powered Smart Terminal Assistant

ShellMate is an intelligent command-line assistant that helps you convert natural language into shell commands, explain commands, and even execute them safely — all powered by Google’s Gemini API.  
It’s designed to make the terminal more intuitive, especially for beginners and power users who want productivity with context awareness.

## Features

- **Natural Language → Bash Command Conversion**  
  Type what you want to do in plain English, and ShellMate will generate the correct shell command for you.

  Example:
  ```bash
  shellmate gen "list all Python files in the current folder"
  ```

- **Command Explanation**  
  Unsure what a command does? Ask ShellMate to explain it:
  ```bash
  shellmate explain "sudo apt-get update"
  ```

- **Interactive REPL Mode**  
  Use the built-in REPL for a chat-like experience:
  ```bash
  shellmate repl
  ```
  You can generate, explain, and optionally execute commands in a loop.

- **Dry Run / Execute Mode**  
  Preview generated commands safely before executing:
  ```bash
  shellmate gen "delete temporary files" --dry   # Default dry run
  shellmate gen "delete temporary files" --no-dry   # Execute directly
  ```

- **Rich Command Output**  
  ShellMate uses [Rich](https://github.com/Textualize/rich) for colorful, structured panels and formatted terminal output.

- **Activity Logging**  
  Every interaction is stored in a `log.json` file for auditing or review later.  
  Logs include:
  - Instruction  
  - Generated Command  
  - Metadata (explanation, risk level, etc.)  
  - Timestamp  

## How It Works

1. The user provides a natural-language instruction or a shell command.
2. ShellMate builds a structured prompt and sends it to Gemini API.
3. The AI model returns:
   - The appropriate shell command
   - Optional metadata such as explanation and risk level
4. The user can then review, confirm, or execute the command.

## Project Structure

```
ShellMate/
├── cli.py              # Typer-based CLI entry point
├── config.py           # Gemini client configuration
├── context.py          # Local context gathering for AI prompts
├── gemini_client.py    # Gemini API call logic
├── executor.py         # Safe command execution handling
├── prompts.py          # Prompt templates for AI
├── logger.py           # JSON-based activity logger
├── .env.example        # Example environment variables (API key template)
├── .gitignore          # Ignores __pycache__, .env, and logs
└── log.json            # Auto-generated command log (not pushed to Git)
```

## Setup & Installation

1. Clone the repository
   ```bash
   git clone https://github.com/ShivrajCodes/ShellMate.git
   cd ShellMate
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate         # Windows
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables  
   Create a `.env` file based on `.env.example` and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the CLI directly using:
```bash
python run.py gen "create a new directory called test"
```

or after installing:
```bash
shellmate gen "show all running processes"
```

### Available Commands

| Command | Description |
|----------|-------------|
| `gen` | Generate a shell command from natural language |
| `explain` | Explain what a shell command does |
| `repl` | Start interactive REPL session |

## Example Session

```bash
$ shellmate gen "check available disk space"

╭─────────────── Instruction ────────────────╮
│ check available disk space                │
╰────────────────────────────────────────────╯

╭──────────── Generated Command ────────────╮
│ df -h                                     │
│ Checks disk usage in human-readable form. │
╰────────────────────────────────────────────╯

╭────────────── Risk Level ───────────────╮
│ LOW                                    │
╰────────────────────────────────────────╯

Dry run: command not executed.
```

## Tech Stack

- Python 3.10+
- [Typer](https://typer.tiangolo.com/) — for CLI structure
- [Rich](https://github.com/Textualize/rich) — for beautiful terminal output
- [Google Gemini API](https://ai.google.dev/) — for intelligent code generation
- dotenv — for environment variable management
- JSON logging — for persistent activity tracking

## Author

Authors : Nilanjan Mondal, Shivraj Bhattacharya, Nabamita Samui, Sourik Ghosh, Sayantan Das, Debanjan Mondal

## License

This project is licensed under the MIT License — feel free to use and modify it with proper attribution.

