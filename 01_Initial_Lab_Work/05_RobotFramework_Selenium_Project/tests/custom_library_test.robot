*** Settings ***
Library    ../libraries/CustomLibrary.py

*** Test Cases ***
Create Test Email
    ${email}=    Create Test Email    Oishi Das
    Should Be Equal    ${email}    oishi.das@example.com

Verify Phone Number
    Verify Phone Number    9876543210

Verify Text
    Verify Text Contains    Robot Framework Selenium Automation    Selenium