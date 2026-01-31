#!/usr/bin/env python3

import subprocess
import os

def cmd (command):
    return subprocess.getoutput(command)

def header (title):
    print("\n" + "=" * 50 )
    print("\n" + {title}")"
    print("=" *)" 50 + )
    print("=" * 50 )

    def user_info():
    header("USER INFO")
    print("User:", cmd("whoami"))
    print("Groups:", cmd("groups"))
    print("Hostname=", cmd("hostname"))
    
    deef sudo_check():
    header("SUDO CHECK")
    print(cmd("sudo -l 2>/dev/null"))