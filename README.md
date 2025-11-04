<h1 align="center">⚙️ <b>AI Powered CLI Assistant</b></h1>  
<h3 align="center"><i>Your Smart Command-Line Co-Pilot</i></h3>  

AI Powered CLI Assistant (Shellmate) is an intelligent terminal companion that turns natural language instructions into safe, executable shell commands.<br>
It explains what each command does, evaluates risk levels, and allows dry-run or real execution — making command-line automation effortless, educational, and secure.<br>
Powered by <b>Google Gemini AI</b>, it blends reasoning, safety, and clarity in one sleek CLI experience.  

---

<h2>✨ Features</h2>  

💬 <b>Natural Language → Command Conversion</b> – Type what you mean; the AI writes the correct shell command.<br>
🧠 <b>Command Explanation</b> – Understand every line before executing.<br>
⚠️ <b>Risk Assessment</b> – Automatically grades each command as Low, Medium, or High risk.<br>
🧪 <b>Dry-Run Mode</b> – Safely preview the command without running it.<br>
🔒 <b>Safe Execution</b> – Approve and execute commands only when ready.<br>
⚡ <b>Gemini-Powered Intelligence</b> – Uses Google Gemini AI for deep understanding and accurate command crafting.<br>
🧾 <b>Execution Summary</b> – Displays result code, stdout, and stderr after each run.<br>

---

<h2>🧠 Tech Stack</h2>  

<b>Python</b> – Core development & CLI logic<br>
<b>Google Gemini AI</b> – Natural language understanding & command reasoning<br>
<b>Click / Argparse</b> – Command-line interface framework<br>
<b>dotenv</b> – Secure API key configuration<br>
<b>OS / subprocess</b> – Command execution & system integration<br>

---

<h2>📁 Project Modules</h2>  

🧩 <b>Command Parser & Generator</b> – Converts natural language to valid shell syntax<br>
🔍 <b>Explanation & Risk Analyzer</b> – Describes what the command does and assesses safety<br>
🧪 <b>Dry-Run / Safe Execution Engine</b> – Offers interactive confirmation before execution<br>
🧰 <b>CLI Interface (Shellmate)</b> – Elegant text-based output with color-coded sections<br>
🔐 <b>Gemini API Integration</b> – Powers intelligent command synthesis and reasoning<br>

---

<h2>🚀 Example Usage</h2>

```bash
./run.py gen "Can you list all my files in Downloads that I have downloaded more than 1 year ago and not used for 1 year" --no-dry

Instruction
Can you list all my files in Downloads that I have downloaded more than 1 year ago and not used for 1 year

Generated Command
bash
Copy code
find ~/Downloads -type f -mtime +365 -atime +365
Explanation
Lists all regular files in your Downloads folder that were modified over a year ago and not accessed for a year — identifying old, unused files.

Risk Level: LOW ✅

Execution Result:
bash
Copy code
/Users/.../googlechrome.dmg  
/Users/.../971.eps  
/Users/.../.localized  
 ```
---
<h2>💡 Why You’ll Love It</h2>
✅ Eliminates guesswork from terminal usage<br>
✅ Prevents risky command execution<br>
✅ Educates you about shell commands<br>
✅ Boosts productivity through automation<br>

<h3 align="center">🚀 Crafted with ❤️ using <b>Python + Google Gemini AI</b></h3>
