# Assignment2
# Project Setup

This project uses pytest for testing and selenium for browser automation, along with EdgeDriver and ChromeDriver for compatibility with different browsers.

Prerequisites
Python 3.10 - Make sure Python is installed on your machine. You can download it https://www.python.org/downloads/.

Pip - Python’s package installer, usually installed with Python.

Installation

Step 1: Install pytest and selenium

Open a terminal or command prompt.

Run the following commands to install pytest and selenium:

bash

pip install pytest

pip install selenium

Step 2: Install Web Drivers
1. ChromeDriver
Download ChromeDriver for your version of Chrome from the ChromeDriver download page.
Extract the downloaded file.
Move the chromedriver executable to a folder that is in your system's PATH. For example, on Windows, you could place it in C:\Windows\System32 or add its folder to the PATH.
2. EdgeDriver
Download EdgeDriver for your version of Microsoft Edge from the EdgeDriver download page.
Extract the downloaded file.
Move the msedgedriver executable to a folder in your system's PATH, as with ChromeDriver.
Step 3: Verify Installation

You can verify that the drivers are accessible by opening a terminal or command prompt and typing:

bash

chromedriver --version

msedgedriver --version

If installed correctly, the version of each driver should display.

Step 4: Running Tests

To run your tests with pytest, use:

bash

pytest <your_test_file.py>

This will automatically find and run all functions that start with test_ in the specified file.

Additional Information

Updating Web Drivers: Make sure your drivers match your browser versions to avoid compatibility issues.
Documentation:

pytest: https://docs.pytest.org/en/stable/contents.html

selenium: https://selenium-python.readthedocs.io/