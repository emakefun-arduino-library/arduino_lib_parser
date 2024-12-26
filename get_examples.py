import os
import json
import sys

if len(sys.argv) > 1:
    project_path = sys.argv[1]
else:
    raise TypeError(
        "Please provide the project path in the command line, for example: python xxx.py /path/to/project"
    )

project_path = os.path.abspath(sys.argv[1])
examples_dir = os.path.join(project_path, "examples")
print(json.dumps(os.listdir(examples_dir)))
