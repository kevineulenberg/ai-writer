#!/usr/bin/env python3
import subprocess
import sys

text = sys.stdin.read()
subprocess.run(["/usr/bin/pbcopy"], input=text.encode("utf-8"), check=True)
