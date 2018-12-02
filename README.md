# Automation-Python-Shorten-Url
### This is a sample repository for Selenium + Python 3.x compatible for Docker.  

# [Description]
This Framework use `Python 3.x` inside,
We recommend you to visit `https://www.python.org/` for reference.

We divide this framework to some modules 

#
#### [GlobalConfig.py] `src.main.config.GlobalConfig`
    GlobalConfig    -   This module responsible of the
                        configuration of framework. 
                        Will determine it runtime according
                        to the Operating System and more...

#
#### [BasePage.py] `src.main.base.BasePage`
    BasePage        -   This module responsible of the  
                        main functionalitieso f selenium  

#
#### [Wait.py] `src.main.base.utils.Wait`
    Wait            -   This module responsible of handling
                        smart waiting for different  
                        type of scenarios in the DOM

#
#### [Logger.py] `src.main.base.utils.Logger`
    Logger          -   This module responsible to 
                        log and record all the actions 
                        taken by the framework and will
                        contain critical information for
                        log analysis and errors during runtime 

#
#### [BitlyHomePage.py] `src.main.base.pages.BitlyHomePage`
    BitlyHomePage   -   This module represents the
                        POM. It contains some functional

#
#### [BaseTes.py] `src.test.BaseTest`
    BaseTest        -   This module is the core module 
                        for tests, all tests inherit some
                        functionalities from it. It handles
                        mostly the startup sessions of the
                        browser and it closure.
                        Also, will handle the configuration of 
                        Selenium/Docker Usage.

#
#### [UrlShortenService.py] `src.test.e2e.UrlShortenServiceTest`
    UrlShortenService   -   This module represents the
                            test of our POM based on UI
                            using Selenium with Unittest
                            module to handle TestCases, 
                            TestSuites and more...

#
##### [Docs] `./Docs`
    TP.txt          -   A sample manual Test Plan
                        for future implementation 
                        and refrence for Manual Testing 

#
##### [Docker Configuration] `./docker/`
    docker-compose.yml  -  This is a configuration file
                           for selenium/docker useage.   

#
##### [Docker Scripts] `./docker/localhost/`
    start-docker-hub.sh     -   Shell script that runs docker-hub
    start-chrome-node.sh    -   Shell script that runs chrome-node 
    start-firefox-node.sh   -   Shell script that runs firefox-node

#
# HOW-TO
##### [LOGS]
Note that a log is already created by our first time test run.
Make sure to view the log that located at `src.runtime.logs`
for to ensure you're running on Docker / Localhost.
* Expect `[BaseTest - Call "setUp" -> is_docker True]` for Docker
* Expect `[BaseTest - Call "setUp" -> is_docker False]` for Localhost

##### [IMPORTANT Python Libs]
1. In case your machine does't contain `Python 3.x`, please download it to your machine
2. Once `Python 3.x` is installed, open your `commad-prompt` or `terminal`
and use the following commands:
- `pip install --upgrade pip`   -   to ensure your pip is up-to-date
- `pip install unittest`        -   to ensure your unittest is up-to-date
- `pip install selenium`        -   to install Selenium libraries

#
##### [DOCKER]
1. If you use a docker, please make sure to install it 
from the following link : `https://store.docker.com/editions/community/docker-ce-desktop-mac`
2. Simply navigate to `./docker/localhost` and run the following command
`./start-docker-hub.sh` 
3. After you've done this, run `./start-chrome-node.sh` or `./start-firefox-node.sh`
to start a node.
4. Make sure your `BaseTest.py` module configuration
sets `setUp(self, dokerized=True)` to ensure running IN Docker mode.
5. Run the automation from command-line using the following command `python -m unittest <package>/<test_module>`

#
##### [Unittest Base]
1. Make sure your `BaseTest.py` module configuration
sets `setUp(self, dokerized=False)` to ensure running NOT in Docker mode.
2. Run the automation from command-line using the following command `python -m unittest <package>/<test_module>`

#
###### Run From CLI Example: 
 
`$ python -m unittest src/test/e2e/UrlShortenServiceTest.py`
