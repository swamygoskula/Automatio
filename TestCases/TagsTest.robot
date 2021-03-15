*** Settings ***
Documentation  Basic Search Functionality
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
Verify Basic Search Functionality For eBay
    [Documentation]     This test case verify the basic search
    [Tags]  Functional

    open browser    https://opensource-demo.orangehrmlive.com/  Chrome
    input text      id:txtUsername  Admin
    input text      id:txtPassword  admin123
    click button    id:btnLogin
    close browser

*** Keywords ***
