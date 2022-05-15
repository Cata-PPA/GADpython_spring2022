from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime
def scoate_diacritice(string):
    string = string.replace('î', 'i')
    string = string.replace('â', 'a')
    string = string.replace('ă', 'a')
    string = string.replace('ș', 's')
    string = string.replace('ț', 't')
    return string


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/')
header = [browser.find_element(by=By.XPATH, value=f'//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]/td[{int(i)}]'
                               ).text for i in range(1, 6)]
for i in range(0, len(header)):
    header[i] = scoate_diacritice(header[i])
header.append('Data')

dictionar = {i: [] for i in header}
dictionar['Data'] = []
lungime_anterioara = 0
for zi in range(20, 27):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{zi}-ianuarie-ora-13-00/')
    table = [browser.find_element(by=By.XPATH, value=f'//*/div/div/table[1]/tbody/tr[{int(i)}]')
             .text for i in range(2, 44)]
    for i in range(0, len(table)):
        table[i] = scoate_diacritice(table[i])
    for i in range(0, len(table)):
        table[i] = table[i].split(' ')
    for i in range(0, len(table)):
        for j in range(0, len(header)):
            if header[j] != 'Data' and i != 31 and i != 41:
                dictionar[header[j]].append(table[i][j])

        if i != 31 and i != 41:
            dictionar['Data'].append(datetime.datetime.strptime(f'{zi}012022', '%d%m%Y'))# ValueError("All arrays must be of the same length")
    browser.close()

# for key, value in dictionar.items():
#     print(key, len(list(filter(bool, value))))
df = pd.DataFrame(dictionar)
df.to_csv('text.xls')
