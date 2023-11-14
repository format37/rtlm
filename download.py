import os
import requests
import xml.etree.ElementTree as ET
from tqdm import tqdm

def download_files(base_url, paths, path_to_save):
    for path in tqdm(paths, desc="Downloading files", unit="file"):
        # Construct the full URL
        url = f"{base_url}/{path}"

        # Determine local file path
        local_path = os.path.join(path_to_save, path)

        # Skip if file already exists
        if os.path.exists(local_path):
            continue

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        # Download and save the file
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_path, 'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed to download {path}")


def main():

    path_to_save = ''

    # Base URL of the GCS bucket
    base_url = 'https://storage.googleapis.com/rtlm'
    response = requests.get(base_url)

    # Ensure the response is OK and the content type is XML
    if response.status_code == 200 and 'xml' in response.headers.get('Content-Type', ''):
        print("Successfully fetched XML")
        # Define the namespace
        ns = {'ns': 'http://doc.s3.amazonaws.com/2006-03-01'}
        # Parse the XML from the response text
        root = ET.fromstring(response.content)
        print(f"root: {root}")

        paths = [elem.text for elem in root.findall('.//ns:Key', ns)]

        print(f"Count of files to check: {len(paths)}")
        # Filter out existing files
        existing_files = [path for path in paths if os.path.exists(os.path.join(path_to_save, path))]
        paths = [path for path in paths if path not in existing_files]
        print(f"Count of files to download: {len(paths)}")

        download_files(base_url, paths, path_to_save)

    else:
        print("Failed to fetch or parse XML")


if __name__ == '__main__':
    main()
