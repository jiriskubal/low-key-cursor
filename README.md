# 🤖 Low-Key Cursor - AI Coding Assistant

> ⚠️ **Warning**: I don't recommend using a code you're afraid of losing 😄😄

A lightweight AI coding assistant powered by Google's Gemini API that can perform various file operations and code execution tasks through natural language prompts.

## ✨ Features

- 🔍 **File Operations**: List directories, read file contents, and write files
- 🐍 **Python Execution**: Run Python scripts with optional arguments
- 💬 **Natural Language Interface**: Describe what you want to do in plain English
- 🗣️ **Verbose Mode**: Optional detailed output for debugging and understanding

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Google Gemini API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd low-key-cursor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Gemini API key:
```bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

### Usage

Basic usage:
```bash
python main.py "your prompt here"
```

With verbose output:
```bash
python main.py "your prompt here" --verbose
```

#### Example Commands

```bash
# Analyze code structure
python main.py "Show me all files in the calculator directory"

# Get help with debugging
python main.py "How do I fix the calculator?"

# Code analysis
python main.py "What does the main.py file do?"

# Execute Python scripts
python main.py "Run the calculator with these numbers: 5 and 3"
```


## ⚙️ Configuration

The `config.py` file contains key settings:

- `MAX_CHARS`: Maximum characters for file content (default: 10,000)
- `WORKING_DIR`: Restricted working directory (default: "./calculator")
- `MAX_ITERS`: Maximum iterations for AI responses (default: 20)

## 🛠️ Available Functions

The AI assistant can perform these operations:

| Function | Description |
|----------|-------------|
| `get_files_info` | List files and directories with sizes |
| `get_file_content` | Read and display file contents |
| `run_python_file` | Execute Python scripts with arguments |
| `write_file` | Create or overwrite files |

## 🔒 Security Features

- **Directory Restriction**: All operations are limited to the configured working directory
- **Path Validation**: Prevents access to files outside the permitted area
- **Safe Execution**: Python execution is sandboxed to the working directory


### Verbose Mode

Use `--verbose` flag to see detailed information about:
- Function calls and their arguments
- Token usage (prompt and response tokens)
- Function call results

## 📝 Examples

### File Analysis
```bash
python main.py "What files are in the current directory and what do they do?"
```

### Code Debugging
```bash
python main.py "There's a bug in calculator.py, can you help me find it?"
```

### Code Generation
```bash
python main.py "Create a simple Python script that calculates the factorial of a number"
```
