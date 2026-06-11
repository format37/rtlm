import os

import pandas as pd
from huggingface_hub import snapshot_download

REPO_ID = "format37/rtlm"
CHANNELS = ["belarusone", "oneplusone", "russiaone", "ORT"]


def download_dataset(local_dir="data"):
    """Download all parquet files from the Hugging Face dataset repo."""
    snapshot_download(
        repo_id=REPO_ID,
        repo_type="dataset",
        allow_patterns="data/*.parquet",
        local_dir=local_dir,
    )
    return local_dir


def load_channel(channel, local_dir="data"):
    """Load all years of a channel into a single DataFrame."""
    channel_dir = os.path.join(local_dir, "data", channel)
    files = sorted(
        os.path.join(channel_dir, f)
        for f in os.listdir(channel_dir)
        if f.endswith(".parquet")
    )
    return pd.concat((pd.read_parquet(f) for f in files), ignore_index=True)


def main():
    print("Downloading dataset from Hugging Face...")
    local_dir = download_dataset()

    for channel in CHANNELS:
        df = load_channel(channel, local_dir)
        print(f"\n{channel}: {len(df)} rows, "
              f"{df['datetime'].min()} .. {df['datetime'].max()}")
        print(df.head())


if __name__ == "__main__":
    main()
