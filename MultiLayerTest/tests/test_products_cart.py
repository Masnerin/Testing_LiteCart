import pytest
from .data_providers import valid_customers


@pytest.mark.parametrize("customer", valid_customers, ids=[repr(x) for x in valid_customers])
def test_product_in_the_cart(app, customer):
    for i in range(3):
        app.product_selection()
        app.product_in_cart()
    app.clean_the_cart()


