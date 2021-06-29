
import twstock,time,requests

def send_ifttt(v1,v2,v3):
    url=f'https://maker.ifttt.com/trigger/stock/with/key/2fbtnnMpurfqdvY4yn8PN?value1=名稱:{str(v1)}現價：{str(v2)}&value2={str(v3)}&value3={str(v4)}'
    #print(url)
    r=requests.get(url)
    

def get_price(stockid):
    rt= twstock.realtime.get(stockid)
    if rt['success']:
        return(rt['info']['name'],float(rt['realtime']['latest_trade_price']))
    else:
        return(False,False)
def get_best(stockid):
    stock=twstock.Stock(stockid)
    bp = twstock.BestFourPoint(stock)
    if bp != None:
        if bp.best_four_point()[0] == True:
            return('買進',bp.best_four_point()[1])
        else:
            return('賣出',bp.best_four_point()[1])
    else:
        return(False,False)
v1,v2=get_price('1325')
v3,v4=get_best('1325')
send_ifttt(v1,v2,v3)

#print(name,price,act,why,sep="|")

