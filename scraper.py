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
    user_selection = ['Brandy', 'Gin', 'Rum', 'Tequila', 'Vodka', 'Whiskey', 'Almond Liqueur', 'Cherry Liqueur', 'Chocolate Liqueur', 'Coffee Liqueur', 'Coconut Liqueur', 'Irish Cream Liqueur', 'Herbal Liqueur', 'Mint Liqueur', 'Melon Liqueur', 'Orange Liqueur', 'Peach Liqueur', 'Raspberry Liqueur', 'Sloe Liqueur', 'Southern Liqueur', 'Bitters', 'Champagne', 'Dry Vermouth', 'Sweeet Vermouth', 'Cola', 'Ginger Ale', 'Ginger Beer', 'Lemon Lime', 'Soda Water', 'Tonic Water', 'Cranberry Juice', 'Grapefruit Juice', 'Lemon Juice', 'Lime Juice', 'Orange Juice', 'Pineapple Juice', 'Cream', 'Cream of Coconut', 'Grenadine', 'Mint Sprig', 'Simple Syrup']
    brandy = 'Brandy'
    gin = 'Gin'
    rum = 'Rum'
    tequila = 'Tequila'
    vodka = 'Vodka'
    whiskey = 'Whiskey'
    almond = 'Almond Liqueur'
    cherry = 'Cherry Liqueur'
    chocolate = 'Chocolate Liqueur'
    coffee = 'Coffee Liqueur'
    coconut = 'Coconut Liqueur'
    irishcream = 'Irish Cream Liqueur'
    herbal = 'Herbal Liqueur'
    mint = 'Mint Liqueur'
    melon = 'Melon Liqueur'
    orange = 'Orange Liqueur'
    peach = 'Peach Liqueur'
    raspberry = 'Raspberry Liqueur'
    sloe = 'Sloe Liqueur'
    southern = 'Southern Liqueur'
    bitters = 'Bitters'
    champagne = 'Champagne'
    dryvermouth = 'Dry Vermouth'
    sweetvermouth = 'Sweet Vermouth'
    cola = 'Cola'
    gingerale = 'Ginger Ale'
    gingerbeer = 'Ginger Beer'
    lemonlime = 'Lemon Lime'
    sodawater = 'Soda Water'
    tonicwater = 'Tonic Water'
    cranberryjuice = 'Cranberry Juice'
    grapefruitjuice = 'Grapefruit Juice'
    lemonjuice = 'Lemon Juice'
    limejuice = 'Lime Juice'
    orangejuice = 'Orange Juice'
    pineapplejuice = 'Pineapple Juice'
    cream = 'Cream'
    creamofcoconut = 'Cream of Coconut'
    grenadine = 'Grenadine'
    mintsprig = 'Mint Spring'
    simplesyrup = 'Simple Syrup'
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
    if almond in user_selection:
        almondliqueur_check = driver.find_element(By.ID,'almondliqueur_checkbox')
        almondliqueur_check.click()
    if cherry in user_selection:
        cherryliqueur_check = driver.find_element(By.ID,'cherryliqueur_checkbox')
        cherryliqueur_check.click()
    if chocolate in user_selection:
        chocolateliqueur_check = driver.find_element(By.ID,'chocolate_checkbox')
        chocolateliqueur_check.click()
    if coffee in user_selection:
        coffeeliqueur_check = driver.find_element(By.ID,'coffee_checkbox')
        coffeeliqueur_check.click()
    if coconut in user_selection:
        coconut_check = driver.find_element(By.ID,'coconut_checkbox')
        coconut_check.click()
    if irishcream in user_selection:
        irishcream_check = driver.find_element(By.ID,'irishcream_checkbox')
        irishcream_check.click()
    if herbal in user_selection:
        herbal_check = driver.find_element(By.ID,'herbal_checkbox')
        herbal_check.click()
    if mint in user_selection:
        mint_check = driver.find_element(By.ID,'mint_checkbox')
        mint_check.click()
    if melon in user_selection:
        melon_check = driver.find_element(By.ID,'melonliqueur_checkbox')
        melon_check.click()
    if orange in user_selection:
        orange_check = driver.find_element(By.ID,'orangeliqueur_checkbox')
        orange_check.click()
    if peach in user_selection:
        peach_check = driver.find_element(By.ID,'peach_checkbox')
        peach_check.click()
    if raspberry in user_selection:
        raspberry_check = driver.find_element(By.ID,'raspberryliqueur_checkbox')
        raspberry_check.click()
    if sloe in user_selection:
        sloeberry_check = driver.find_element(By.ID,'sloeliqueur_checkbox')
        sloeberry_check.click()
    if southern in user_selection:
        southerncomfort_check = driver.find_element(By.ID,'soco_checkbox')
        southerncomfort_check.click()
    if cola in user_selection:
        cola_check = driver.find_element(By.ID,'cola_checkbox')
        cola_check.click()
    if gingerale in user_selection:
        gingerale_check = driver.find_element(By.ID,'gingerale_checkbox')
        gingerale_check.click()
    if gingerbeer in user_selection:
        gingerbeer_check = driver.find_element(By.ID,'gingerbeer_checkbox')
        gingerbeer_check.click()
    if lemonlime in user_selection:
        lemonlime_check = driver.find_element(By.ID,'lemonlime_checkbox')
        lemonlime_check.click()
    if sodawater in user_selection:
        sodawater_check = driver.find_element(By.ID,'sodawater_checkbox')
        sodawater_check.click()
    if tonicwater in user_selection:
        tonicwater_check = driver.find_element(By.ID,'tonicwater_checkbox')
        tonicwater_check.click()
    if cranberryjuice in user_selection:
        cranberryjuice_check = driver.find_element(By.ID,'cranberryjuice_checkbox')
        cranberryjuice_check.click()
    if grapefruitjuice in user_selection:
        grapefruitjuice_check = driver.find_element(By.ID,'grapefruitjuice_checkbox')
        grapefruitjuice_check.click()
    if lemonjuice in user_selection:
        lemonjuice_check = driver.find_element(By.ID,'lemonjuice_checkbox')
        lemonjuice_check.click()
    if limejuice in user_selection:
        limejuice_check = driver.find_element(By.ID,'limejuice_checkbox')
        limejuice_check.click()
    if orangejuice in user_selection:
        orangejuice_check = driver.find_element(By.ID,'orangejuice_checkbox')
        orangejuice_check.click()
    if pineapplejuice in user_selection:
        pineapplejuice_check = driver.find_element(By.ID,'pineapplejuice_checkbox')
        pineapplejuice_check.click()
    if cream in user_selection:
        cream_check = driver.find_element(By.ID,'cream_checkbox')
        cream_check.click()
    if creamofcoconut in user_selection:
        creamofcoconut_check = driver.find_element(By.ID,'creamofcoconut_checkbox')
        creamofcoconut_check.click()
    if grenadine in user_selection:
        grenadine_check = driver.find_element(By.ID,'grenadine_checkbox')
        grenadine_check.click()
    if mintsprig in user_selection:
        mintsprig_check = driver.find_element(By.ID,'mintsprig_checkbox')
        mintsprig_check.click()
    if simplesyrup in user_selection:
        simplesyrup_check = driver.find_element(By.ID,'simplesyrup_checkbox')
        simplesyrup_check.click()


# if orangejuice in user_selection:orangejuice_check = driver.find_element(By.ID,'orangejuice_checkbox')
# orangejuice_check.click()

# if brandy in user_selection:brandy_check = driver.find_element(By.ID,'brandy_checkbox')
# brandy_check.click()