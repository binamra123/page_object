# import os
# import shutil
import pytest
# from Pages.loginpage import LoginPage
# from Utils.screenshot import take_screenshot

# @pytest.fixture(scope="session", autouse=True)
# def move_html_report():
#     yield  
#     source_file = 'pytest_html_report.html'
#     destination_folder = 'Report'
#     destination_file = os.path.join(destination_folder, 'pytest_html_report.html')
#     shutil.move(source_file, destination_file)



# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()

#     if rep.when == "call" and rep.failed:
#         driver = item.funcargs.get("driver")
#         if driver:
#             test_name = item.name
#             screenshot_dir = os.path.join("screenshots", "failed_tests")
#             os.makedirs(screenshot_dir, exist_ok=True)
#             screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")
#             take_screenshot(driver, screenshot_path)

