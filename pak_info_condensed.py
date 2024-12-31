import json

# Input JSON file name
input_file = 'pak_info.json'

# Output JSON file name
output_file = 'pak_output.json'

# Array of model_id's to match
model_ids = [181,180,9,52]  # Example model_id's, replace with your own

# Read the JSON data from the input file
with open(input_file, 'r') as file:
    data = json.load(file)

# Filter the JSON data
filtered_data = {k: v for k, v in data.items() if v['model_id'] in model_ids}

# Write the filtered JSON data to the output file
with open(output_file, 'w') as file:
    json.dump(filtered_data, file, indent=4)

print(f"Filtered data has been written to {output_file}")
