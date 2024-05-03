from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

@given(u'a web browser is at the home page whit popup buttons "Register" and "Login"')
def step_impl(context):
  context.driver.get("http://opencart:8080")
  context.driver.find_element(By.XPATH, "//nav[@id=\'top\']/div/div[2]/ul/li[2]/div/a/span").click()
  assert context.driver.find_element(By.LINK_TEXT, "Register")
  assert context.driver.find_element(By.LINK_TEXT, "Login")

@when(u'user clicks at "Register" button')
def step_impl(context):
  context.driver.find_element(By.LINK_TEXT, "Register").click()


@then(u'shoud see "Register Acount" page')
def step_impl(context):
  assert context.driver.find_element(By.XPATH, "//h1[contains(.,\'Register Account\')]")


@given(u'a web browser is at the "Register Acount" page')
def step_impl(context):
   context.driver.get("http://opencart:8080/en-gb?route=account/register")


@when(u'user click on "Continue" button')
def step_impl(context):
  context.driver.execute_script("window.scrollTo(0,500)")
  time.sleep(1)
  context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


@then(u'shoud see warning message')
def step_impl(context):
  assert context.driver.find_element(By.CSS_SELECTOR, ".alert")


@given(u'required fields are filled')
def step_impl(context):
  context.driver.find_element(By.ID, "input-firstname").click()
  context.driver.find_element(By.ID, "input-firstname").send_keys("test")
  context.driver.find_element(By.ID, "input-lastname").click()
  context.driver.find_element(By.ID, "input-lastname").send_keys("test")
  context.driver.execute_script("window.scrollTo(0,500)")
  time.sleep(1)
  context.driver.find_element(By.ID, "input-email").click()
  context.driver.find_element(By.ID, "input-email").send_keys("test@gmail.com")
  context.driver.find_element(By.ID, "input-password").click()
  context.driver.find_element(By.ID, "input-password").send_keys("test")
  context.driver.find_element(By.NAME, "agree").click()

@then(u'acount shoud by created')
def step_impl(context):
  assert context.driver.find_element(By.XPATH, "//h1[contains(.,\'Your Account Has Been Created!\')]")
  context.driver.find_element(By.LINK_TEXT, "Continue").click()


@given(u'a web browser is on "Account" page')
def step_impl(context):
  context.driver.get("http://opencart:8080/en-gb?route=account/account&customer_token=141a9183653782bcd33c538d20")


@when(u'user click on "View your order history" button')
def step_impl(context):
  context.driver.find_element(By.LINK_TEXT, "View your order history").click()


@then(u'shoud see orders page')
def step_impl(context):
  assert context.driver.find_element(By.XPATH, "(//a[contains(text(),\'Order History\')])[2]")
  time.sleep(2)


@given(u'a web browser is at the "Order History" page for new registred user')
def step_impl(context):
  pass

@when(u'user click on "Continue" button for return')
def step_impl(context):
  context.driver.find_element(By.LINK_TEXT, "Continue").click()


@then(u'shoud see "Account" page')
def step_impl(context):
  assert context.driver.find_element(By.XPATH, "//h2[contains(.,\'My Account\')]")
  context.driver.find_element(By.XPATH, "//nav[@id=\'top\']/div/div[2]/ul/li[2]/div/a/span").click()
  context.driver.find_element(By.LINK_TEXT, "Logout").click()