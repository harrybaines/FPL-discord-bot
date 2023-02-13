from selenium import webdriver
from selenium.webdriver.chrome.options import Options

POSITIONS = ['GK', 'DEF', 'MID', 'FWD', 'SUB']
GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

options = Options()
options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})
options.add_argument("window-size=1980,960")
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')        

def get_fpl_scout_team():
    driver = webdriver.Chrome(options=options)
 
    url = 'https://www.fantasyfootballscout.co.uk/'
    driver.maximize_window()
    driver.get(url)

    privacy_notice_btn = driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[2]/div/button[2]')
    privacy_notice_btn.click()
    
    team_div = driver.find_element('xpath', '//*[@id="ffsscoutpickswidget-3"]/div')
    return team_div.screenshot_as_png