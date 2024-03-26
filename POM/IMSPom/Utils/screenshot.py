from selenium import webdriver

def take_screenshot(driver, filename):
    try:
        driver.save_screenshot(filename)
        print(f"Screenshot saved as {filename}")
    except Exception as e:
        print(f"Failed to take screenshot: {str(e)}")