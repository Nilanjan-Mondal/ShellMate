<div align="center">

![github](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)
![python](https://img.shields.io/badge/Python-181717.svg?style=for-the-badge&logo=python&logoColor=white)
![typer](https://img.shields.io/badge/Typer-181717.svg?style=for-the-badge)
![rich](https://img.shields.io/badge/Rich-181717.svg?style=for-the-badge)

# ShellMate – Smart Terminal Assistant

</div>

ShellMate is a lightweight CLI tool that helps users **convert natural language instructions into shell commands**, **explain existing commands**, and interactively execute them safely. It leverages the **Gemini AI model** for generating accurate and context-aware commands.

---
<div align="center">
  <img src="https://cdn.discordapp.com/attachments/1235309844290867221/1435511680632094720/IMG-20251104-WA0000.jpg?ex=690c3bef&is=690aea6f&hm=bfe85fa9499dd58ea1c1ba4615d3bc4a525d1bb8321e2da5b1f08e52c84e71af" height=700 width=700/>
</div>
---

> [!NOTE]
>
> ## Features
>
> - **_Natural language → shell commands_** (`gen` command)
> - **_Explain shell commands in plain English_** (`explain` command)
> - **_Safe execution with dry-run option_**
> - **_Context-aware command generation_** using current working directory
> - **_Command risk assessment and explanation_**

---

<div align="center">

| Role           | Tech Used                                                                                                                                                                                                                                                             |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CLI            | ![Python](https://img.shields.io/badge/Python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white) ![Typer](https://img.shields.io/badge/Typer-%23404d59.svg?style=for-the-badge) ![Rich](https://img.shields.io/badge/Rich-%23111.svg?style=for-the-badge) |
| AI Integration | ![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2.svg?style=for-the-badge&logo=Google-Gemini&logoColor=white) ![GenAI](https://img.shields.io/badge/Google%20GenAI-FF6F61.svg?style=for-the-badge)                                                        |

</div>

---

## How It Works

1. User provides a **natural language instruction** (e.g., "move all .txt files to Documents").
2. ShellMate sends the instruction along with **local context** to the Gemini AI model.
3. The AI generates a **safe Bash command** with a short explanation and a risk level.
4. User can **preview** the command (dry-run) or choose to **execute** it.
5. Users can also **explain any existing shell command** in plain English.
6. All activities are logged in `log.json` for audit and debugging.

---

## Project Structure

```
ShellMate/
|
├── pycache/                    # cache files (auto gen)
|
├── cli.py                      # Typer CLI app with commands
├── run.py                      # Entry point
├── executor.py                 # Safe command execution
├── gemini_client.py            # Gemini AI API calls
├── context.py                  # Local file context extraction
├── prompts.py                  # Prompt templates for Gemini AI
├── config.py                   # Gemini API client setup
├── logger.py                   # Logging user activity
├── .env                        # environment variables
├── requirements.txt            # python dependencies
|
├── LICENSE                     # project license
└── README.md
```

---

## Setup & Installation

1. **Clone the repository**
```bash
git clone https://github.com/Nilanjan-Mondal/ShellMate.git
cd ShellMate
```
2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Setup environment variables**
```bash
touch .env
cat GEMINI_API_KEY=your_api_key_here > .env
```
5. **Make the file executable**
```bash
chmod +x run.py
```
6. **Run the CLI**
```bash
./run.py --help
```

---

## Use Cases

- Developers who want to generate shell commands safely without memorizing syntax.
- Users learning shell commands who need explanations in plain English.
- Interactive terminal assistance for quick automation tasks.
- Context-aware command generation based on current working directory and files.

---

<div align="center">

<br>
<br>

| Member          | Role                           |
| --------------- | ------------------------------ |
| Nilanjan Mondal | Core Development & Maintenance |
| Shivraj         | Logging Implementation         |

<br>


<a href="https://github.com/nilanjan-mondal"><img src="https://github.com/user-attachments/assets/c0336e8b-334c-46e0-9743-1b4df092ea23" height=70 width=70></a>
<a href="https://github.com/ShivrajCodes"><img src="https://github.com/user-attachments/assets/36862894-4439-407f-b428-85d8cff152a8" height=70 width=70></a>

</div>

<br>


<p align="center">
<a href="https://github.com/Nilanjan-Mondal/ShellMate/blob/main/LICENSE">
<img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/>
</a>
</p>
