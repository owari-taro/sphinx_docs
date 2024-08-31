#!/usr/bin/python3
import subprocess

size=100_000_000

subprocess.run(["free","-h"])

array=[0]*size
print("\n1個目の配列を作成後")
subprocess.run(["free","-h"])

array2=[0]*size
print("\n2個目の配列を作成後")
subprocess.run(["free","-h"])
