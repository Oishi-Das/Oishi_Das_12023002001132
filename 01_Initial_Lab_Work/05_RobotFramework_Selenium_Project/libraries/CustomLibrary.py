class CustomLibrary:

    def create_test_email(self, name):
        return name.lower().replace(" ", ".") + "@example.com"

    def verify_phone_number(self, phone):
        phone = str(phone)
        if len(phone) != 10 or not phone.isdigit():
            raise AssertionError("Phone number must contain exactly 10 digits")

    def verify_text_contains(self, text, expected):
        if expected not in text:
            raise AssertionError(f"Expected '{expected}' to be present in '{text}'")