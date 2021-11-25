class crypto():
    crypto_to_check='bitcoin,' \
    'ethereum,ethereum-classic,ergo' \
    ',litecoin,binancecoin,solana,' \
    'cardano,ripple,polkadot' \
    ',dogecoin,shiba-inu,terra-luna,' \
    'monero,zcash,ravencoin,beam,raptoreum'
    status_online_api = '(V3) To the Moon!'
    def __init__(self):
        self.url_api = 'https://api.coingecko.com/api/v3/'


    def check_api_status(self,url='ping',gecko='gecko_says'):
        from requests import get
        from json import dumps,loads
        try:
            resp=get(url=self.url_api+url).json()
            to_json = dumps(resp)
            parse = loads(to_json)
            return parse[gecko]
        except ConnectionError:
            print('Problem with connect to the api')
        except TimeoutError:
            print('Timeout')
        except Exception as e:
            print(str(e))

    def get_current_price(self,url,ids,vs_currencies,include_market_cap=False,include_24hr_vol=False,include_24hr_change=False,include_last_updated_at=False):
        from requests import get
        from json import loads,dumps
        try:
            resp =get(url=self.url_api+url+'?ids='+ids+'&vs_currencies='+vs_currencies+'&include_market_cap='+include_market_cap+'&include_24hr_vol='+include_24hr_vol+'&include_24hr_change='+include_24hr_change+'&include_last_updated_at='+include_last_updated_at).json()
            to_json = dumps(resp)
            parse = loads(to_json)
            return parse
        except ConnectionError:
            print('Problem with connect to the api')
        except TimeoutError:
            print('Timeout')
        except Exception as e:
            print(str(e))

    def top_trending_coins(self,url='search/trending'):
        from requests import get
        from json import loads, dumps

        try:
            resp = get(url=self.url_api+url).json()
            to_json = dumps(resp)
            parse = loads(to_json)
            return parse
        except ConnectionError:
            print('Problem with connect to the api')
        except TimeoutError:
            print('Timeout')
        except Exception:
            print(str(e))

    @staticmethod
    def main():
        from json import dumps,loads
        try:
            c = crypto()
            cryptocurrency = c.get_current_price(url='simple/price', ids=c.crypto_to_check, vs_currencies='pln',
                                                 include_market_cap='true', include_24hr_vol='true',
                                                 include_24hr_change='true',
                                                 include_last_updated_at='true')
            top_crypto = c.top_trending_coins()
            print(
                '=============================================== TOP 7 Trending Coins ============================================================')
            [print(i + 1, '.', 'id: ', top_crypto['coins'][i]['item']['id'], 'name: ',
                   top_crypto['coins'][i]['item']['name'], 'btc: ', top_crypto['coins'][i]['item']['price_btc'])
             for i in range(7)]
            print(
                '=================================================================================================================================')
            print(
                '===============================================  Coins worth buying  ============================================================')
            [print(i, ':', cryptocurrency[i]['pln'], ' zł')
             if cryptocurrency[i]['pln_24h_change'] < (-1)
             else None
             for i in c.crypto_to_check.split(',')
             ]
            print('=================================================================================================================================')
        except Exception as e:
            print(str(e))


if __name__=='__main__':
    c = crypto()
    from time import sleep
    from datetime import datetime
    while c.check_api_status() in c.status_online_api:
        print('Time: ',datetime.now())
        c.main()
        [sleep(i)
         for i in range(300)]
