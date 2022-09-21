import psycopg
from model.customer import Customer

class CustomerDao:
    # CRUD Operations
    # Create -- insert a new user into my "database"
    # Read -- Retrieve a user or users into my "database"
    # Update -- Update a user in my "database"
    # Delete -- Delete a user in my "database"

    def get_all_customers(self):
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj_api", user="postgres",
                             password='@zul@8') as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM customers')

                my_list_of_cus_objs = []
                for cus in cur:
                    c_id = cus[0]
                    customername = cus[1]
                    first_name = cus[2]
                    last_name = cus[3]
                    customer_phone = cus[4]
                    username = cus[5]

                    my_cus_obj = Customer(c_id, customername, first_name, last_name, customer_phone, username)
                    my_list_of_cus_objs.append(my_cus_obj)

                return my_list_of_cus_objs