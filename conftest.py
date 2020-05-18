import os

import pytest

from selenium import webdriver
import time


@pytest.fixture()
def driver(request):
    BROWSERSTACK_URL = 'https://{}:{}@hub-cloud.browserstack.com/wd/hub'.format(
        os.environ['BROWSERSTACK_USERNAME'], os.environ['BROWSERSTACK_API_KEY'])

    desired_cap = {

      'os' : 'Windows',
      'os_version' : '10',
      'browser' : 'Chrome',
      'browser_version' : '80',
      'name' : request.param

    }

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        desired_capabilities=desired_cap
      )

    yield driver
    driver.quit()
