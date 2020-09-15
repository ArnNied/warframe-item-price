from json import loads
from statistics import mean
from time import sleep
from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request

def main():
    while True:
        print("Look for individual item or a set (ex: 'trinity prime set', 'volt prime chassis') without quotes")
        search = input("> ").strip().lower()

        try:
            req = Request(
                url=f"https://api.warframe.market/v1/items/{search.replace(' ', '_')}/statistics", 
                headers={'language': 'en', 'platform': 'pc'}
                )
            response = loads(urlopen(req).read())['payload']['statistics_closed']['48hours']
        except HTTPError:
            print("ERROR: Invalid item, check if the item name is correct\n")
            sleep(0.75)
            continue
        except URLError:
            print("ERROR: Please make sure you are connected to the internet\n")
            sleep(0.75)
            continue

        last_twelve_hours = {
            'volume': 0,
            'min_price': [],
            'max_price': [],
            'avg_price': [],
        }
        
        for data in response[-13:-1]:
            last_twelve_hours['volume'] += data['volume']
            last_twelve_hours['min_price'].append(data['min_price'])
            last_twelve_hours['max_price'].append(data['max_price'])
            last_twelve_hours['avg_price'].append(data['avg_price'])

        print(f"""
        | {search.upper()} |
        SOLD/BOUGHT
        Last Hour:
        Volume: {response[-1]['volume']}
        Min price: {response[-1]['min_price']}
        Max price: {response[-1]['max_price']}
        Average price: {response[-1]['avg_price']}

        Last 12 hours:
        Volume: {last_twelve_hours['volume']}
        Min price: {min(last_twelve_hours['min_price'])}
        Max price: {max(last_twelve_hours['max_price'])}
        Average price: {mean(last_twelve_hours['avg_price'])}
        """)

if __name__ == '__main__':
    main()
