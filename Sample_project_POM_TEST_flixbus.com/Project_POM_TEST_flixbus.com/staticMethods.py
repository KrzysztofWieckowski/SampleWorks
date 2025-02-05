# staticMethods.

from datetime import datetime
import os


class StaticMethods:
    """A class for static methods."""

    """Method that creates folder with current date for reports and returns path to it."""
    @staticmethod
    def report_folder():
        date = StaticMethods.get_date()
        dir = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir))
        folder = dir + "/Reports/Reports" + date + "/"
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    """Method which returns present date."""
    @staticmethod
    def get_date():
        date_format = '%Y%m%d'
        return datetime.now().strftime(date_format)

    """Method which screenshots and saves it to report folder."""
    @staticmethod
    def save_screenshot_picture(driver, file_name):
        date_time = StaticMethods.get_date_time()
        screenshot_folder = StaticMethods.report_folder()
        picture = screenshot_folder + file_name + ' ' + date_time + '.png'
        driver.save_screenshot(picture)

    """Method for getting current date and time."""
    @staticmethod
    def get_date_time():
        dt_format = '%Y%m%d_%H%M%S'
        return datetime.now().strftime(dt_format)
