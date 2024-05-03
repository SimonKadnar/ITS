from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

@given(u'a web browser is at the "Orders" page')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "View more...").click()


@then(u'shoud see "Add order" page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) > .card-header")


@given(u'a web browser is at the "Add order" page')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "View more...").click()
    context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


@when(u'admin clicks on "Confirm" button')
def step_impl(context):
    context.driver.find_element(By.ID, "button-confirm").click()
