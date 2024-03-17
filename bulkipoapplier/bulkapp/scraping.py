from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import os
# disable logging for webdriver
os.environ['WDM_LOG_LEVEL'] = '0'

class web_driver():  
    #django set options for webdriver

    # function that calls and runs the webdriver
    def open_browser(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.headless = False # run in background
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920x1080')
        # add user agent
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36')
        options.add_argument("--start-maximized")

        # drivermanager automatically installs latest driver and set path to that driver
        #chrome_driver_path = ChromeDriverManager(version="114.0.5735.90").install()        # call drivermanager according to browser you use
        # function that calls and runs the webdriver
        self.driver= webdriver.Chrome(options=options)        
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get("https://meroshare.cdsc.com.np/#/login")  # Open the Meroshare Login Page
        self.driver.implicitly_wait(10)
        

        
 

def login(dp,username,password):
    web_driver.wait.until(EC.presence_of_element_located((By.TAG_NAME, "app-login")))
    # Login
    web_driver.wait.until(EC.presence_of_element_located((By.NAME, "selectBranch")))
    web_driver.driver.find_element(By.NAME ,"selectBranch").click()
    dpEntry = web_driver.driver.find_element(By.CLASS_NAME, "select2-search__field")   # Find the Dp Entry Box
    dpEntry.click()  # Click on the Dp Entry Box
    dpEntry.send_keys(dp)  # Enter the Dp Id
    dpEntry.send_keys(Keys.ENTER)  # Press Enter
    #send keys one by one
    web_driver.driver.find_element(By.NAME ,"username").send_keys(username)
    web_driver.driver.find_element(By.NAME ,"password").send_keys(password)
    web_driver.driver.find_element(By.CLASS_NAME ,"sign-in").click()


def goto_asba():
    web_driver.wait.until(EC.presence_of_element_located((By.TAG_NAME, "app-dashboard")))
    web_driver.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='sideBar']/nav/ul/li[8]/a/span")))
    web_driver.driver.find_element(By.XPATH,"//*[@id='sideBar']/nav/ul/li[8]/a/span").click()
    web_driver.wait.until(EC.url_to_be("https://meroshare.cdsc.com.np/#/asba"))  # Wait until the page url changes to the asba page

def open_ipo_lister():
    ipolist = []
    try:
        web_driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div')))
        web_driver.wait.until(EC.presence_of_element_located((By.TAG_NAME, "app-applicable-issue")))
        web_driver.driver.implicitly_wait(1)
        IPOlist = web_driver.driver.find_elements(By.CLASS_NAME,"company-name")
        
        for i in IPOlist:
            ipolist.append(i.text)
        return ipolist
    except Exception as e:
        ipolist.append("No IPO are available.")
        return ipolist

def ipo_selector(ind=''):
    if (ind == 0):
        iposelector_index = ''
    else:
        iposelector_index = '[{}]'.format(ind)

    apply_btn = web_driver.driver.find_element(By.XPATH,'//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div' + str(iposelector_index) +'/div/div[2]/div/div[4]/button')
    apply_btn.click()
    bank_selector()



def bank_selector():
     # wait until the page url changes to other than asba page
    web_driver.wait.until_not(EC.url_to_be("https://meroshare.cdsc.com.np/#/asba"))
    # select and click element with name selectBank and click on it
    bank_dropdown = Select(web_driver.driver.find_element(By.XPATH,"//*[@name='selectBank']"))
    bank_list = bank_dropdown.options
    print(bank_list)
    if len(bank_list) > 2: 
        selected_bank = 3
        web_driver.driver.find_element(By.XPATH,"//*[@id='selectBank']/option[" + str(selected_bank) + "]").click()
    else:
        web_driver.driver.find_element(By.XPATH,"//*[@id='selectBank']/option[2]").click()


        
def applySuccess(qty,crn,pin):
    appliedKitta = web_driver.driver.find_element(By.NAME,"appliedKitta")
    appliedKitta.send_keys(qty)
    crninput = web_driver.driver.find_element(By.NAME,"crnNumber")
    crninput.send_keys(crn)

    web_driver.driver.find_element(By.NAME,"disclaimer").click()

    # submit the form
    submit = web_driver.driver.find_element(By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]")
    web_driver.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]")))
    submit.click()
    web_driver.wait.until(EC.presence_of_element_located((By.NAME,"transactionPIN")))

    web_driver.driver.find_element(By.NAME,"transactionPIN").send_keys(pin)
    pin_submit = web_driver.driver.find_element(By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]")
    web_driver.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]")))
    pin_submit.click()
    sleep(1)
    close_browser()

     
def close_browser():
    web_driver.driver.quit()
