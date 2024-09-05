import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(30)


@when(u'open orange hrm homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()


@then(u'verify that the logo present on page')
def step_impl(context):
    status = context.driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()
    assert status is True


@then(u'close browser')
def step_impl(context):
    context.driver.close()
