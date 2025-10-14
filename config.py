import os
import json
from pathlib import Path
from typing import Optional
import keyring
from rich.console import Console
from google import genai

console = Console()

def _key_from_env() -> Optional[str]:
    return os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY") or os.getenv("GENAI_API_KEY")

def _key_from_config_file() -> Optional[str]:
    cfg_path = Path.home() / ".shellmate" / "config.json"
    if cfg_path.exists():
        try:
            data = json.loads(cfg_path.read_text())
            return data.get("gemini_api_key")
        except Exception as e:
            console.print(f"[yellow]Warning: failed reading {cfg_path}: {e}[/yellow]")
    return None

def _key_from_keyring() -> Optional[str]:
    try:
        secret = keyring.get_password("shellmate", "gemini_api_key")
        if secret:
            return secret
    except Exception as e:
        console.print(f"[yellow]Warning: keyring access failed: {e}[/yellow]")
    return None

def make_client() -> genai.Client:
    api_key = _key_from_env() or _key_from_config_file() or _key_from_keyring()

    if not api_key:
        console.print(
            "[bold red]ERROR:[/bold red] No Gemini API key found.\n"
            "Provide it via one of these methods:\n"
            "1) create a .env file with GEMINI_API_KEY=...\n"
            "2) create ~/.shellmate/config.json with {\"gemini_api_key\":\"...\"}\n"
            "3) store it in your OS secret store using keyring"
        )
        raise SystemExit(1)

    try:
        return genai.Client(api_key=api_key)
    except Exception as e:
        console.print(f"[red]Failed to create GenAI client:[/red] {e}")
        raise SystemExit(1)
