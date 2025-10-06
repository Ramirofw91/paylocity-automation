import pytest
from playwright.sync_api import sync_playwright
import requests

@pytest.fixture
def auth_session():
    USERNAME = "TestUser815"
    PASSWORD = "zoC4ucG%)@81"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login")
        page.fill("input#Username", USERNAME)
        page.fill("input#Password", PASSWORD)
        page.click("button[type='submit']")
        page.wait_for_load_state("networkidle")
        cookies = page.context.cookies()
        browser.close()
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    return session