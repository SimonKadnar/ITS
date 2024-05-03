from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


@given(u'a web browser is at the home page')
def step_impl(context):
    context.driver.get("http://opencart:8080")


@given(u'the user enters name of testing product into the search bar')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("Imac")


@when(u'user clicks on "Search" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fa-magnifying-glass").click()


@then(u'shoud see test product on "Search" page')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h1[contains(.,\'Search - Imac\')]")


@given(u'a web browser is at the "Search" page whit test product')
def step_impl(context):
    context.driver.get("http://opencart:8080/index.php?route=product/search&language=en-gb&search=imac")


@when(u'user clicks on "Add Cart" button')
def step_impl(context):
    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0,500)")
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(1) > form .fa-shopping-cart").click()
    time.sleep(1) 
    context.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(1) > form button:nth-child(1)").click() 


@then(u'shoud see sucess message for added product')
def step_impl(context):
    time.sleep(1)
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert")


@given(u'in basket is test product')
def step_impl(context):
    pass


@when(u'user clicks on "View Cart" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".list-inline-item:nth-child(4) .d-none").click()


@then(u'shoud see "Shopping Cart" page whit added product')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h1[contains(.,\'Shopping Cart\')]")
    assert context.driver.find_element(By.XPATH, "(//a[contains(text(),\'iMac\')])[2]")


@given(u'a web browser is at the "Shopping Cart" page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=checkout/cart")


@when(u'user clicks on "Remove" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4) > .fa-solid").click()


@then(u'shopping cart shoud by empty')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "p:nth-child(2)")


@when(u'user clicks on "Checkout" button')
def step_impl(context):
    context.driver.get("http://opencart:8080")
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("mac")
    context.driver.find_element(By.CSS_SELECTOR, ".fa-magnifying-glass").click()
    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0,500)")
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(1) > form .fa-shopping-cart").click()
    time.sleep(1) 
    context.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(1) > form button:nth-child(1)").click() 
    context.driver.execute_script("window.scrollTo(0,10)")
    time.sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, ".list-inline-item:nth-child(5) .d-none").click()

    
@then(u'shoud see "Checkout" page whit added product')
def step_impl(context):

    assert context.driver.find_element(By.XPATH, "//h1[contains(.,\'Checkout\')]")
    context.driver.execute_script("window.scrollTo(0,500)")
    time.sleep(1)
    assert context.driver.find_element(By.XPATH, "(//a[contains(text(),\'iMac\')])[2]")


@given(u'a web browser is at the "Checkout" page')
def step_impl(context):
        context.driver.get("http://opencart:8080/en-gb?route=checkout/checkout")


@given(u'required fields are not filled')
def step_impl(context):
    pass


@when(u'user click on "button-register" button')
def step_impl(context):
    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0,800)")
    time.sleep(1)
    context.driver.find_element(By.ID, "button-register").click()


@then(u'shoud see warning message for order')
def step_impl(context):
    time.sleep(1)
    assert context.driver.find_element(By.ID, "error-password")


@given(u'required fields are filled for order')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("test2")
    context.driver.find_element(By.ID, "input-lastname").click()
    context.driver.find_element(By.ID, "input-lastname").send_keys("test2")

    context.driver.execute_script("window.scrollTo(0,300)")
    time.sleep(1)
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys("test5@gmail.com")
    context.driver.find_element(By.ID, "input-shipping-address-1").click()
    context.driver.find_element(By.ID, "input-shipping-address-1").send_keys("test2")
    context.driver.find_element(By.ID, "input-shipping-city").click()

    context.driver.execute_script("window.scrollTo(0,600)")
    time.sleep(1)
    context.driver.find_element(By.ID, "input-shipping-city").send_keys("test2")
    context.driver.find_element(By.ID, "input-shipping-postcode").click()
    context.driver.find_element(By.ID, "input-shipping-postcode").send_keys("test2")
    context.driver.find_element(By.ID, "input-shipping-zone").click()
    dropdown = context.driver.find_element(By.ID, "input-shipping-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Aberdeen']").click()

    context.driver.execute_script("window.scrollTo(0,800)")
    time.sleep(1)
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("test2")
    context.driver.find_element(By.ID, "input-register-agree").click()
    context.driver.find_element(By.ID, "button-register").click()

    context.driver.execute_script("window.scrollTo(0,200)")
    time.sleep(1)
    context.driver.find_element(By.ID, "input-shipping-method").click()
    context.driver.find_element(By.ID, "button-shipping-methods").click()
    context.driver.find_element(By.CSS_SELECTOR, ".form-check:nth-child(3) > label").click()
    context.driver.find_element(By.ID, "button-shipping-method").click()
    context.driver.find_element(By.ID, "button-payment-methods").click()
    context.driver.find_element(By.CSS_SELECTOR, "#form-payment-method label").click()
    context.driver.find_element(By.ID, "button-payment-method").click()
    

@when(u'user click on "Confirm Order" button')
def step_impl(context):
    context.driver.find_element(By.ID, "button-confirm").click()

@then(u'shoud see "Success" page')
def step_impl(context):
    time.sleep(1)
    assert context.driver.find_element(By.XPATH, "//h1[contains(.,\'Your order has been placed!\')]")
    context.driver.find_element(By.XPATH, "//nav[@id=\'top\']/div/div[2]/ul/li[2]/div/a/span").click()
    context.driver.find_element(By.LINK_TEXT, "Logout").click()
