from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

@given(u'a web browser is at the "Products" page')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Catalog").click()
    context.driver.find_element(By.LINK_TEXT, "Products").click()


@when(u'admin click on "Add New" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary").click()
    time.sleep(1)


@then(u'shoud see "Add Product" page')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "(//a[contains(text(),\'Products\')])[2]")


@given(u'a web browser is at the "Add Product" page')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Catalog").click()
    context.driver.find_element(By.LINK_TEXT, "Products").click()
    context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary").click()


@when(u'admin clicks on "Save" button')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,10)")
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary").click()


@then(u'shoud see warning message for warehouse')
def step_impl(context):
    time.sleep(1)
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-danger")


@given(u'required fields are filled for warehouse')
def step_impl(context):
    context.driver.find_element(By.ID, "input-name-1").click()
    context.driver.find_element(By.ID, "input-name-1").send_keys("test3")
    context.driver.find_element(By.ID, "input-meta-title-1").click()
    context.driver.find_element(By.ID, "input-meta-title-1").send_keys("test3")
    context.driver.find_element(By.LINK_TEXT, "Data").click()
    context.driver.find_element(By.ID, "input-model").click()
    context.driver.find_element(By.ID, "input-model").send_keys("test3")
    context.driver.find_element(By.LINK_TEXT, "SEO").click()
    context.driver.find_element(By.ID, "input-keyword-0-1").click()
    context.driver.find_element(By.ID, "input-keyword-0-1").send_keys("test3")


@then(u'shoud see sucess message for warehouse')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".alert-success").click()

@when(u'admin click on "Back" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'shoud see "Products" page')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "(//a[contains(text(),\'Products\')])[2]")


@given(u'filter table is filled whit wrong information about created product')
def step_impl(context):
    context.driver.find_element(By.ID, "input-name").click()
    context.driver.find_element(By.ID, "input-name").send_keys("abc")


@when(u'admin clicks on "Filter" button')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,500)")
    time.sleep(1)
    context.driver.find_element(By.ID, "button-filter").click()


@then(u'shoud see no products')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//td[contains(.,\'No results!\')]")


@given(u'filter table is filled whit right informations about created product')
def step_impl(context):
    context.driver.find_element(By.ID, "input-name").click()
    context.driver.find_element(By.ID, "input-name").send_keys("test3")


@then(u'shoud see only added product')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".text-success")
    assert context.driver.find_element(By.XPATH, "//small[contains(.,\'Enabled\')]")

@when(u'admin clicks on "Edit" button for first product')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn:nth-child(1)").click()


@then(u'shoud see "Edit Product" page')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//a[contains(text(),\'General\')]")


@given(u'a web browser is at the "Edit Product" page for first product')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Catalog").click()
    context.driver.find_element(By.LINK_TEXT, "Products").click()
    context.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn:nth-child(1)").click()


@given(u'edits information for product')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,250)")
    time.sleep(1)
    context.driver.find_element(By.ID, "input-name-1").click()
    context.driver.find_element(By.ID, "input-name-1").send_keys("test4")


@then(u'shoud see alert sucess message')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-success")


@when(u'admin clicks on "dropdown" button for first product')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle > .fa-solid").click()

@when(u'admin clicks on "+ Add variant" button')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Add Variant").click()


@then(u'warning message about creating variant')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-warning")


@given(u'a web browser is at the "add variant" page')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Catalog").click()
    context.driver.find_element(By.LINK_TEXT, "Products").click()
    context.driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle > .fa-solid").click()
    context.driver.find_element(By.LINK_TEXT, "Add Variant").click()


@when(u'admin chnage data')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "SEO").click()
    context.driver.find_element(By.ID, "input-keyword-0-1").click()
    context.driver.find_element(By.ID, "input-keyword-0-1").send_keys("test5")
    context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary").click()

@when(u'sucess message about creating variant')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-success")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@given(u'first product is selected')
def step_impl(context):
    context.driver.find_element(By.NAME, "selected[]").click()


@when(u'admin clicks on "Copy" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
    context.driver.find_element(By.CSS_SELECTOR, ".text-danger:nth-child(2)").click()


@then(u'shoud see copy of first product which is disabled')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert")


@when(u'see popup message "Are you sure?" whit buttons "Ok" and "Cancel"')
def step_impl(context):
    assert context.driver.switch_to.alert.text == "Are you sure?"


@then(u'shoud see sucess message')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert")