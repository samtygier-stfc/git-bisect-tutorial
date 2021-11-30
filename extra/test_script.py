#!/usr/bin/env python
import sys
import subprocess
import os

# modify file
orginal = open("lorenzattractor.py").readlines()
with open("lorenzattractor.py", "w") as outfile:
    for line in orginal:
        if "plt.show" in line:
            indent = line[:line.find("plt.show")]

            outfile.write(indent + "import math\n")
            outfile.write(indent + "if math.isnan(xs[-1]): print('BISECT_BAD')\n")
            outfile.write(indent + "else: print('BISECT_GOOD')\n")
        else:
            outfile.write(line)
    outfile.flush()
    os.fsync(outfile.fileno())

# run modified, capturing standard output
output = subprocess.run([sys.executable, "lorenzattractor.py"], stdout=subprocess.PIPE, encoding="UTF-8").stdout
subprocess.run(["git", "reset", "--hard"])

# check for special keys
if "BISECT_BAD" in output:
    print("bad")
    sys.exit(1)
if "BISECT_GOOD" in output:
    print("good")
    sys.exit(0)

print("skip")
sys.exit(125)
