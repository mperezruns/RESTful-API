import dao.customer_dao
from exception.customer_not_found import CustomerNotFoundError
from exception.customer_exists import CustomerAlreadyExistsError
from model.customer import Customer
from service.customer_service import CustomerService
import pytest

def test_get_all_customers(mocker):
    # ARRANGE
    def mock_get_all_customers(self):
        return [Customer(1, 'Nicholas Albro', 'Nicholas', 'Albro', '572-945-7688', 'ogtempuraa'), Customer(2, 'Nicholas Jung', 'Nicholas', 'Jung', '818-352-0900', 'nickjung9')]
    # ARRANGE
    mocker.patch('dao.customer_dao.CustomerDao.get_all_customers', mock_get_all_customers)
    customer_service = CustomerService()
    # ACT
    actual = customer_service.get_all_customers()
    # ASSERT
    assert actual == [
        {
            "id": 1,
            "customername": "Nicholas Albro",
            "first_name": "Nicholas",
            "last_name": "Albro",
            "customerphone": "572-945-7688",
            "username": "ogtempuraa"
        },
        {
            "id": 2,
            "customername": "Nicholas Jung",
            "first_name": "Nicholas",
            "last_name": "Jung",
            "customerphone": "818-352-0900",
            "username": "nickjung9"
        }
    ]