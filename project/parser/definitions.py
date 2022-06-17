import time

def change_url(driver, url):
    try:
        driver.get(url)
        driver.implicitly_wait(10)
        time.sleep(5)
    except:
        pass


def space_rep(string):
    try:
        nonBreakSpace = u'\xa0'
        string = string.replace(nonBreakSpace, '')
        string = string.replace(' ', '')
    except:
        pass
    finally:
        return string