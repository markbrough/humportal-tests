import time
import pytest

class TestHome:
    @pytest.mark.parametrize('driver', ['Humportal home page - signatories'], indirect=['driver'])
    def test_home_number_signatories(self, driver):
        driver.get("https://www.humportal.org/")
        if not "Humanitarian" in driver.title:
            raise Exception("Unable to load humportal page!")
        time.sleep(5)
        elem = driver.find_element_by_css_selector("h4[signatorytype='gb']")
        assert int(elem.text) > 0
        print("Found {} signatories".format(elem.text))

    @pytest.mark.parametrize('driver', ['Humportal home page - publishing to IATI'], indirect=['driver'])
    def test_home_number_iati(self, driver):
        driver.get("https://www.humportal.org/")
        if not "Humanitarian" in driver.title:
            raise Exception("Unable to load humportal page!")
        time.sleep(5)
        elem = driver.find_element_by_css_selector("h4[signatorytype='iati']")
        assert int(elem.text) > 0
        print("Found {} signatories".format(elem.text))

    @pytest.mark.parametrize('driver', ['Humportal home page - publishing humanitarian'], indirect=['driver'])
    def test_home_number_publishers(self, driver):
        driver.get("https://www.humportal.org/")
        if not "Humanitarian" in driver.title:
            raise Exception("Unable to load humportal page!")
        time.sleep(5)
        elem = driver.find_element_by_css_selector("h4[signatorytype='humanitarian']")
        assert int(elem.text) > 0
        print("Found {} signatories".format(elem.text))
