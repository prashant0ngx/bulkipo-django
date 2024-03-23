""" from celery import shared_task
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from .scraping import web_driver,login, goto_asba, ipo_selector,applySuccess,close_browser,open_ipo_lister

# Initialize the web driver instance
driver_instance = web_driver()

@shared_task
def apply_ipo_async(crn, pin):
    try:
        # Open browser and perform login
        driver_instance.open_browser()
        login(crn, pin)

        # Go to ASBA page
        goto_asba()

        # Select IPO and apply
        ipo_selector()
        applySuccess()

        return "IPO applied successfully!"
    except Exception as e:
        # Handle exceptions as needed
        return str(e)
    finally:
        # Ensure browser is closed
        close_browser()

@shared_task
def fetch_ipo_list_async():
    try:
        # Open browser and fetch IPO list
        driver_instance.open_browser()
        ipos = open_ipo_lister()
        return ipos
    except Exception as e:
        # Handle exceptions as needed
        return []
    finally:
        # Ensure browser is closed
        close_browser()

# Define other Celery tasks as needed
 """