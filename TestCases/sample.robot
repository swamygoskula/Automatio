*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
Mouseactions
    open browser    https://www.google.co.in/    Chrome
    maximize browser window
    open context menu   xpaht://*[@id="searchSystemUser_userName"]
    sleep   3

    #double click action
    go to   https://www.orangehrm.com/  Chrome
    maximize browser window
    double click element    xpath://*[@id="searchSystemUser_userName"]
    sleep   3

    #drag and drop
    go to   https://www.orangehrm.com/   Chrome
    maximize browser window
    drag and drop   id:box6 id:box7
    sleep   5
    close browser

*** Keywords ***
