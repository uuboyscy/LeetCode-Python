from pathlib import Path

input_str = "485. Max Consecutive Ones"
docstring = """
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

output_str = "_%05d" % int(input_str.split(".")[0]) + input_str.split(".")[1].lower().replace(" ", "_")

docstring = '"""' + docstring + '"""\n'

Path(output_str).mkdir()
with Path(f"{output_str}/solution.py").open("w", encoding="utf-8") as f:
    f.write(docstring)
