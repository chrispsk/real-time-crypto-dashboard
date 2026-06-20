from django.shortcuts import render
from .tasks import fetch_crypto_prices

def index(request):
    # here I can receive coins even after the page finished loading !!!!
    #url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=7&page=1&sparkline=false"
    #coins = requests.get(url).json()
    return render(request, "index.html")
