import requests
from lxml import etree

header = {'cookie':'thw=cn; v=0; t=ab66dffdedcb481f77fd563809639584; cookie2=1f14e41c704ef58f8b66ff509d0d122e; _tb_token_=5e6bed8635536; cna=fGOnFZvieDECAXWIVi96eKju; unb=1864721683; sg=%E4%B8%8B3f; _l_g_=Ug%3D%3D; skt=83871ef3b7a49a0f; cookie1=BqeGegkL%2BLUif2jpoUcc6t6Ogy0RFtJuYXR4VHB7W0A%3D; csg=3f233d33; uc3=vt3=F8dBy3%2F50cpZbAursCI%3D&id2=UondEBnuqeCnfA%3D%3D&nk2=u%2F5wdRaOPk21wDx%2F&lg2=VFC%2FuZ9ayeYq2g%3D%3D; existShop=MTU2MjUyMzkyMw%3D%3D; tracknick=%5Cu4E36%5Cu541B%5Cu4E34%5Cu4E3F%5Cu5929%5Cu4E0B; lgc=%5Cu4E36%5Cu541B%5Cu4E34%5Cu4E3F%5Cu5929%5Cu4E0B; _cc_=WqG3DMC9EA%3D%3D; dnk=%5Cu4E36%5Cu541B%5Cu4E34%5Cu4E3F%5Cu5929%5Cu4E0B; _nk_=%5Cu4E36%5Cu541B%5Cu4E34%5Cu4E3F%5Cu5929%5Cu4E0B; cookie17=UondEBnuqeCnfA%3D%3D; tg=0; enc=2GbbFv3joWCJmxVZNFLPuxUUDA7QTpES2D5NF0D6T1EIvSUqKbx15CNrsn7nR9g%2Fz8gPUYbZEI95bhHG8M9pwA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=32_1; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; swfstore=97213; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=UIHiLt3xThH8t7YQouiW&cookie15=URm48syIIVrSKA%3D%3D&existShop=false&pas=0&cookie14=UoTaGqj%2FcX1yKw%3D%3D&tag=8&lng=zh_CN; JSESSIONID=A502D8EDDCE7B58F15F170380A767027; isg=BMnJJFqj8FrUHowu4yKyNXcd2PXjvpa98f4aQWs-RbDvsunEs2bNGLfj8BYE6lWA; l=cBTDZx2mqxnxDRr0BOCanurza77OSIRYYuPzaNbMi_5dd6T114_OkmrjfF96VjWdO2LB4G2npwJ9-etkZ1QoqpJRWkvP.; whl=-1%260%260%261562528831082',

          'user-agent':'Mozilla/5.0'}

    
def parsePage(url,fpath):
    rsp = requests.get(url=url, headers=header).content.decode()
    rsp = etree.HTML(rsp)
    items = rsp.xpath('//li[contains(@class, "gl-item")]')
    info = []
    for item in items:
        try:
            title = ''.join(item.xpath('.//div[@class="p-name p-name-type-2"]//em//text()'))
            url = 'https:' + item.xpath('.//div[@class="p-name p-name-type-2"]/a/@href')[0]
            store = item.xpath('.//div[@class="p-shop"]/span/a/text()')[0]
            store_url = 'https' + item.xpath('.//div[@class="p-shop"]/span/a/@href')[0]
            item_id = url.split('/')[-1][:-5]
            price = item.xpath('.//div[@class="p-price"]//i/text()')[0]
            info.append([title,url,store,store_url,item_id,price])
            
        except:
            continue
    for ele in info:
        with open(fpath,'a', encoding = 'utf-8') as f:
            f.write(ele[0]+';'+ele[1]+';'+ele[2]+';'+ele[3]+';'+ele[4]+';'+ele[5]+';'+ '\n')
    



def main():
    start_url = 'https://search.jd.com/Search?keyword=显卡&enc=utf-8&page=' 
    output_file = 'C:/Users/10530/Desktop/爬/datastruct/datastruct_jdVGA.txt'
    depth = 200
    count = 0
    with open(output_file,'a', encoding = 'utf-8') as f:
            f.write('商品标题;商品链接;店铺名称;店铺链接;商品id;商品价格'+ '\n')
    for i in range(depth):
        try:
            url = start_url + str(1 + i * 2)
            parsePage(url,output_file)
            count = count + 1
            print("\r当前任务已经完成:{:.2f}%".format(count*100/depth),end="")
        except:
            count = count + 1
            print("\r当前任务已经完成:{:.2f}%".format(count*100/depth),end="")
            continue

main()