import json
import datetime
import os
import sys


def convert_timestamp_to_datetime(timestamp):
    datetime_obj = datetime.datetime.utcfromtimestamp(timestamp)
    '''
    FYI: 2020-12-31 23:59:59 %Y-%m-%d %H:%M:%S
    231225_15:57 %y-%m-%d %H:%M:%S
    '''
    return datetime_obj.strftime('%y%m%d_%H%M')


def search_in_json(file_path, search_text):
    matches = []
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for key, value in data['mapping'].items():
            if 'message' in value:
                content = value['message']['content']['parts'][0]
                if search_text in content:
                    timestamp = value['message']['create_time']
                    formatted_date_time = convert_timestamp_to_datetime(
                        timestamp)
                    matches.append((content, formatted_date_time))
    return matches
# TODO handling if content contains key words. e.g. "message" or "content" or "parts" or "create_time"
# TODO make fast copy option, like just press enter then the most recent date will be copied to clipboard


def main():
    json_files = [f for f in os.listdir('.') if f.endswith('.json')]
    total_size = sum(os.path.getsize(f) for f in json_files)

    if len(json_files) > 10 or total_size > 10 * 1024 * 1024:
        print("Error:\nToo many JSON files or total size too large. Please reduce the number or size of JSON files. \n Or you may modify the code to handle large files but it may take a long time to search.")
        sys.exit(1)
    print("Enter the text snippet you're searching for!\n(type 'q' or 'Ctrl + c' to quit)\n")

    while True:
        search_text = input("Search:")
        if search_text.lower() == 'q':
            break
        elif len(search_text) <= 1:
            print(
                "Please enter at least 2 characters!\n(or type 'q' or 'Ctrl + c' to quit)")
            continue

        print(f"========================================")

        for json_file in json_files:
            matches = search_in_json(json_file, search_text)
            if matches:
                for match in matches:
                    print(f"\n{match[0]}\n\n{match[1]}\n")
                print(f"========================================")
                if len(matches) > 1:
                    print("Warning:\nMultiple matches found!\n~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    main()
