# rtlm
Tools for downloading and processing the rtlm dataset — transcriptions of the 24/7 live streams of four TV channels (Channel One/ORT, Russia 1, Belarus 1, 1+1), November 2023 – February 2025, transcribed with Whisper large-v2.

The dataset is hosted on Hugging Face: https://huggingface.co/datasets/format37/rtlm

## Installation
```bash
git clone https://github.com/format37/rtlm.git
cd rtlm
pip install -r requirements.txt
```

## Usage

### Load with the datasets library
```python
from datasets import load_dataset

ds = load_dataset("format37/rtlm", split="train")            # all channels
ort = load_dataset("format37/rtlm", "ORT", split="train")    # a single channel
```

### Download parquet files
```bash
python download_parquet.py
```

### Query with BigQuery
For users with Google Cloud access:
```bash
python big_query_request.py
```
