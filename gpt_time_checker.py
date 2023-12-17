import json
import datetime
import os
import sys

def convert_timestamp_to_datetime(timestamp):
    datetime_obj = datetime.datetime.utcfromtimestamp(timestamp)
    return datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

def search_in_json(file_path, search_text):
    matches = []
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for key, value in data['mapping'].items():
            if 'message' in value and search_text in value['message']['content']['parts'][0]:
                timestamp = value['message']['create_time']
                formatted_date_time = convert_timestamp_to_datetime(timestamp)
                matches.append((value['message']['content']['parts'][0], formatted_date_time))
    return matches

def main():
    json_files = [f for f in os.listdir('.') if f.endswith('.json')]
    total_size = sum(os.path.getsize(f) for f in json_files)

    if len(json_files) > 10 or total_size > 10 * 1024 * 1024:
        print("Too many JSON files or total size too large. Please reduce the number or size of JSON files.")
        sys.exit(1)

    search_text = input("Enter the text snippet you're searching for (type 'q' to quit): ")
    if search_text.lower() == 'q':
        return
    # TODO make fast copy option, like just press enter then the most recent date will be copied to clipboard

    for json_file in json_files:
        matches = search_in_json(json_file, search_text)
        if matches:
            for match in matches:
                print(f"File: {json_file}\n{match[0]}\n{match[1]}\n")
            if len(matches) > 1:
                print("Multiple matches found.")

if __name__ == "__main__":
    main()
