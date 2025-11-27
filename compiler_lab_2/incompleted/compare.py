import subprocess
import difflib

for i in range(1, 8):
    parser = "./parser"
    input_file = f"../test/example{i}.kpl"
    result_file = f"../test/result{i}.txt"
    output_file = "a.txt"

    with open(output_file, "w") as out:
        subprocess.run([parser, input_file], stdout=out)

    with open(output_file, "r") as f1, open(result_file, "r") as f2:
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()

    diff = difflib.unified_diff(
        f1_lines, f2_lines,
        fromfile=output_file,
        tofile=result_file,
        lineterm=""
    )

    print(f"\n===== RESULT {i} DIFF =====\n")
    has_diff = False
    for line in diff:
        has_diff = True
        print(line)

    if not has_diff:
        print("Hai file giống nhau hoàn toàn!")
    else:
        print("\nHai file KHÁC NHAU!")
