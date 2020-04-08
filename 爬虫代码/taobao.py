import requests
import re

headers = {'cookie':'cna=Fv/jFoOluxECATplmMTVR8bD; thw=cn; tracknick=t_1529830471331_096; tg=0; enc=Q1InB%2BF4YDIv0VGoeyy5Ja711k1yEWzrdx2SUQ%2BiIqhrxR6hn9eSgU%2BeZWvwQHLlOQ1ay2cf7EtIzkRGdRWIlg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; miid=243649131559951258; t=5a793a6faf64300220f174d1494464b1; v=0; cookie2=1b602f3772af21d365a37aa5dc6d849a; _tb_token_=f8eb6e6fadab5; _samesite_flag_=true; tfstk=cnTFB06QR23Elq1eJZbPO83PmeddZGsl0P5RxnWl7QOtH9ShiqeRsfwR_sBxSMf..; unb=3806302020; uc3=nk2=F6k3HS5JGhskNPxkESEVkzmlAA%3D%3D&vt3=F8dBxdAbD%2FDL2utOlkQ%3D&lg2=UtASsssmOIJ0bQ%3D%3D&id2=UNiE5GfaKOVrWg%3D%3D; csg=a4b39962; lgc=t_1529830471331_096; cookie17=UNiE5GfaKOVrWg%3D%3D; dnk=t_1529830471331_096; skt=4192678916bcd81d; existShop=MTU4NjMyMTQ4Mg%3D%3D; uc4=nk4=0%40FbMocxv6V1LquIDl4Nwe9zjDjyQhrNK6WoOBoFqC&id4=0%40Ug%2BbULoEf9miPB%2FODOVzSJQEndT4; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=602; _nk_=t_1529830471331_096; cookie1=BxUFpzd0E1sMLCZfP%2FMnH3s%2B1vICqTIJdluuu6uXvD4%3D; mt=ci=10_1; uc1=cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&lng=zh_CN&existShop=false&cookie14=UoTUPOdMwHRjLQ%3D%3D&pas=0&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie21=UIHiLt3xThH8t7YQoFNq; isg=BIOD9liU2WccCJV6HCs96LWAEkct-Bc6rw0XBrVg3-JZdKOWPcinimHm7gQ6T28y; l=dBTUtcVgQJgS1BFLBOCanurza77OSIRYYuPzaNbMi_5Ig6T_iVbOo69x5F96VjWf9lYB4sc4x1v9-etkZQDmndK-g3fPaxDc.',

          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'}#考虑到淘宝的反爬,需要修改requests.get()方法中控制访问的参数headers

def getHTMLText(url):
    try:
        r = requests.get(url,headers = headers, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    

def parsePage(html,output_path):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?"',html)
        slt = re.findall(r'\"view_sales\"\:\".*?"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            sell = eval(slt[i].split(':')[1])
            with open(output_path,'a', encoding = 'utf-8') as f:
                f.write(title+';'+price+';'+sell+ '\n')
    except:
        print("")


    
def main():
    goods = '图书'
    depth = 5
    start_url = 'https://s.taobao.com/search?q=' + goods
    output_path = 'C:/Users/10530/Desktop/爬/datastruct/datastruct_tbbooks.txt'
    with open(output_path,'a', encoding = 'utf-8') as f:
        f.write('商品名称;商品价格;商品销量'+ '\n')
    count = 0
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(html,output_path)
            count = count + 1
            print("\r当前任务已经完成:{:.2f}%".format(count*100/depth),end="")
        except:
            count = count + 1
            print("\r当前任务已经完成:{:.2f}%".format(count*100/depth),end="")
            continue
    
main()