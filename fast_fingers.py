from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class TypingBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://10fastfingers.com/typing-test/english")

    def initialize(self):
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="fs-slot-footer-wrapper"]/button').click()

    def get_word_list(self):
        wlist = self.driver.find_element_by_id("wordlist").get_attribute("innerHTML")
        return wlist.split('|')

    def type_words(self, wpm, w_cooldown=0, l_cooldown=0):
        box = self.driver.find_element_by_xpath('//*[@id="inputfield"]')
        box.click()
        wlist = self.get_word_list()
        timer = self.driver.find_element_by_id("timer")
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
                
if __name__ == "__main__":
    bot = TypingBot()
    bot.initialize()
    wlist = bot.get_word_list()
    input("Press any key...")
    bot.type_words(len(wlist))
    print("end")