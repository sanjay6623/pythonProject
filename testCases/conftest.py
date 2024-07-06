import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup(browser,request):
    if browser=="chrome":
        driver = webdriver.Chrome()
        print("Lunching Chrome Broswer----------")
    elif browser == "firefox":
        driver= webdriver.Firefox()
        print("Launching Firefox browser---------")
    else:
        driver= webdriver.Edge()
        print("Launching edge browser-----")

    driver.maximize_window()


    request.cls.driver = driver
    yield
    driver.quit()
    return driver


def pytest_addoption(parser): # This will get th value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request): #This will return the browser vlaue to setup method

    return request.config.getoption("--browser")


########### PyTest HTML Report#####
# @pytest.mark.optionlhook
# def pytest_configure(config):
#     config.addinivalue_line(
#         "markers", "sanity: mark a test as a sanity test"
#     )
#     config.addinivalue_line(
#         "markers", "regression: mark a test as a regression test"
#     )

def pytest_configure(config):
  config.stash[metadata_key]['Project Name'] = 'Ecommerce'
  config.stash[metadata_key]['Module Name'] = 'Customer'
  config.stash[metadata_key]['Tester Name'] = 'Sanjay'

# registring user markers by config
  config.addinivalue_line(
      "markers", "sanity: mark a test as a sanity test"
  )
  config.addinivalue_line(
      "markers", "regression: mark a test as a regression test"
  )


@pytest.mark.optionlhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

