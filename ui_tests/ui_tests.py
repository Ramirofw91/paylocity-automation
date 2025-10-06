import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from config import USERNAME, PASSWORD, EMPLOYEEID,ARODEMPID


#1 Log In Test
def test_load_login_page(page):
    page.goto("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login")
    page.wait_for_selector('input[id="Username"]')
    page.click("#Username")
    page.fill('input#Username', USERNAME)
    page.click("#Username")
    page.click("#Password")
    page.fill('input#Password',PASSWORD)
    page.click("button[type='submit'].btn.btn-primary")
    assert page.url == "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Benefits"

#2 Benefits Page elements
def test_benefits_page(page_logged_in):
    assert page_logged_in.is_visible('a.navbar-brand[href="/Prod/Benefits"]')
    assert page_logged_in.is_visible('#employeesTable')
    assert page_logged_in.is_visible('a[href="/Prod/Account/LogOut"]')
    assert page_logged_in.is_visible('#add')
    page_logged_in.wait_for_selector('i.fas.fa-edit')
    assert page_logged_in.is_visible('i.fas.fa-edit')
    assert page_logged_in.is_visible('i.fas.fa-times')

#3 Add Employee
def test_add_employee(page_logged_in):
    page_logged_in.wait_for_load_state('networkidle')
    page_logged_in.wait_for_selector("#add")
    page_logged_in.click("#add")
    page_logged_in.wait_for_selector('input#firstName')
    page_logged_in.click('input#firstName')
    page_logged_in.fill('input#firstName', 'TestFirstName')
    page_logged_in.click('input#lastName')
    page_logged_in.fill('input#lastName', 'TestLastName')
    page_logged_in.click('input#dependants')
    page_logged_in.fill('input#dependants', '3')
    page_logged_in.click('#addEmployee')
    page_logged_in.wait_for_selector('td:has-text("TestFirstName")')
    assert page_logged_in.is_visible('td:has-text("TestFirstName")')

#4 Modify Employee
def test_modify_employee(page_logged_in):
    page_logged_in.wait_for_load_state('networkidle')
    row_selector = f"tr:has-text('{EMPLOYEEID}')"
    page_logged_in.locator(f"{row_selector} i.fas.fa-edit").click()
    page_logged_in.fill('input#dependants', "4")
    page_logged_in.click('#updateEmployee')
    row_selector = f"tr:has-text('{EMPLOYEEID}')"
    row = page_logged_in.locator(row_selector)
    row.wait_for()
    dependants_cell = row.locator("td").nth(3)
    dependants_value = dependants_cell.inner_text()
    assert dependants_value == "4"


# 4 Delete Employee
def test_deleteEmployee(page_logged_in):
        page_logged_in.wait_for_selector(f"tr:has-text('{ARODEMPID}')")
        fila = page_logged_in.locator(f"tr:has-text('{ARODEMPID}')")
        fila.wait_for()
        page_logged_in.locator(f"tr:has-text('{ARODEMPID}') i.fas.fa-times").click()
        page_logged_in.wait_for_selector('#deleteEmployee')
        page_logged_in.click('#deleteEmployee')
        page_logged_in.wait_for_selector(f"tr:has-text('{ARODEMPID}')", state='detached', timeout=10000)
        assert not page_logged_in.query_selector(f"tr:has-text('{ARODEMPID}')")


# 5 Delete Employee
def test_deleteEmployee(page_logged_in):
        page_logged_in.wait_for_selector(f"tr:has-text('{EMPLOYEEID}')")
        fila = page_logged_in.locator(f"tr:has-text('{EMPLOYEEID}')")
        fila.wait_for()
        page_logged_in.locator(f"tr:has-text('{EMPLOYEEID}') i.fas.fa-times").click()
        #if page_logged_in.is_visible('#confirmDelete'):
        page_logged_in.click('#deleteEmployee')
        page_logged_in.wait_for_selector(f"tr:has-text('{EMPLOYEEID}')", state='detached', timeout=10000)
        assert not page_logged_in.query_selector(f"tr:has-text('{EMPLOYEEID}')")

     #page_logged_in.wait_for_timeout(3000)

















