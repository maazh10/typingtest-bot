from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class TypingBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://10fastfingers.com/typing-test/english")

    def initialize(self):
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
        sleep(5)
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="fs-slot-footer-wrapper"]/button').click()
            self.driver.find_element_by_xpath('//*[@id="Layer_1"]').click()
        except:
            sleep(5)
            self.driver.find_element_by_xpath(
                '//*[@id="fs-slot-footer-wrapper"]/button').click()
            self.driver.find_element_by_xpath('//*[@id="Layer_1"]').click()

    def get_word_list(self):
        wlist = self.driver.find_element_by_id(
            "wordlist").get_attribute("innerHTML")
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

    words = len(wlist)
    wc = 0
    lc = 0

    print("\n--------PICK A MODE--------")
    print("1 - Very Slow")
    print("2 - Slow")
    print("3 - Medium")
    print("4 - Fast")
    print("5 - Very Fast")
    print("6 - Ultra")
    print("7 - Custom")
    res = ""
    res = input("Enter your choice (1-7): ")
    while res not in "1234567":
        res = input("Please enter a valid choice (1-7): ")

    if res == "1":
        print("\n--------MODE: VERY SLOW--------")
        lc = 0.4
        wc = 0.5
    elif res == "2":
        print("\n--------MODE: SLOW--------")
        lc = 0.2
        wc = 0.5
    elif res == "3":
        print("\n--------MODE: MEDIUM--------")
        lc = 0.1
        wc = 0.4
    elif res == "4":
        print("\n--------MODE: FAST--------")
        lc = 0
        wc = 0.2
    elif res == "5":
        print("\n--------MODE: VERY FAST--------")
        lc = 0
        wc = 0.1
    elif res == "6":
        print("\n--------MODE: ULTRA--------")
        lc = 0
        wc = 0
    elif res == "7":
        print("\n--------MODE: CUSTOM--------")
        words = input("Number of words to type [enter max for maximum]: ")
        if words == "max":
            words = len(wlist)
        else:
            words = int(words)
        lc = input("Letter Cooldown [enter min for minimum]: ")
        if lc == "min":
            lc = 0
        else:
            lc = float(lc)
        wc = input("Word Cooldown [enter min for minimum]: ")
        if wc == "min":
            wc = 0
        else:
            wc = float(wc)

    input("\nPress any key to begin...")
    bot.type_words(words, wc, lc)
    print("end")
