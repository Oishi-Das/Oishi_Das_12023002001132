*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=../test_data/login_data.csv
Test Template    Fill Form With External Data
Test Teardown    Close Browser

*** Test Cases ***
Fill Data Entry Form
    ${name}    ${email}    ${phone}

*** Keywords ***
Fill Form With External Data
    [Arguments]    ${name}    ${email}    ${phone}
    Open Browser    https://testautomationpractice.blogspot.com/    Chrome
    Set Screenshot Directory    ${EXECDIR}/screenshots
    Maximize Browser Window
    Sleep    3s
    Capture Page Screenshot    data_${name}_homepage.png
    Page Should Contain Element    id:name
    Input Text    id:name    ${name}
    Sleep    2s
    Input Text    id:email    ${email}
    Sleep    2s
    Input Text    id:phone    ${phone}
    Sleep    5s
    Capture Page Screenshot    data_${name}_form_filled.png