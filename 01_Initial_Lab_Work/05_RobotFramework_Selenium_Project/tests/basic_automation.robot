*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://testautomationpractice.blogspot.com/
${BROWSER}    Chrome
${SCREENSHOT_DIR}    ${EXECDIR}/screenshots

*** Test Cases ***
Open Browser And Verify Form
    Open Browser    ${URL}    ${BROWSER}
    Set Screenshot Directory    ${SCREENSHOT_DIR}
    Maximize Browser Window
    Sleep    3s
    Capture Page Screenshot    basic_01_homepage.png
    Page Should Contain Element    id:name
    Capture Page Screenshot    basic_02_name_element.png
    Input Text    id:name    Oishi Das
    Sleep    2s
    Capture Page Screenshot    basic_03_name_entered.png
    Page Should Contain Element    id:email
    Input Text    id:email    oishi@example.com
    Sleep    2s
    Capture Page Screenshot    basic_04_email_entered.png
    Close Browser