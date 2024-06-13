import json

# Function to load the JSON data from a file
def load_json_data(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}.")
        return {}

# Function to find data by partial name
def find_data_by_name(data, name):
    results = []
    for key, value in data.items():
        if name.lower() in value['name'].lower():
            results.append(value)
    return results

# Load the JSON data
data = load_json_data('data.json')

# Loop to keep listening for input
while True:
    # Prompt the user for a name
    name_to_find = input("Enter the name (or type 'exit' to quit): ")

    # Check if the user wants to exit
    if name_to_find.lower() == 'exit':
        print("Exiting the program.")
        break

    # Find the data by name
    results = find_data_by_name(data, name_to_find)

    # Display the results
    if results:
        for result in results:
            print(json.dumps(result, indent=4))
    else:
        print("No data found for the given name.")
