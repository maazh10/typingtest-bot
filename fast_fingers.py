from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import constants

# main bot class
class TypingBot:
    def __init__(self):
        # neglect warnings and certificate errors to clean up terminal
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # initialize chrome driver
        self.driver = webdriver.Chrome(options=options)
        # navigate to 10fastfingers
        self.driver.get("https://10fastfingers.com/typing-test/english")

    # set window size, close all popups 
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

    # grab the word list from inner HTML
    def get_word_list(self):
        wlist = self.driver.find_element_by_id("wordlist").get_attribute("innerHTML")
        return wlist.split('|')

    def type_words(self, wpm, w_cooldown=0, l_cooldown=0):
        # find and click the input box
        box = self.driver.find_element_by_xpath('//*[@id="inputfield"]')
        box.click()
        # get word list and find the timer
        wlist = self.get_word_list()
        timer = self.driver.find_element_by_id("timer")
        # if theres no letter cooldown input full words 
        if l_cooldown > 0:
            i = 0
            # continue typing till the we reach the total number of words given by user or timer hits 0
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

    print("\n... LOADING ...")

    # initialize bot object
    bot = TypingBot()
    bot.initialize()
    wlist = bot.get_word_list()

    # intialize type_words() parameters
    words = len(wlist)
    wc = 0
    lc = 0

    # MENU
    print("\n-------- PICK A MODE --------")
    print("1 - Very Slow")
    print("2 - Slow")
    print("3 - Medium")
    print("4 - Fast")
    print("5 - Very Fast")
    print("6 - Ultra")
    print("7 - Custom")
    print("8 - Exit")
    res = ""
    res = input("Enter your choice (1-8): ")
    while res not in "12345678":
        res = input("Please enter a valid choice (1-8): ")

    if res == "1":
        print("\n-------- MODE: VERY SLOW --------")
        lc = constants.VS_LC
        wc = constants.VS_WC
    elif res == "2":
        print("\n-------- MODE: SLOW --------")
        lc = constants.S_LC
        wc = constants.S_WC
    elif res == "3":
        print("\n-------- MODE: MEDIUM --------")
        lc = constants.M_LC
        wc = constants.M_WC
    elif res == "4":
        print("\n-------- MODE: FAST --------")
        lc = constants.F_LC
        wc = constants.F_WC
    elif res == "5":
        print("\n-------- MODE: VERY FAST --------")
        lc = constants.VF_LC
        wc = constants.VF_WC
    elif res == "6":
        print("\n-------- MODE: ULTRA --------")
        lc = constants.U_LC
        wc = constants.U_WC
    elif res == "7":
        print("\n-------- MODE: CUSTOM --------")
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
    elif res == "8":
        bot.driver.close()
        exit()

    # begin the test with given arguements
    input("\nPress any key to begin...")
    bot.type_words(words, wc, lc)

    print("\n-------- END --------")
