# Real-Time Crypto Tracker CLI
A command-line tool to track real-time cryptocurrency prices using token names from decentralized exchanges (DEXes).
## Features
- Fetch real-time price data for a specific token
- Optional CSV export of results
- Watch mode to track price every 60 seconds
- Graceful exit on Ctrl+C
## Usage
```
python main.py --token bonk
python main.py --token bonk --output data.csv
python main.py --token bonk --watch
```
## Arguments
- `--token` (required): Token name (e.g., `bonk`)
- `--output` (optional): Save output to CSV file
- `--watch` (optional): Enable watch mode with updates every 60 seconds
## Requirements
- Python 3.7+
- `requests` (Install with `pip install -r requirements.txt`)
## Setup
```
git clone https://github.com/your-username/crypto_tracker_cli.git
cd crypto_tracker_cli
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## License
MIT