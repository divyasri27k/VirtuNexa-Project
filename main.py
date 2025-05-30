
from shortener import shorten_url, retrieve_url
from db import init_db, increment_clicks, get_clicks
import logging

logging.basicConfig(filename='logs/activity.log', level=logging.INFO)

def main():
    init_db()
    while True:
        print("\n--- URL Shortener ---")
        print("1. Shorten a URL")
        print("2. Retrieve original URL")
        print("3. View click analytics")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            long_url = input("Enter the long URL: ")
            short = shorten_url(long_url)
            print("Short URL:", short)
        elif choice == '2':
            short = input("Enter the short URL code: ")
            original = retrieve_url(short)
            if original:
                increment_clicks(short)
                print("Original URL:", original)
            else:
                print("Invalid short code.")
        elif choice == '3':
            url = input("Enter short URL code: ")
            count = get_clicks(url)
            print(f"Click count for {url}: {count}")
        elif choice == '4':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
