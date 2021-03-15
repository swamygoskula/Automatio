*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***
TabbedWindowTest
    open browser    https://www.google.co.in/  Chrome
    sleep   3
    close all browsers