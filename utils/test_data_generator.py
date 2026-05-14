from datetime import datetime


class TestDataGenerator:

    @staticmethod
    def generate_username():
        timestamp = datetime.now().strftime("%d%m%y%H%M%S")
        return f"user_{timestamp}"

    @staticmethod
    def generate_password():
        timestamp = datetime.now().strftime("%d%m%y%H%M%S")
        return f"T@{timestamp}"