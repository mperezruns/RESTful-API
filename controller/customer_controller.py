from flask import Blueprint, request

from service.customer_service import CustomerService
from model.customer import Customer

cc = Blueprint('customer_controller', __name__)

# Instantiate a CustomerService Object
customer_service = CustomerService()

# FIRST ENDPOINT
@cc.route('/customers')
def get_all_customers():
    return {
        "customers": customer_service.get_all_customers()
    }