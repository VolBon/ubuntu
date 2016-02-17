from selenium import webdriver
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("params.ini")
lst = Config.items('Section1')

def page_clicker(param):
    output = ''
    driver = webdriver.Firefox()
    driver.get("http://www.ted.com/")
    for key, path in param:
        try:
            inputElement = driver.find_element_by_xpath(path)
        except:
            print path
        else:
            inputElement.click()
            driver.save_screenshot(key+'.png')
            output += '''\n<br><p3>'''+driver.title+'''<br>'''
            output += '''\n<br><img src="'''+key+'''.png"><br>'''
    driver.close()
    return output

def main():
    Html_file= open("log.html","w")
    Html_file.write('''<html>
            <body>''')
    output = page_clicker(lst)
    Html_file.write(output)
    Html_file.write('''</body>
        </html>''')
    Html_file.close()

if __name__ == "__main__":
    main()