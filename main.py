from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path="/home/yura/PycharmProjects/pythonProject3/geckodriver")

browser.get('https://www.ncbi.nlm.nih.gov/assembly/GCF_000970305.1')

browser.find_element_by_id('download-asm').click()

browser.find_element_by_id('dl_assembly_download').click()





