arr = ['coconut', 'irishcream', 'herbal', 'mint', 'melon', 'orange', 'peach', 'rasberry', 'sloeberry', 'southerncomfort'] 
const easy = (arr) => {
    for (let i = 0; i < arr.length; i++) {
        console.log("if " + arr[i] + " in user_selection:" + arr[i] + "_check = driver.find_element(By.ID,'" + arr[i] + "_checkbox')" + arr[i] + '_check.click()')
    }
}
easy(arr)

// if in user_selection:
//         _check = driver.find_element(By.ID,'_checkbox')
//         _check.click()

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
melon_check = driver.find_element(By.ID,'melon_checkbox')
melon_check.click()

if orange in user_selection:
orange_check = driver.find_element(By.ID,'orange_checkbox')
orange_check.click()

if peach in user_selection:
peach_check = driver.find_element(By.ID,'peach_checkbox')
peach_check.click()

if rasberry in user_selection:
rasberry_check = driver.find_element(By.ID,'rasberry_checkbox')
rasberry_check.click()

if sloeberry in user_selection:
sloeberry_check = driver.find_element(By.ID,'sloeberry_checkbox')
sloeberry_check.click()

if southerncomfort in user_selection:
southerncomfort_check = driver.find_element(By.ID,'southerncomfort_checkbox')
southerncomfort_check.click()
