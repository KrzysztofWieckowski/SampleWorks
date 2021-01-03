from datetime import datetime
import os


class StaticMethods:
    """Method that creates folder with current date for reports and returns path to it."""

    @staticmethod
    def reports_folder():
        date = StaticMethods.get_date()
        dir = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir))
        folder = dir + "/Reports/Reports" + date + "/"
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    """Method which gets current date."""
    @staticmethod
    def get_date():
        date_format = '%Y%m%d'
        return datetime.now().strftime(date_format)