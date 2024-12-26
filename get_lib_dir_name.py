import os
import sys

if len(sys.argv) > 1:
    project_path = sys.argv[1]
else:
    raise TypeError(
        "Please provide the project path in the command line, for example: python xxx.py /path/to/project"
    )

project_path = os.path.abspath(sys.argv[1])

with open(
    os.path.join(project_path, "library.properties"),
    "r",
    encoding="utf-8",
) as f:

    while True:
        line = f.readline()

        if len(line) == 0:
            break

        if line.startswith("name="):
            print(line.split("=")[1].strip().replace(" ", "_"))
            break
