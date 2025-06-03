from argparse import ArgumentParser
from token_tracker import *
import time
def main():
    parser = ArgumentParser(
        description="Crypto Currency Tracker CLI"
    )
    parser.add_argument(
        "--token",
        required=True,
        help="Token name from DEX it’s trading on, e.g. bonk"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Saves results to CSV"
    )
    parser.add_argument(
        "--watch",
        action="store_true",
        help="Fetches price based on the set time"
    )

    args = parser.parse_args()

    if args.watch:
        print(f"[INFO] Watching {args.token} every 60 seconds...Press (Control + c) to interrupt.")
        try:
            while True:
                data = fetch_token_data(args.token)
                print_summary(data)
                if args.output:
                    save_to_csv(data, args.output)
                time.sleep(60)
                print("\n"*1)
        except KeyboardInterrupt:
            print("\n[INFO] Interrupted.")

    else:
        data = fetch_token_data(args.token)
        print_summary(data)
        if args.output:
            save_to_csv(data, args.output)


if __name__ == "__main__":
    main()

