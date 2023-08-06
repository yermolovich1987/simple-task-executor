Based on the requirements and information provided, here is the proposed architecture for the application:

1. `main.py`: The entry point of the application. It will handle the user interface using Streamlit and coordinate the code generation, test generation, and evaluation processes.

2. `code_generator.py`: This module will contain the logic for generating code based on the specified interface using Open AI LLM.

3. `test_generator.py`: This module will contain the logic for generating tests based on the specified interface using Open AI LLM.

4. `test_evaluator.py`: This module will contain the logic for evaluating the generated code by running the tests and determining if they pass or fail.

**main.py**

streamlit run main.py

The sample of user inputs:

`A code that parses product CSV file with 3 columns: SKU, quantity, price. The result should output the total quantity.`