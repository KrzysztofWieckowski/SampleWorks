from datetime import datetime
import os


class StaticMethods:

    # Method which creates folder with current date for reports and returns path to it
    @staticmethod
    def report_folder():
        date = StaticMethods.get_date()
        dir = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir))
        folder = dir + "/Reports/Reports" + date + "/"
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    # Method for getting current date.
    @staticmethod
    def get_date():
        d_format = '%Y%m%d'
        return datetime.now().strftime(d_format)