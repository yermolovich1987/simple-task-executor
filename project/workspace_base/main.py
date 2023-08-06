import streamlit as st
from code_generator import generate_function_name
from code_generator import generate_code_from_user_message
from test_generator import generate_tests_from_user_message
from test_evaluator import run_tests
import re
import os
import subprocess
from tempfile import TemporaryDirectory

MAX_ATTEMPTS = 1


def create_attempt_directory(attempt_number):
    attempt_dir = f"attempt_{attempt_number:01}"
    os.makedirs(attempt_dir, exist_ok=True)
    return attempt_dir

def save_to_files(function_name, code, test_code):
    main_file = f"{function_name}.py"
    test_file = f"test_{function_name}.py"
    with open(main_file, 'w') as code_file:
        code_file.write(code)

    with open(test_file, 'w') as test_file:
        test_file.write(test_code)

    print(f"Successfully generated the files: {main_file} and {test_file}.")
    return main_file, test_file


def main():
    st.title("Code Generator App")

    # Get the task on Python from the user
    user_input = st.text_area("Enter the task on Python:")

    # Generate code and tests
    # code = generate_code(user_input)
    # tests = generate_tests(task)

    # Evaluate the generated code
    # test_results = evaluate_tests(code, tests)

    # Display the results
    if st.button("Generate Code"):
        function_name = generate_function_name(user_input)

        # generated_code = generate_code_from_user_message(user_input, function_name)
        print(f"Function name: {function_name}")

        generated_code = "None"
        generated_tests = "None"
        tests_passed = False
        attempts = 0
        while not tests_passed and attempts < MAX_ATTEMPTS:
            # Use OpenAI to generate code and tests
            generated_code = generate_code_from_user_message(user_input, function_name)
            generated_tests = generate_tests_from_user_message(user_input, function_name)
            test_code_with_comment = f"from {function_name} import {function_name}\n\n{generated_tests}"

            # Save codes and tests:
            attempt_dir = create_attempt_directory(attempts)
            os.chdir(attempt_dir)
            main_file, test_file = save_to_files(function_name, generated_code, test_code_with_comment)
            os.chdir("..")
            tests_passed = run_tests(function_name, attempt_dir)
            attempts += 1

        if not tests_passed:
            st.write(
                "Failed to generate working code after maximum attempts. Please try again or manually review the code and tests.")
        else:
            print("All tests successful! Generating final code files...")
            st.subheader("Generated Python code:")
            st.code(generated_code)

            st.subheader("Generated Python Tests for the code above:")
            st.code(generated_tests)


#    st.subheader("Test Results:")
#    for test, result in test_results.items():
#        st.write(f"Test: {test}")
#        st.write(f"Result: {result}")
#        st.write("---")

if __name__ == "__main__":
    main()
