from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://10fastfingers.com/typing-test/english")
sleep(2)
driver.find_element_by_xpath(
    '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
sleep(5)
driver.find_element_by_xpath(
    '//*[@id="fs-slot-footer-wrapper"]/button').click()

def get_word_list():
    wlist = driver.find_element_by_id("wordlist").get_attribute("innerHTML")
    return wlist.split('|')

def type_words(box, wpm, w_cooldown=0, l_cooldown=0):
    timer = driver.find_element_by_id("timer")
    if l_cooldown > 0:
        i = 0
        while i < wpm and timer.text != "0:00":
            print('typing "' + wlist[i] + '"...')
            for key in wlist[i]:
                box.send_keys(key)
                sleep(l_cooldown)
            box.send_keys(Keys.SPACE)
            i += 1
            sleep(w_cooldown)
    else:
        i = 0
        while i < wpm and timer.text != "0:00":
            print('typing "' + wlist[i] + '"...')
            box.send_keys(wlist[i])
            box.send_keys(Keys.SPACE)
            i += 1
            sleep(w_cooldown)

input_box = driver.find_element_by_xpath('//*[@id="inputfield"]')
input_box.click()
sleep(10)
wlist = get_word_list()
type_words(input_box, len(wlist))

print("end")