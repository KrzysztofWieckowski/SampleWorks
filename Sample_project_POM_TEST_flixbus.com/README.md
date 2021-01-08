# Sample POM Project with Selenium and Python.

This demo project delivers a framework for website test automation. It's a Sample Page Object Model test (with www.flixbus.com. as an example).

You can easy create a new test changing:
- sequence of actions
- number of actions
- data provided
- expected results

However please remember about the search logic in the UI of the website.

The test creates reports and takes screenshots of failures (see the ```Example of test reports``` folder above).
---

## Requirements:
•	Python 3.8.

•	Selenium 3.141.0.

•	Webdriver for browser you would like to use.

•	html-testRunner 1.2.1.

•	JetBrains PyCharm Community Edition 2020.2.3.

## Installing:
•	Python installation package can be download from [here](https://www.python.org/downloads/) - remember to choose option "Add to PATH" during installation.

•	Instructions for Selenium and Webdriver configuration are [here](https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium) - I recommend adding Selenium and Webdriver files to Python installation folder, otherwise PATH variable has to be set also for them.

•	html-testRunner can be installed by simple command in cmd: ```pip install html-testRunner```.

•	PyCharm is available [here](https://www.jetbrains.com/pycharm/download/#section=windows).

## Running:
I've uploaded  whole project with its internal structure. You can simply put it into your PyCharm's PycharmProjects folder or wherever you want.
Steps to run:

1.	Open Pycharm and the project python files.
2.  Set the interpreter and the path in Run/Debug configurations:

  -  select ```Run``` | ```Edit Configurations...```

  -  click the ```+``` button and click ```Python``` on the list.

  -  select ```Script path``` and find the path to ```mainTest.py``` file.

  -  select proper ```Python interpreter``` from the list and click ```OK```.

 For more info please check [here](https://www.jetbrains.com/help/pycharm/run-debug-configuration-python.html#1).

3.	Right-click on file mainTest.py.
4.	Click on ```Run 'mainTest'``` or ```Debug 'mainTest'```.
5.	When the process is finished, open 'Reports' folder created on your computer (where the project is placed) and find an appropriate report. You can easily open the report (html document) using your web browser.




Example of report:

![Test PrtScr](https://user-images.githubusercontent.com/74428939/102710336-dd0a0c80-42b1-11eb-8c86-c4414ed11338.png)
