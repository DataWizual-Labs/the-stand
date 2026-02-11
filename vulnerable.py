# Test file for Auditor Core
import os
password = "AKIAIMNO78987EXAMPLE" # Это должен поймать Gitleaks
os.system(f"rm -rf {password}")    # Это должен поймать Semgrep/Bandit
eval("print('hello')")             # Это должен поймать SAST