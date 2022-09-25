# from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

if __name__ == "__main__":
    website = 'https://www.makemycocktail.com/?#HowToMakeACocktail'
    # DRIVER_PATH = '/Applications/chromedriver'
    driver = uc.Chrome()
    # driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(website)

    # driver.implicitly_wait(10)
    # age_verification_button = driver.find_elements_by_xpath('//input[@onclick="ageVerification_yes()"]')
    age_verification_button = driver.find_element("xpath", '//input[@onclick="ageVerification_yes()"]')
    age_verification_button.click()
    # driver.execute_script("return arguments[0].click();", age_verification_button)
    # driver.quit()
    user_selection = ['Brandy', 'Rum', 'Tequila', 'Vodka', 'Whiskey', 'Almond Liquer']
    brandy = 'Brandy'
    gin = 'Gin'
    rum = 'Rum'
    tequila = 'Tequila'
    vodka = 'Vodka'
    whiskey = 'Whiskey'
    almondliqueur = 'Almond Liquer'
    if brandy in user_selection:
        brandy_check = driver.find_element(By.ID,'brandy_checkbox')
        brandy_check.click()
    if gin in user_selection:
        gin_check = driver.find_element(By.ID,'gin_checkbox')
        gin_check.click()
    if rum in user_selection:
        rum_check = driver.find_element(By.ID,'rum_checkbox')
        rum_check.click()
    if tequila in user_selection:
        tequila_check = driver.find_element(By.ID,'tequila_checkbox')
        tequila_check.click()
    if vodka in user_selection:
        vodka_check = driver.find_element(By.ID,'vodka_checkbox')
        vodka_check.click()
    if whiskey in user_selection:
        whiskey_check = driver.find_element(By.ID,'whiskey_checkbox')
        whiskey_check.click()
    if almondliqueur in user_selection:
        almondliqueur_check = driver.find_element(By.ID,'almondliqueur_checkbox')
        almondliqueur_check.click()
#     if cherryliqueur in user_selection:
#         cherryliqueur_check = driver.find_element(By.ID,'cherryliqueur_checkbox')
#         cherryliqueur_check.click()
#     if chocolateliqueur in user_selection:
#         chocolateliqueur_check = driver.find_element(By.ID,'chocolateliqueur_checkbox')
#         chocolateliqueur_check.click()
#     if coffeeliqueur in user_selection:
#         coffeeliqueur_check = driver.find_element(By.ID,'coffeeliqueur_checkbox')
#         coffeeliqueur_check.click()
#     if in user_selection:
#         _check = driver.find_element(By.ID,'_checkbox')
#         _check.click()
#     if in user_selection:
#         _check = driver.find_element(By.ID,'_checkbox')
#         _check.click()
#     if in user_selection:
#         _check = driver.find_element(By.ID,'_checkbox')
#         _check.click()
#     if in user_selection:
#         _check = driver.find_element(By.ID,'_checkbox')
#         _check.click()
#     if in user_selection:
#         _check = driver.find_element(By.ID,'_checkbox')
#         _check.click()
# gin rum tequila vodka whiskey
# import undetected_chromedriver as uc
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# if __name__ == '__main__':
#     email = "#"
#     password = "#"

#     options = webdriver.ChromeOptions()
#     #options.add_argument('proxy-server=106.122.8.54:3128')
#     #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')

#     browser = uc.Chrome(
#         options=options,
#     )
#     browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

#     browser.find_element(By.ID, 'identifierId').send_keys(email)

#     browser.find_element(
#         By.CSS_SELECTOR, '#identifierNext > div > button > span').click()

#     password_selector = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"

#     WebDriverWait(browser, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector)))

#     browser.find_element(
#         By.CSS_SELECTOR, password_selector).send_keys(password)

#     browser.find_element(
#         By.CSS_SELECTOR, '#passwordNext > div > button > span').click()