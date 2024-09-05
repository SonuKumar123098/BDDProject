from behave import given, when, then


# allure serve reports/    --> generate html reports
#  behave -f allure_behave.formatter:AllureFormatter -o reports/ features

@given(u'I launch browser')
def step_impl(context):
    assert True, "Test Passed"


@when(u'I open application')
def step_impl(context):
    assert True, "Test Passed"


@when(u'Enter valid username and password')
def step_impl(context):
    assert True, "Test Passed"


@when(u'click on Login')
def step_impl(context):
    assert True, "Test Passed"


@then(u'User must login to the Dashboard page')
def step_impl(context):
    assert True, "Test Passed"


@when(u'navigate to search page')
def step_impl(context):
    assert True, "Test Passed"


@then(u'search page should display')
def step_impl(context):
    assert True, "Test Passed"


@when(u'navigate to advanced search page')
def step_impl(context):
    assert True, "Test Passed"


@then(u'advanced search page should display')
def step_impl(context):
    assert True, "Test Passed"
