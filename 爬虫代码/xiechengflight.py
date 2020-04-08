import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'}
        r = requests.get(url = url, headers = header, timeout = 30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getFlightCatalog(url):
    flightCatalog = {}
    html = getHTMLText(url)
    soup = BeautifulSoup(html,'html.parser')
    letter_list = soup.find(attrs = {'class':'letter_list'}).find_all('li')
    for li in letter_list:
        try:
            for a in li.find_all('a')[:1]:
                flightCatalog[a.get_text()] = url + a['href'][9:]
        except:
            continue
    
    return flightCatalog
        
def getFlightLine(url):
    flightLine = {}
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')
    letter_list = soup.find(attrs = {'id': 'ulD_Domestic'}).find_all('li')
    for li in letter_list:
        try:
            for a in li.find_all('a'):
                flightLine[a.get_text()] = a['href']    
        except:
            continue
    return flightLine

def parseFlightMessage(url,fpath):
    html = getHTMLText(url)
    soup = BeautifulSoup(html,'html.parser')
    flight_Detail = soup.find(attrs = {'id': 'flt1'}).find_all('tr')
    info = []
    for tr in flight_Detail:
        try:
            flight_td = tr.find_all('td')
            flight_no = flight_td[0].find('strong').get_text().strip()
            flight_stime = flight_td[1].find('strong').get_text().strip()
            flight_sairport = flight_td[1].find('div').get_text().strip()
            flight_etime = flight_td[3].find('strong').get_text().strip()
            flight_eairport = flight_td[3].find('div').get_text().strip()
            flight_punrate = flight_td[5].get_text().strip()
            flight_price = flight_td[6].get_text().strip().replace('¥','')
            if(flight_price == "查看时价"):
                continue
            with open(fpath,'a', encoding = 'utf-8') as f:
                f.write(flight_no+';'+flight_stime+';'+flight_sairport+';'+flight_etime+';'+flight_eairport+';'+flight_punrate+';'+flight_price+'\n')
        except:
            continue
    
    
    

def main():
    url = 'https://flights.ctrip.com/schedule'
    output_path = 'C:/Users/10530/Desktop/爬/datastruct/datastruct_xcflight.txt'
    with open(output_path,'a', encoding = 'utf-8') as f:
        f.write('航班号;起飞时间;起飞机场;降落时间;降落机场;准点率;机票价格(¥)'+ '\n')
    allFlight = getFlightCatalog(url)
    count = 0
    for key in allFlight.keys():
        try:
            allLine = getFlightLine(allFlight[key])
            for line in allLine.keys():
                    parseFlightMessage(allLine[line],output_path)
                    
            count = count + 1
            print("\r当前任务已经完成:{:.2f}%".format(count*100/len(allFlight)),end="")       
        except:
            count = count + 1
            print("\r当前任务已经完成:{:.2f}%".format(count*100/len(allFlight)),end="")
            continue
  
main() 