import pytest
import time
from playwright.sync_api import Playwright, sync_playwright

@pytest.fixture(scope="module", params=["chromium", "firefox"])
def page(request):
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, request.param)
        browser = browser_type.launch()
        page = browser.new_page()
        yield page
        browser.close()

def test_title(page):
    try:
        page.goto("https://www.google.com/?hl=En", timeout=60000)
        assert page.title() == "Google"
        print(page.title())
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def test_buttons(page):
    try:
        page.goto("https://www.google.com/?hl=En", timeout=60000)
        page.get_by_role("button", name="Google Search").click()
        page.get_by_role("combobox", name="Search").click()
        page.get_by_role("button", name="Search by image").click()
        page.get_by_role("button", name="Close").click()
    except Exception as e:
        print(f"An error occurred: {str(e)}")


