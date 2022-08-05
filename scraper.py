from selenium import webdriver
from seleniumwire import webdriver 
from fake_headers import Headers
from urllib.request import urlopen
import urllib.request
import warnings
warnings.filterwarnings("ignore")


driver_option = webdriver.ChromeOptions()
driver_option.add_argument("--incognito")
driver_option.add_argument('--disable-blink-features=AutomationControlled')
chromedriver_path = 'Your chromedriver path'
if __name__ == "__main__":
    header = Headers(
        #browser="chrome",
        #os="win",
        headers=False
    )
def create_webdriver():
 return webdriver.Chrome(executable_path=chromedriver_path, chrome_options=driver_option)

def scrolll():
                scheight = .1
                while scheight < 9.9:
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
                    scheight += .05


browser = create_webdriver()
opener = urllib.request.build_opener()
badstr = ['<', '>', '"', '/', '\\', "|", "?", "*", " ", ",", ".", "'", "_"]
#copy and pase your urls in list below
urls = ['https://www.sheypoor.com/ایران/وسایل-نقلیه/خودرو/نیسان/وانت-زامیاد?o=npy&wi=0']

cname = 0
for url in urls:
        pn = 0
        count = 1
        #color = colors[cname]
        cname += 1
        list = [n for n in range(1, 55)]
        for i in list:
                url = url [:-1] + "1&p=" + str(i)
                browser.get(url)
                carpics = (browser.find_elements_by_xpath("//span[@class='item-image ratio-4-3']"))
                scrolll()
                for car in carpics:
                    try:
                        picurl = (car.find_elements_by_xpath("img")[0].get_attribute('src'))
                        picname = (car.find_elements_by_xpath("img")[0].get_attribute('title'))
                        print(picurl, "\n" ,picname, '=', count)
                        count += 1
                        scrolll()
                        head = header.generate()
                        hdr = head['User-Agent']
                        print("\n", hdr, "\n")
                        opener.addheaders = [('User-agent', ("'"+hdr+"'"))]
                        urllib.request.install_opener(opener)
                        pn += 1
                        urllib.request.urlretrieve(picurl, picname + "-" + str(pn).zfill(4) + ".jpg")
                    except:
                        pn -= 1
                        print("///////////////////////////")
                        pass
browser.quit()