# warframe-item-price
A simple Python (3.x) script with no dependencies needed that uses warframe.market API (api.warframe.market/v1/) to output min price, max price, and avg price in the last hour and last 12 hour.

## HOW TO USE
1. Install Python 3.x
2. Download or clone this repository
3. Run main.py with `python main.py` on the shell
4. Enter item name
5. Profit

## EXAMPLE
```
$ py main.py
Look for individual item or a set (ex: 'trinity prime set', 'volt prime chassis') without quotes
> vauban prime chassis

        | VAUBAN PRIME CHASSIS |
        SOLD/BOUGHT
        Last Hour:
        Volume: 3
        Min price: 15.0
        Max price: 15.0
        Average price: 15.0

        Last 12 hours:
        Volume: 44
        Min price: 9.0
        Max price: 15.0
        Average price: 12.583333333333334

Look for individual item or a set (ex: 'trinity prime set', 'volt prime chassis') without quotes
>
```

# NOTE:
- Platform: pc
- Language: en

To change platform or language, simply edit the headers on line 14 using text editor (notepad, notepad++, etc) to your need.

- Available platform: pc, xbox, ps4
- Avaliable language: en, ru
