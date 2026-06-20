from playwright.sync_api import sync_playwright


TARGET_URL = "https://develop-car-portal.iranianpooshesh.com/"


def main() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(TARGET_URL, wait_until="domcontentloaded")
        page.wait_for_timeout(10_000)
        browser.close()


if __name__ == "__main__":
    main()
