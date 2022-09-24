from flask import Blueprint, request

from model.customer import Customer
from service.customer_service import CustomerService

cc = Blueprint('customer_controller', __name__)

# Instantiate a CustomerService Object
customer_service = CustomerService()

# FIRST ENDPOINT
@cc.route('/customers')
def get_all_customers():
    return {
        "customers": customer_service.get_all_customers()
    }