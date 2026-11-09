@echo off
chcp 65001 >nul
pip install -r requirements.txt
python zstd_tool.py
