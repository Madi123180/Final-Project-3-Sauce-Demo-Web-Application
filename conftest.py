import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import os
import datetime
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def setup_driver():
  # options = Options()
  # options.add_argument("--headless")
  # options.add_argument("--no-sandbox")
  # options.add_argument("--disable-dev-shm-usage")
  # driver = webdriver.Chrome(options=options)
  driver = webdriver.Edge()
  driver.maximize_window()
  driver.get("https://www.saucedemo.com/")
  wait = WebDriverWait(driver, 10)

  yield driver
  driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook that executes after a test runs.
    If a test fails during execution, it automatically captures a screenshot.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        # Retrieve the fixture value
        fixture_val = item.funcargs.get("setup_driver")

        driver = None
        if fixture_val:
            # Check if it's a tuple or list (like your (driver, wait))
            if isinstance(fixture_val, (tuple, list)):
                driver = fixture_val[0]
            else:
                driver = fixture_val  # In case it's just the driver object directly

        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name
            file_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")

            driver.save_screenshot(file_path)
            print(f"\n[FAILURE] Screenshot saved to: {file_path}")