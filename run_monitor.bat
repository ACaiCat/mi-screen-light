@echo off
chcp 65001 >nul
cd /d "%~dp0"
start "" /B uv run main.py
exit