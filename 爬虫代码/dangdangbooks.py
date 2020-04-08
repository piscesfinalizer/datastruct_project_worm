import requests
from bs4 import BeautifulSoup

def getHTML(url):
    try:
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'}
        r = requests.get(url = url, headers = header, timeout = 30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def parsePage(url,fpath):
    html = getHTML(url)
    soup = BeautifulSoup(html,'html.parser')
    for li in soup.find(attrs = {'class':'bigimg'}).find_all('li'):
        try:
            title = li.find('p',attrs = {'class':'name'}).text
            detail = li.find('p',attrs = {'class':'detail'}).text
            now_price = li.find('span',attrs = {'class':'search_now_price'}).get_text()
            pre_price = li.find('span',attrs = {'class':'search_pre_price'}).get_text()
            discount = li.find('span',attrs = {'class':'search_discount'}).text.replace('\xa0(','').replace(')','')
            author = li.find('p',attrs = {'class':'search_book_author'}).find_all('a')[0].text
            produce = li.find('p',attrs = {'class':'search_book_author'}).find_all('a')[1].text
            press = li.find('p',attrs = {'class':'search_book_author'}).find_all('a')[2].text
            commonts_num = li.find('p',attrs = {'class':'search_star_line'}).text
            with open(fpath,'a', encoding = 'utf-8') as f:
                f.write(title+';'+detail+';'+now_price+';'+pre_price+';'+discount+';'+author+';'+produce+';'+press +';'+commonts_num+ '\n')
        except:
            continue
    
def main():
    goods = '图书'
    depth = 100
    start_url = 'http://search.dangdang.com/?key='+ goods + '&act=input&page_index='
    output_path = 'C:/Users/10530/Desktop/爬/datastruct/datastruct_ddbooks.txt'
    count = 0
    with open(output_path,'a', encoding = 'utf-8') as f:
        f.write('图书标题;图书详情;现价;原价;折扣;作者;出品方;出版社;评论数'+ '\n')
    for i in range(depth):
        try:
            url = start_url + str(i+1) 
            parsePage(url,output_path)
            count = count + 1
            print("\r当前任务已经完成:{:.2f}%".format(count*100/depth),end="")
        except:
            count = count + 1
            print("\r当前任务已经完成:{:.2f}%".format(count*100/depth),end="")
            continue
main()