import requests
import pandas as pd
import os
from tqdm import tqdm

class DataDownloader:
    def __init__(self, base_url='https://storage.googleapis.com/rtlm/parquet'):
        self.base_url = base_url
        self.channels = ['belarusone', 'oneplusone', 'russiaone', 'ORT']
        self.data_dir = 'data'
        self.dfs = {}
        
        # Create directory for downloads if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)

    def download_channel_data(self, channel):
        """Download parquet file for a specific channel if it doesn't exist."""
        url = f"{self.base_url}/{channel}/{channel}.parquet"
        local_path = f"{self.data_dir}/{channel}.parquet"
        
        if not os.path.exists(local_path):
            response = requests.get(url)
            if response.status_code == 200:
                with open(local_path, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded {channel} data")
                return True
            else:
                print(f"Failed to download {channel} data")
                return False
        return True

    def load_channel_data(self, channel):
        """Load parquet file for a specific channel into DataFrame."""
        local_path = f"{self.data_dir}/{channel}.parquet"
        if os.path.exists(local_path):
            self.dfs[channel] = pd.read_parquet(local_path)
            print(f"\n{channel} DataFrame loaded successfully")
            return True
        print(f"No data file found for {channel}")
        return False

    def download_all_channels(self):
        """Download data for all channels."""
        for channel in tqdm(self.channels, desc="Downloading channel data"):
            self.download_channel_data(channel)

    def load_all_channels(self):
        """Load all downloaded channel data into DataFrames."""
        for channel in self.channels:
            self.load_channel_data(channel)

    def get_dataframe(self, channel):
        """Get DataFrame for a specific channel."""
        return self.dfs.get(channel)

def main():
    # Initialize downloader
    downloader = DataDownloader()
    
    # Download and load all channel data
    print("Starting download process...")
    downloader.download_all_channels()
    
    print("\nLoading downloaded data...")
    downloader.load_all_channels()
    
    # Display sample data for each channel
    for channel in downloader.channels:
        df = downloader.get_dataframe(channel)
        if df is not None:
            print(f"\n{channel} DataFrame head:")
            print(df.head())

if __name__ == "__main__":
    main()
    