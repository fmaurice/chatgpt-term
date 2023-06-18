# chatgpt-term

```console
cat chatgpt.py | ./chatgpt.py "Create a readme.md file for the following python script, the title will be 'chatgpt-term'" > readme.md
```

This is a Python script that allows the user to chat with the GPT-3.5-turbo model from OpenAI via the command-line / terminal.

## Requirements
- Python 3.x
- `requests` module
- `prompt_toolkit` module
- `argparse` module
- `python-dotenv` module
- An OpenAI API key

## Installation
1. Clone the repository.
2. Install the required modules using `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory and add your OpenAI API key in the following format `OPENAI_API_KEY=<your API key>`.
4. Run the script using `python chatgpt-term.py`.

## Usage
The script can be used in the following ways:
1. `python chatgpt-term.py` - This allows the user to chat with the GPT-3.5-turbo model via the command-line. The user can input a question or statement and the model will generate a response.
2. `python chatgpt-term.py <text>` - This allows the user to input a question or statement with the command. The model will generate a response based on the input.
3. `python chatgpt-term.py --debug` - This allows the user to see only the request being sent to the API.
4. `python chatgpt-term.py --debug-response` - This allows the user to see the complete response from the API.

## License
This script is provided under the [MIT License](https://github.com/ashpoul/chatgpt-term/blob/main/LICENSE).
