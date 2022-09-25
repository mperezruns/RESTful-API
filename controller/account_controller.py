from flask import Blueprint, request

from exception.acc_not_found_error import AccountNotFoundError
from exception.customer_not_found import CustomerNotFoundError
from model.account import Account
from service.account_service import AccountService

ac = Blueprint('account_controller', __name__)

account_service = AccountService()

@ac.route('/accounts')
def get_accounts():
    return {
        "accounts": account_service.get_accounts()
    }