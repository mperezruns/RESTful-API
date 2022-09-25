import psycopg
from model.account import Account

class AccountDao:

    def get_accounts(self):
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj_api", user="postgres",
                             password='@zul@8') as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM accounts')

                account_list = []

                for acc in cur:
                    a_id = acc[0]
                    account_type = acc[1]
                    balance = acc[2]
                    customer_id = acc[3]

                    my_acc_obj = Account(a_id, account_type, balance, customer_id)
                    account_list.append(my_acc_obj)

                return account_list