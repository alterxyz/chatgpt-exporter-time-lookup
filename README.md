# chatgpt-exporter-time-lookup

To verify the timestamps(time) of specific parts of conversations in ChatGPT's chat history.

## Overview

**chatgpt-exporter-time-lookup** is a simple extension tool for the [chatgpt-exporter](https://github.com/pionxzh/chatgpt-exporter).

It allows users to easily search for messages within their exported ChatGPT conversations and view these messages with their associated timestamps in a human-readable format.

*In easy words*, copy and paste a snippet of text, and this simple program will return the message with its **time**.

## Features

- **Effortless Timestamp Lookup**: Instantly convert Unix timestamps from exported ChatGPT JSON files to readable date-time formats.
- **Simple Text Search**: Input a snippet from your ChatGPT conversation and find the exact message along with its timestamp.
- **Handle Multiple Matches**: If there are multiple matches for your query, the tool will list all, providing a comprehensive view.

## Usage

1. **Download the Python File**: Simply download the `gpt_time_checker.py` file from this repository.
2. **Place in JSON Directory**: Move this downloaded file to the directory where your exported ChatGPT JSON file is located.
3. **Run the Tool**: Run the python program as you like.
4. **Follow Prompts**: Enter the path to your JSON file and the snippet of text you are searching for. The tool will do the rest, displaying any and all matches along with their timestamps.

## System Requirements

- **Python Version**: This tool was developed and tested using Python 3.11.7.
- **Operating System**: It was run on Windows 11, using Visual Studio Code's integrated terminal.
- **Python Installation**: Ensure Python is installed on your system to use this tool.

## Installation

No additional installation is necessary beyond having Python installed on your system. This tool is designed to run directly from the command line with minimal setup.

## Contributing

Your contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is under the MIT License.
