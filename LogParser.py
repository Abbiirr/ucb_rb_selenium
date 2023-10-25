import xml.etree.ElementTree as ET
import re
import json

# Replace 'log_file_paths' with a list of actual log file paths
log_file_paths = [
    'C:\\Abir\\bulk.log.2023-10-25.16\\bulk.log.2023-10-25.16',
    'C:\\Abir\\log.txt'
    # Add more log file paths as needed
]

# Create an empty list to store log data
all_log_data = []
all_log_data.append('<root>')
# Load and append data from each log file
for log_file_path in log_file_paths:
    with open(log_file_path, 'r') as log_file:
        log_data =  log_file.read()
        all_log_data.append(log_data)

all_log_data.append('</root>')

# Concatenate log data from all files
concatenated_log_data = ''.join(all_log_data)

# Parse the concatenated log data
root = ET.fromstring(concatenated_log_data)

duplicate_counter = {}

for log_row in root.findall('.//log-row'):
    log_message = log_row.find('log-message')
    method_invocation = log_message.text.strip()

    # Check if it's a request for 'requestForIntraFundTransferProcessor'
    if 'Invoking Method: requestForIntraFundTransferProcessor' in method_invocation:
        request_id = log_row.find('request-id').text

        # Extract the request body
        request_message = log_row.find('.//log-message')
        request = request_message.text.strip()

        json_part = re.search(r'{.*}', request)
        if json_part:
            extracted_json = json_part.group(0)

            # Parse the extracted JSON
            try:
                parsed_json = json.loads(extracted_json)
                ftdId = parsed_json['fundTransferDetailsId']
                if ftdId in duplicate_counter:
                    duplicate_counter[ftdId] = duplicate_counter[ftdId] + 1
                else:
                    duplicate_counter[ftdId] = 1
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON: {e}")
        else:
            print("No JSON found in the log message.")

for index, (key, value) in enumerate(duplicate_counter.items()):
    print(f'Index {index}: {key}: {value}')
