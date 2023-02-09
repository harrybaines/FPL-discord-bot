from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

POSITIONS = ['GK', 'DEF', 'MID', 'FWD', 'SUB']

options = Options()
options.add_argument("window-size=1980,960")
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')        

def get_fpl_scout_team():
    options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    driver = webdriver.Chrome(executable_path=str(os.environ.get('CHROMEDRIVER_PATH')), options=options)
 
    url = 'https://www.fantasyfootballscout.co.uk/'
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(220)

    element = driver.find_element('xpath', '//*[@id="ffsscoutpickswidget-3"]/div')
    rows = element.find_elements(By.TAG_NAME, "ul")

    scout_picks_content = element.text.split('\n')
    title = scout_picks_content[0].title()
    gw = scout_picks_content[1]
    team_str = ''

    for pos, row in zip(POSITIONS, rows):
        players = row.text.split('\n')
        for player in players:
            team_str += f'{pos}: {player.title()}\n'
        team_str += '\n'

    output_str = f'{gw} {title}\n\n{team_str}'
    return output_str
