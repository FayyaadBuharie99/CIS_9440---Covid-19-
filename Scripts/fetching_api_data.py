import requests
import json

def fetch_all_data(api_url):
    try:
        all_data = []
        offset = 0
        limit = 1000  # API limit per request

        while True:
            # Construct the URL with offset and limit parameters for pagination
            url = f"{api_url}?$offset={offset}&$limit={limit}"

            response = requests.get(url)
            response.raise_for_status()  # Check for any HTTP errors

            data = response.json()  # Assuming the response is JSON data

            # Append fetched data to the main dataset
            all_data.extend(data)

            if len(data) < limit:
                # If the number of fetched rows is less than the limit, we've fetched all data
                break

            offset += limit  # Increment offset for the next page

        return all_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def save_to_json(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)  # Save data to JSON file with indentation for readability
        print(f"Data saved to {filename}")
    except IOError as e:
        print(f"Error saving data to JSON file: {e}")

# Example API endpoint URL with pagination support
api_endpoint = "https://data.sfgov.org/resource/q3xd-hfi8.json"

# Call the function to fetch all data from the API endpoint using pagination
api_data = fetch_all_data(api_endpoint)

if api_data:
    # Save the data to a JSON file
    save_to_json(api_data, "output_all.json")
else:
    print("Failed to fetch data from the API.")
