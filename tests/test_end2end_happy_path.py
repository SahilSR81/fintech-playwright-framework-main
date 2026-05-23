import pytest
from playwright.sync_api import expect, Page

from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.open_account_page import OpenAccountPage
from pages.accounts_overview_page import AccountsOverviewPage
from pages.transfer_funds_page import TransferFundsPage
from pages.find_transactions_page import FindTransactionsPage
from pages.bill_pay_page import BillPayPage
from pages.loan_request_page import LoanRequestPage
from pages.update_profile_page import UpdateProfilePage

from utils.test_data_generator import TestDataGenerator


class TestE2EHappyPath:

    def test_complete_e2e_workflow(self, page: Page):
        """
        Complete End-to-End Happy Path Test covering:
        1. User Registration
        2. User Login
        3. Open New Account
        4. View Account Overview
        5. Transfer Funds
        6. Find Transactions
        7. Bill Payment
        8. Loan Request
        9. Update Contact Information
        10. User Logout
        """

        # ===== STEP 1: USER REGISTRATION =====
        print("\n" + "="*60)
        print("STEP 1: USER REGISTRATION")
        print("="*60)

        home_page = HomePage(page)
        home_page.click_register_link()

        register_page = RegisterPage(page)

        # Generate user credentials
        username = TestDataGenerator.generate_username()
        password = TestDataGenerator.generate_password()

        print(f"Registering user: {username}")

        # Fill registration form
        register_page.fill_registration_form(
            first_name="Sahil",
            last_name="Singh",
            address="123 Main Street",
            city="Ranchi",
            state="Jharkhand",
            zip_code="834001",
            phone_number="9876543210",
            ssn="1234",
            username=username,
            password=password
        )

        register_page.click_register_button()

        # Verify registration success
        expect(register_page.success_message).to_be_visible()
        print(f"✓ User registered successfully: {username}")

        # ===== STEP 2: USER LOGIN =====
        print("\n" + "="*60)
        print("STEP 2: USER LOGIN")
        print("="*60)

        login_page = LoginPage(page)

        # Logout from registration success page and login again
        login_page.click_logout_link()

        # Login with registered credentials
        login_page.login_user(
            username=username,
            password=password
        )

        # Verify login success
        expect(login_page.account_overview_text).to_be_visible()
        print(f"✓ User logged in successfully")

        # ===== STEP 3: OPEN NEW ACCOUNT =====
        print("\n" + "="*60)
        print("STEP 3: OPEN NEW ACCOUNT")
        print("="*60)

        open_account_page = OpenAccountPage(page)
        open_account_page.navigate_to_open_account()

        # Wait for page to fully load
        page.wait_for_load_state("domcontentloaded")

        # Open a new Savings account
        print("Opening new Savings account...")
        open_account_page.open_account(
            account_type="SAVINGS",
            from_account_index=0
        )

        # Verify account opened
        open_account_page.verify_account_opened()

        # Get new account ID
        new_account_id = open_account_page.get_new_account_id()
        print(f"✓ New account created: {new_account_id}")

        # ===== STEP 4: VIEW ACCOUNT OVERVIEW =====
        print("\n" + "="*60)
        print("STEP 4: VIEW ACCOUNT OVERVIEW")
        print("="*60)

        # Navigate to accounts overview
        page.get_by_role("link", name="Accounts Overview").click()

        accounts_overview_page = AccountsOverviewPage(page)

        # Wait for accounts data to load
        accounts_overview_page.wait_for_accounts_data()
        accounts_overview_page.verify_accounts_overview_page()

        # Get first account number (the default checking account from registration)
        from_account = accounts_overview_page.get_first_account_number()
        print(f"✓ Account Overview verified")
        print(f"  Default Account: {from_account}")
        print(f"  New Account: {new_account_id}")

        # ===== STEP 5: TRANSFER FUNDS =====
        print("\n" + "="*60)
        print("STEP 5: TRANSFER FUNDS")
        print("="*60)

        # Navigate to transfer funds
        page.get_by_role("link", name="Transfer Funds").click()

        transfer_page = TransferFundsPage(page)

        # Transfer amount
        transfer_amount = "100.00"

        print(f"Transferring ${transfer_amount} from {from_account} to {new_account_id}")

        transfer_page.fill_transfer_amount(transfer_amount)
        transfer_page.select_from_account(from_account)
        transfer_page.select_to_account(new_account_id)
        transfer_page.click_transfer_button()

        # Verify transfer success
        expect(transfer_page.transfer_complete_heading).to_be_visible()
        confirmation_amount = transfer_page.get_confirmation_amount()
        print(f"✓ Transfer completed: {confirmation_amount}")

        # ===== STEP 6: FIND TRANSACTIONS =====
        print("\n" + "="*60)
        print("STEP 6: FIND TRANSACTIONS")
        print("="*60)

        # Navigate to find transactions
        page.get_by_role("link", name="Find Transactions").click()

        find_trans_page = FindTransactionsPage(page)

        # Select account to search in
        find_trans_page.select_account(index=0)

        # Search by amount
        print(f"Searching for transaction with amount: ${transfer_amount}")
        find_trans_page.search_by_amount(transfer_amount)

        # Verify transaction found
        find_trans_page.verify_results_visible()
        expect(find_trans_page.transaction_table).to_contain_text(transfer_amount)
        print(f"✓ Transaction found successfully")

        # ===== STEP 7: BILL PAYMENT =====
        print("\n" + "="*60)
        print("STEP 7: BILL PAYMENT")
        print("="*60)

        # Navigate to bill pay
        page.get_by_role("link", name="Bill Pay").click()

        bill_pay_page = BillPayPage(page)

        # Bill payment details
        bill_amount = "50.00"
        payee_info = {
            "payee_name": "Electric Company",
            "address": "123 Power Street",
            "city": "Volttown",
            "state": "CA",
            "zipcode": "90210",
            "phone": "555-0001",
            "account_number": "987654321",
        }

        print(f"Processing bill payment of ${bill_amount} to {payee_info['payee_name']}")

        bill_pay_page.pay_bill(
            payee_name=payee_info["payee_name"],
            address=payee_info["address"],
            city=payee_info["city"],
            state=payee_info["state"],
            zipcode=payee_info["zipcode"],
            phone=payee_info["phone"],
            account_number=payee_info["account_number"],
            amount=bill_amount,
            from_account_index=0
        )

        # Verify bill payment success
        bill_pay_page.verify_bill_payment_successful()
        print(f"✓ Bill payment successful")

        # ===== STEP 8: REQUEST LOAN =====
        print("\n" + "="*60)
        print("STEP 8: REQUEST LOAN")
        print("="*60)

        # Navigate to loan request
        page.get_by_role("link", name="Request Loan").click()

        loan_page = LoanRequestPage(page)

        # Loan details
        loan_amount = "5000.00"
        down_payment = "500.00"

        print(f"Requesting loan of ${loan_amount} with down payment ${down_payment}")

        loan_page.apply_for_loan(
            amount=loan_amount,
            down_payment=down_payment,
            from_account=from_account
        )

        # Verify loan request processed
        expect(loan_page.loan_status).to_be_visible(timeout=10000)
        loan_status = loan_page.get_loan_status()
        print(f"✓ Loan request processed: {loan_status}")

        # ===== STEP 9: UPDATE CONTACT INFORMATION =====
        print("\n" + "="*60)
        print("STEP 9: UPDATE CONTACT INFORMATION")
        print("="*60)

        # Navigate to update contact info
        page.get_by_role("link", name="Update Contact Info").click()

        update_profile_page = UpdateProfilePage(page)

        # Wait for form to load
        expect(page.locator('[id="customer.firstName"]')).not_to_be_empty(timeout=10000)

        # Update contact information
        new_phone = "555-999-8888"

        print(f"Updating phone number to: {new_phone}")

        update_profile_page.update_contact_information(
            first_name="Sahil",
            last_name="Singh",
            street="456 Oak Avenue",
            city="Patna",
            state="Bihar",
            zip_code="800001",
            phone_number=new_phone
        )

        # Verify profile updated
        update_profile_page.verify_profile_updated_successfully()
        print(f"✓ Contact information updated successfully")

        # ===== STEP 10: USER LOGOUT =====
        print("\n" + "="*60)
        print("STEP 10: USER LOGOUT")
        print("="*60)

        update_profile_page.logout_user()

        # Verify logout - should be on login page
        expect(page.locator("input[name='username']")).to_be_visible()
        print(f"✓ User logged out successfully")

        # ===== E2E TEST COMPLETION =====
        print("\n" + "="*60)
        print("E2E TEST COMPLETED SUCCESSFULLY!")
        print("="*60)
        print("\nAll steps executed successfully:")
        print("  1. ✓ User Registration")
        print("  2. ✓ User Login")
        print("  3. ✓ Open New Account")
        print("  4. ✓ View Account Overview")
        print("  5. ✓ Transfer Funds")
        print("  6. ✓ Find Transactions")
        print("  7. ✓ Bill Payment")
        print("  8. ✓ Request Loan")
        print("  9. ✓ Update Contact Info")
        print(" 10. ✓ User Logout")
        print("="*60 + "\n")