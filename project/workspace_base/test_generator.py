import openai

system_message = f"""
You are the senior software engineer with good Python background.
"""


def generate_tests_from_user_message(user_input, function_name, model="gpt-3.5-turbo", temperature=0, max_tokens=3000):
    code_prompt = f"Create test cases for the Python function {function_name}. The test cases should cover user input. Your response should contain just test code without additional markup (like ```python```) or thoughts. <user_input>{user_input}<user_input>"
    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': code_prompt}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]
