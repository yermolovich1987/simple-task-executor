import openai

system_message = f"""
You are the senior software engineer with good Python background.
"""


def generate_function_name(user_input, model="gpt-3.5-turbo", temperature=0, max_tokens=3000):
    # TODO Function name could be supplied by user.

    code_prompt = f"Generate a name of the Python function based on the following statement delimited with triple backtick. The output should single string with function name. ```{user_input}```\n"
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


def generate_code_from_user_message(user_input, function_name, model="gpt-3.5-turbo", temperature=0, max_tokens=3000):
    code_prompt = f"Generate a Python function with name {function_name} based on the user input. Your response should contain just python code without additional markup or thoughts. <user_input>{user_input}<user_input>\n"
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
