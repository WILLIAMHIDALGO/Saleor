import pytest
import json
from unittest.mock import Mock
from uuid import uuid4

from django.contrib.auth.models import AnonymousUser
from prices import Money, TaxedMoney

from saleor.checkout import utils

from saleor.checkout.models import Cart


def test_get_cart_from_request(
    monkeypatch,
    customer_user,
    cart_request_factory,
    cart_with_item
):
    # 1-01
    empty_cart = Cart()
    mock_empty_cart = Mock(return_value=empty_cart)
    token_authenticated = uuid4()
    request_authenticated_user = cart_request_factory(user=customer_user, token=token_authenticated)
    monkeypatch.setattr(
        'saleor.checkout.utils.get_user_cart',
        mock_empty_cart
    )
    no_items_cart_authenticated = utils.get_cart_from_request(request_authenticated_user)
    assert no_items_cart_authenticated.quantity == 20
    # 1-02
    non_empty_cart = cart_with_item
    non_empty_cart.user = customer_user

    mock_cart = Mock(return_value=non_empty_cart)
    monkeypatch.setattr(
        'saleor.checkout.utils.get_user_cart',
        mock_cart
    )
    items_cart_authenticated = utils.get_cart_from_request(request_authenticated_user)
    assert items_cart_authenticated.quantity == 3

    # 1-03
    unauthenticated_user = AnonymousUser()
    token_unauthenticated = uuid4()
    request_unauthenticated_user = cart_request_factory(user=unauthenticated_user, token=token_unauthenticated)
    monkeypatch.setattr(
        'saleor.checkout.utils.get_anonymous_cart_from_token',
        mock_empty_cart
    )
    no_items_cart_unauthenticated = utils.get_cart_from_request(request_unauthenticated_user)
    assert no_items_cart_unauthenticated.quantity == 0

    # 1-04
    new_non_empty_cart = cart_with_item
    new_unauthenticated_user = AnonymousUser()
    new_token_unauthenticated = uuid4()
    new_request_unauthenticated_user = cart_request_factory(
        user=new_unauthenticated_user,
        token=new_token_unauthenticated
    )
    new_mock_cart = Mock(return_value=new_non_empty_cart)
    monkeypatch.setattr(
        'saleor.checkout.utils.get_anonymous_cart_from_token',
        new_mock_cart
    )
    items_cart_unauthenticated = utils.get_cart_from_request(new_request_unauthenticated_user)
    assert items_cart_unauthenticated.quantity == 3


def test_get_shipping_address_form(
    customer_user,
    default_country,
    cart_with_item,
    another_address
):
    # 2-02
    cart = cart_with_item
    cart.user = customer_user
    cart.shipping_address = another_address
    forms = utils.get_shipping_address_forms(
        cart,
        customer_user.addresses.all(),
        dict(),
        default_country
    )
    assert len(forms) == 3

    # 2-03
    new_cart = cart_with_item
    new_cart.user = customer_user
    new_cart.shipping_address = customer_user.addresses.first()
    forms = utils.get_shipping_address_forms(
        new_cart,
        customer_user.addresses.all(),
        dict(),
        default_country
    )
    assert len(forms) == 3

    # 2-04
    new_cart_2 = cart_with_item
    forms = utils.get_shipping_address_forms(
        new_cart_2,
        customer_user.addresses.all(),
        dict(),
        default_country
    )
    assert len(forms) == 3

