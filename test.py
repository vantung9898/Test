import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def google_search(domain, keyword): 
    keyword = '''site:%s "%s"''' % (domain, keyword) 

    search_string = keyword.replace(' ', '+') 
    service_obj = Service()
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=service_obj)  
    driver.get("https://www.google.com/search?q=" + search_string + "&start=" + str(1))
    #driver.get("https://github.com/search?q=hGvVGsb9XA7EoWVkW5EJKotMUC8368JY%09&type=repositories")
        
    time.sleep(2)

    height = driver.execute_script('return document.documentElement.scrollHeight')
    width  = driver.execute_script('return document.documentElement.scrollWidth')
    driver.set_window_size(height, width)

    time.sleep(2)
    driver.save_screenshot("screenshot_%s.png" % (keyword))
    # TODO: inspect elements. 

    driver.quit()

if __name__ == "__main__":
    domains = ["github.com", 
               "bitbucket.org"]
    keywords = ["struct sbp2_pointer command_block_agent"]

    for domain in domains:
        for keyword in keywords:
            google_search(domain, keyword)