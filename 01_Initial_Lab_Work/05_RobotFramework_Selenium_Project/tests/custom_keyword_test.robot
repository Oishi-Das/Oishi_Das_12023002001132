*** Settings ***
Resource    ../resources/common_keywords.robot

*** Test Cases ***
Fill Form Using Custom Keywords
    Open Practice Website
    Verify Name Field
    Fill Basic Form    Oishi Das    oishi@example.com    9876543210
    Close Practice Website