from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)


@when(u'I open OrangeHRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()


@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pwd)


@when(u'click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()


@then(u'User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        dashboard = (context.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']"))
        txt = dashboard.text
        status = dashboard.is_displayed()
    except:
        context.driver.close()
        assert False, "Test Failed"

    assert txt == "Dashboard"
    assert status is True, "Test Passed"
    context.driver.close()
