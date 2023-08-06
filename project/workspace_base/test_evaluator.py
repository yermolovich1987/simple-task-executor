import subprocess
import os


def run_tests(function_name, attempt_dir):
    original_working_dir = os.getcwd()
    os.chdir(attempt_dir)
    test_results = subprocess.run(["python", f"test_{function_name}.py"], capture_output=True, text=True)
    os.chdir(original_working_dir)
    if test_results.returncode == 0:
        print("Tests passed!")
        return True
    else:
        print("Tests failed. Please generate more tests or update the implementation.")
        print(test_results.stderr)
        return False
