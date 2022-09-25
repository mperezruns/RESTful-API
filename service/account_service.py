from dao.account_dao import AccountDao

class AccountService:

    def __init__(self):
        self.account_dao = AccountDao()

    def get_accounts(self):
        list_of_accounts = self.account_dao.get_accounts()
        return list(map(lambda a: a.to_dict(), list_of_accounts))
