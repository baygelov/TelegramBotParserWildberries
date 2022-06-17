from selenium.webdriver import ChromeOptions

chromeoptions = ChromeOptions()
# chromeoptions.add_argument('--headless')
chromeoptions.add_argument("window-size=1280,800")
chromeoptions.add_argument('--disable-blink-features=AutomationControlled')
chromeoptions.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.1.985 Yowser/2.5 Safari/537.36")