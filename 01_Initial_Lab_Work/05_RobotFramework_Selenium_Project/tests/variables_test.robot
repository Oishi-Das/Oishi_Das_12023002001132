*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://testautomationpractice.blogspot.com/
${BROWSER}    Chrome
${NAME}    Oishi Das
${EMAIL}    oishi@example.com
${PHONE}    9876543210
${SCREENSHOT_DIR}    ${EXECDIR}/screenshots

*** Test Cases ***
Fill Form Using Variables
    Open Browser    ${URL}    ${BROWSER}
    Set Screenshot Directory    ${SCREENSHOT_DIR}
    Maximize Browser Window
    Sleep    3s
    Capture Page Screenshot    variables_01_homepage.png
    Page Should Contain Element    id:name
    Input Text    id:name    ${NAME}
    Sleep    2s
    Capture Page Screenshot    variables_02_name.png
    Input Text    id:email    ${EMAIL}
    Sleep    2s
    Capture Page Screenshot    variables_03_email.png
    Input Text    id:phone    ${PHONE}
    Sleep    4s
    Capture Page Screenshot    variables_04_phone.png
    Close Browser