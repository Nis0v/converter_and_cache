import requests
import json

#cache update
def url_1(currency):
    global n
    url = f'http://www.floatrates.com/daily/{currency}.json'
    r = requests.get(url)
    r = r.text
    r = json.loads(r)
    n = r
    return n

#Loading currencies

url_1('usd')
cache = {'usd': n}
url_1('eur')
cache['eur'] = n

#Currency they want to exchange
currency = input()
currency = currency.lower()


#Checking if the currency is in the cache
if currency not in cache:
    url_1(currency)
    cache[currency] = n

#Course cycle
while currency:

    #Currency they want to receive
    currency_cnvr = (input())

    #Checking for an empty value
    if currency_cnvr != "":
        currency_cnvr = currency_cnvr.lower()
        number = float(input())
        print('Checking the cache...')

        #Checking if the currency is in the cache
        if currency_cnvr in cache:
            print('Oh! It is in the cache!')
            c = cache[currency][currency_cnvr]["rate"]
            print(f'You received {round((number * float(c)), 2)} {currency_cnvr.upper()}.')
        else:

            #Adding currency to the cache
            print('Sorry, but it is not in the cache!')
            url_1(currency_cnvr)
            cache[currency_cnvr] = n
            c = cache[currency][currency_cnvr]["rate"]
            print(f'You received {round((number * float(c)), 2)} {currency_cnvr.upper()}.')
    else:
        break