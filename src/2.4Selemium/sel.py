from selenium import webdriver

import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("params.ini")
lst = dict(Config.items('Section1'))
#print lst

# Create a new instance of the Firefox driver and launch the start page
driver = webdriver.Firefox()
driver.get("http://www.tieto.pl/")

#print driver.title

# find the element that's name attribute is q (the google search box)
for key, value in lst.iteritems():
    #print key, value
    try:
        inputElement = driver.find_element_by_xpath(value)
    except:
        print value
        continue
    else:
        inputElement.click()
        driver.save_screenshot(key+'.png')
    driver.execute_script("window.history.go(-1)")

driver.close()
# # type in the search
# inputElement.send_keys("cheese")
#
# # submit the form (although google automatically searches now without submitting)
# inputElement.submit()
#
# try:
#     # we have to wait for the page to refresh, the last thing that seems to be updated is the title
#     WebDriverWait(driver, 10).until(EC.title_contains("cheese"))
#
#     # You should see "cheese! - Google Search"
#     print driver.title
#
# finally:
#     driver.quit()