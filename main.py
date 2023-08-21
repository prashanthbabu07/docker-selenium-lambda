from selenium import webdriver
from tempfile import mkdtemp
from selenium.webdriver.common.by import By
import time
import base64


def handler(event=None, context=None):
    options = webdriver.ChromeOptions()
    options.binary_location = '/opt/chrome/chrome'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")
    chrome = webdriver.Chrome("/opt/chromedriver",
                              options=options)
    chrome.get("https://example.com/")

    time.sleep(5)

    image_bytes = chrome.get_screenshot_as_png();
    #text = chrome.find_element(by=By.XPATH, value="//html").text
    base64_bytes = base64.b64encode(image_bytes)
    base64_string = base64_bytes.decode("utf-8")

    response = {
        "statusCode": 200,
        "body": base64_string
    }

    return response
