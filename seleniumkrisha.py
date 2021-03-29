from selenium import webdriver
import time
import csv

class Parsing:
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def ParsingData(self):
        url = 'https://krisha.kz/content/analytics'
        self.driver.get(url)

        history = self.driver.find_elements_by_xpath("//*[contains(text(), 'Вся история')]")
        for h in history:
            h.click()
        time.sleep(5)

        rects = self.driver.find_elements_by_class_name("c3-event-rect")
        self.results = ['data;currency;usdpercent;usd;tngpercent;tng']
        for rect in rects[1:]:
            action = webdriver.ActionChains(self.driver)
            action.move_to_element(rect).perform()
            time.sleep(1)
            currency = self.driver.find_elements_by_class_name("customTooltip")[0].text
            self.results.append(currency)


        print('OK')
        self.driver.close()
    
    def to_txt(self, path):
        with open(path, 'a', encoding='utf8') as f:
            for line in self.results:
                f.write(line.replace('\n', ';').replace('% ', '%;') + '\n')
        

if __name__ == "__main__":
    start = time.time()
    parse = Parsing()
    parse.ParsingData()
    parse.to_txt('result27.csv')
    print('sec:', time.time() - start)