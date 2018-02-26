Ubuntu:
*Install pip for python3
$curl -O https://bootstrap.pypa.io/get-pip.py
$sudo python3 get-pip.py
refference: https://stackoverflow.com/questions/11268501/how-to-use-pip-with-python-3-x-alongside-python-2-x

*Error message: selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
Download geckodriver from: https://github.com/mozilla/geckodriver/releases
Ubuntu:
$tar zxvf geckodriver-v0.19.1-linux64.tar.gz
$sudo mv geckodriver /usr/bin

Win10:
Extract the downloaded file
Add the path of geckodriver to "Path" of system variable
Remenber to restart system after add system variable to take effect

refference: https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
