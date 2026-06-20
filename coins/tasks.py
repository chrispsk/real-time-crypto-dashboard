from __future__ import absolute_import, unicode_literals
import random
from celery import shared_task
import json
import requests
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Coin

channel_layer = get_channel_layer()

@shared_task(name="fetch_crypto_prices")
def fetch_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=7&page=1&sparkline=false'
    response = requests.get(url).json()
    coins = list()

    for co in response:
        # try:
        #     obj = Coin.objects.get(name=co["id"])
        # except Coin.DoesNotExist: # this is for the first time
        #     obj = Coin(name=co['id'], price=co['current_price'])
        #     obj.save()
        obj, created = Coin.objects.get_or_create(name=co["id"])
        # I got an instance of Coin (obj) and now I want to fill it
        # with the data I got from API
        
        obj.name = co['id']
        obj.image = co['image']
        if obj.price > co['current_price']:
            state = 'fall'
        elif obj.price == co['current_price']:
            state = 'same'
        else:
            state = 'raise'
        obj.price = co['current_price']
        obj.save()
        
        coins.append({'id': obj.id, 'image': obj.image, 'name': obj.name, 'price': obj.price, 'state': state})       
    #print(coins)
    # Channel_layer is an async function.
    async_to_sync(channel_layer.group_send)('coins', {'type':'send_new_data', 'text':coins})
    #return joke
