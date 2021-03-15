*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}   Chrome
${url}   https://opensource-demo.orangehrmlive.com/

*** Test Cases ***
TestingInputBox
    open browser    ${url}  ${browser}
    maximize browser window
    input text      id:txtUsername  Admin
    input text      id:txtPassword  admin123
    click button    id:btnLogin
    title should be  OrangeHRM
    close browser

*** Keywords ***

