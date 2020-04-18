from conf import UNAME,PASS
from selenium import webdriver
import time

browser = webdriver.Chrome()

url = 'https://www.instagram.com'
browser.get(url)

time.sleep(2)
username = browser.find_element_by_name("username")
username.send_keys(UNAME)

time.sleep(2)
password = browser.find_element_by_name("password")
password.send_keys(PASS)

time.sleep(1.5)
login_btn = browser.find_element_by_css_selector("button[type='submit']")
login_btn.click()

time.sleep(2)
sele_btn = browser.find_element_by_xpath("//*[contains(text(), 'Not Now')]")
sele_btn.click()

time.sleep(2)
seeAll_btn = browser.find_element_by_xpath('//a[contains(text(), "See All")]')
seeAll_btn.click()

def clickToFollow(browser):
    follow_btns = browser.find_elements_by_xpath("//button[contains(text(), 'Follow')][not(contains(text(), 'Following'))]")
    for btn in follow_btns:
        time.sleep(2)
        try:
            btn.click()
        except:
            pass

# for _ in range(5):
# clickToFollow(browser)

def unfollow(browser):
    profile_btn = browser.find_element_by_xpath("//a[contains(@href, '/smithanderson019/')]")
    profile_btn.click()
    time.sleep(2)
    following_btn = browser.find_element_by_xpath("//a[contains(@href, '/smithanderson019/following')]")
    following_btn.click()
    time.sleep(2)
    unfollow_btns = browser.find_elements_by_xpath("//button[contains(text(), 'Following')]")
    # unfollow_btns = browser.find_elements_by_link_text("Following")
    # time.sleep(2)
    # unfollow_btns[0].click()
    for btn in unfollow_btns:
        time.sleep(2)
        try:
            btn.click()
            time.sleep(2)
            conf_btn = browser.find_element_by_xpath("//*[contains(text(), 'Unfollow')]")
            time.sleep(1.5)
            conf_btn.click()
        except:
            pass

unfollow(browser)