*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://testautomationpractice.blogspot.com/
${BROWSER}    Chrome
${SCREENSHOT_DIR}    ${EXECDIR}/screenshots

*** Keywords ***
Open Practice Website
    Open Browser    ${URL}    ${BROWSER}
    Set Screenshot Directory    ${SCREENSHOT_DIR}
    Maximize Browser Window
    Sleep    3s
    Capture Page Screenshot    custom_keyword_01_open.png

Fill Basic Form
    [Arguments]    ${name}    ${email}    ${phone}
    Page Should Contain Element    id:name
    Input Text    id:name    ${name}
    Sleep    2s
    Input Text    id:email    ${email}
    Sleep    2s
    Input Text    id:phone    ${phone}
    Sleep    3s
    Capture Page Screenshot    custom_keyword_02_form.png

Verify Name Field
    Page Should Contain Element    id:name

Close Practice Website
    Close Browser