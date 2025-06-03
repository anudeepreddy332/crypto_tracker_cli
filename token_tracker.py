import csv
import datetime
import os.path

import requests


def fetch_token_data(user_token):
    base_url = "https://api.geckoterminal.com/api/v2/search/pools"
    final_url = base_url + f"?query={user_token}"

    try:
        response = requests.get(final_url)
        response.raise_for_status()
        old_data = response.json()
        attributes = old_data['data'][0]['attributes']
        name = attributes['name']
        price = attributes['base_token_price_usd']
        price_change_percentage = attributes['price_change_percentage']['h24']
        fdv_usd = attributes['fdv_usd']
        market_cap = attributes['market_cap_usd']

        data = {
            "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": name,
            "Price": price,
            "Price change %": price_change_percentage,
            "FDV": fdv_usd,
            "Market cap": market_cap
        }
        return data

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")

    except (KeyError, IndexError, TypeError) as e:
        print(f"[ERROR] Unexpected data format: {e}")

    except ValueError as e:
        print(f"[ERROR] Failed to decode JSON: {e}")

    return None

def print_summary(data):
    print(f"[✓] {data['Name']}")
    print(f"Price (USD): ${float(data['Price']):.8f}")
    print(f"24h Change: {data['Price change %']}%")
    print(f"FDV: ${int(float(data['FDV'])) / 1000000000:.2f}B")
    if data.get("Market cap"):
        print(f"Market Cap: ${int(float(data['Market cap'])) / 1000000000:.2f}B")
    else:
        print("Market Cap: N/A")

def save_to_csv(data, filename):
    write_header = not os.path.exists(filename)

    with open(filename, 'a', newline="") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow([
                'Timestamp',
                'Token Name',
                'Price (USD)',
                '24h Change %',
                'FDV (USD)',
                'Market Cap (USD)'
            ])
        w.writerow([
            data['Timestamp'],
            data['Name'],
            f"{float(data['Price']):.8f}",
            data['Price change %'],
            data['FDV'],
            data['Market cap']
        ])