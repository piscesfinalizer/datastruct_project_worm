import requests
from bs4 import BeautifulSoup
import re
import tushare


def getHTMLText(url,header,code='utf-8'):
    try:
        r = requests.get(url,headers = header)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""


def getStockList(lst, stockURL):
    kv = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }
    html = getHTMLText(stockURL,kv)
    if html != "":
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find_all('td')
        for i in a:
            try:
                code = re.search(r'\d{6}',i.text)
                if code:
                    code = code.group(0).replace(" ","")
                    lst.append(code)            
            except:
                continue
        
    else:
        print("解析失败")
       
    

def getStockInfo(lst, fpath):
    count = 0
    for code in lst:
        try:
            dataNow = tushare.get_realtime_quotes(code)
            name = dataNow.loc[0][0]
            price = float(dataNow.loc[0][3])
            
            with open(fpath, 'a', encoding='utf-8') as f:

                f.write(str(code) +';'+str(name)+';'+str(price)+'\n')
                count = count + 1
                print("\r当前已经完成:{:.2f}%".format(count*100/len(lst)),end="")
        except:
            count = count + 1
            print("\r当前已经完成:{:.2f}%".format(count*100/len(lst)),end="")
            continue


def main():
    stock_list_url = 'https://www.txsec.com/inc1/gpdm.asp'
    output_file = 'C:/Users/10530/Desktop/爬/datastruct/datastruct_stock.txt'
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write('股票代码;股票名称;股票价格'+'\n')
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist,output_file)
 
main()