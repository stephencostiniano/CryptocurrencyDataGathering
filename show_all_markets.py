import ccxt
exchange = ccxt.binance({'enableRateLimit': True})

market = exchange.fetch_markets()
symbol_set = []
for i in range(0, len(market)-1):
    base = market[i]['base']
    quote = market[i]['quote']
    symbol = market[i]['symbol']
    symbol_set.append(symbol)




print(len(symbol_set))

