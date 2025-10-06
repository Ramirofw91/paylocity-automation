import playwright
import pytest
from playwright.sync_api import sync_playwright
from config import USERNAME, PASSWORD


#username = "TestUser815"
#password = "zoC4ucG%)@81"
@pytest.fixture
def page():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    yield page

@pytest.fixture
def page_logged_in(page):
    page.goto("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login")
    page.wait_for_selector('input[id="Username"]')
    page.click("#Username")
    page.fill('input#Username', USERNAME)
    page.click("#Username")
    page.click("#Password")
    page.fill('input#Password', PASSWORD)
    page.click("button[type='submit'].btn.btn-primary")
    return page
