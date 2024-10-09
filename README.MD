# SauceDemo Inventory Page Testing with Playwright and Python

# Make sure Python is installed in machine
  reference url - https://www.python.org/downloads/
  
# Pycharm download and use to create a project
  reference url - https://www.jetbrains.com/pycharm/download

# Why choose Playwright?
Playwright is opensource tool and very comfortable for UI and API testing and
continues integration.

# Create a pycharm SWagLab and install dependencies
pip install playwright

# Check Playwright install or not
pip list
playwright            1.47.0

# Install pytest and pytest-html
pip install pytest pytest-html

# To run the tests go to the root of the project and run (headless mode)
pytest -s

# To run the tests go to the root of the project and run (headed mode)
pytest test.py --headed

# Debug test script use below command
 PWDEBUG=1 pytest -s -k test_case_link

# Allure report install 
pip install pytest allure-pytest
# Allure report to generate
pytest --alluredir=allure-results

# Allure report view 
 allure serve allure-result
