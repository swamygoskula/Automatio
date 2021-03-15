*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}   Chrome
${url}   https://opensource-demo.orangehrmlive.com/

*** Test Cases ***
LoginTest
    open browser    ${url}   ${browser}
    maximize browser window
    loginToApplication

    select from list by lable   searchSystemUser_userType   Admin
    sleep   3
    close browser

*** Keywords ***
loginToApplication
    input text      id:txtUsername  Admin
    input text      id:txtPassword  admin123
    click button    id:btnLogin