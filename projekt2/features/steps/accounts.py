from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

@given(u'a user is logged in as admin')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/")
    context.driver.find_element(By.ID, "input-username").click()
    context.driver.find_element(By.ID, "input-username").send_keys("user")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR, ".fa-key").click()
    time.sleep(1)

@given(u'a web browser is at the "Customer" page')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Customers").click()
    context.driver.find_element(By.CSS_SELECTOR, "#collapse-5 > li:nth-child(1) > a").click()


@when(u'admin clicks on "Add New" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


@then(u'shoud see "Add Customer" page')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//a[contains(text(),\'General\')]")


@given(u'a web browser is at the "Add Customer" page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


@then(u'shoud see warning message for accounts')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert")


@given(u'required fields are filled for new account')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("test5")
    context.driver.execute_script("window.scrollTo(0,400)")
    time.sleep(1)
    context.driver.find_element(By.ID, "input-lastname").click()
    context.driver.find_element(By.ID, "input-lastname").send_keys("test5")
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys("test5@gmail.com")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("test5")
    context.driver.find_element(By.ID, "input-confirm").click()
    context.driver.find_element(By.ID, "input-confirm").send_keys("test5")
    context.driver.execute_script("window.scrollTo(0,10)")
    time.sleep(1)


@then(u'shoud see sucess message for accounts')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".alert").click()

@when(u'admin clicks on "Back" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fa-reply").click()


@then(u'shoud see "Customer" page')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h1[contains(.,\'Customers\')]")


@given(u'filter table is filled whit wrong information about created user')
def step_impl(context):
    context.driver.find_element(By.ID, "input-name").click()
    context.driver.find_element(By.ID, "input-name").send_keys("test4")
 

@then(u'shoud see no users')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//td[contains(.,\'No results!\')]")


@given(u'filter table is filled whit right informations about created user')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#filter-customer .card-body").click()
    context.driver.find_element(By.ID, "input-name").send_keys("test5")


@given(u'admin clicks on "Filter" button')
def step_impl(context):
    context.driver.find_element(By.ID, "button-filter").click()


@then(u'shoud see only added customer')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//td[contains(.,\'test5 test5\')]")


@when(u'admin clicks on "Edit" button for added customer')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fa-pencil").click()


@then(u'shoud see "Edit Customer" page')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".card-header")


@given(u'a web browser is at the "Edit Customer" page for added customer')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fa-pencil").click()


@given(u'edits information for account')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("test6")


@given(u'a web browser is at the "Edit Customer" page on added customer')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fa-pencil").click()


@when(u'admin clicks on "Orders" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-warning").click()


@then(u'shoud see "Order List" page for added customer')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//td[contains(.,\'No results!\')]")


@given(u'added customer is selected')
def step_impl(context):
    context.driver.find_element(By.NAME, "selected[]").click()


@when(u'admin clicks on "Delete" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fa-trash-can").click()


@when(u'shoud see popup message "Are you sure?" whit buttons "Ok" and "Cancel"')
def step_impl(context):
    assert context.driver.switch_to.alert.text == "Are you sure?"


@when(u'admin clicks on "Ok" button')
def step_impl(context):
    context.driver.switch_to.alert.accept()

@then(u'shoud zero useres accounts')
def step_impl(context):
    context.driver.refresh()
    assert context.driver.find_element(By.XPATH, "//td[contains(.,\'No results!\')]")

