# rtlm
Tools for downloading and processing the [rtlm](https://rtlm.info) dataset

## Installation
```bash
git clone https://github.com/format37/rtlm.git
cd rtlm
pip install -r requirements.txt
```

## Usage

### Download Dataset
```bash
python download_parquet.py
```

### Query with BigQuery
For users with Google Cloud access:
```bash
python big_query_request.py
```