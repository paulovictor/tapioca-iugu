# coding: utf-8
import pytest

from tapioca_iugu.tapioca_iugu import IuguClientAdapter


def test_resource_access(api_client):
    resource = api_client.customer_list()
    assert resource.data == 'https://api.iugu.com/v1/customers'


iterator_data = [
    ({},
     {'totalItems': 730, 'items': ['item'] * 100},
     {'params': {'start': 100}}),

    ({'params': {'start': 100}},
     {'totalItems': 730, 'items': ['item'] * 100},
     {'params': {'start': 200}}),

    ({'params': {'start': 700}},
     {'totalItems': 730, 'items': ['item'] * 100},
     None),
]


@pytest.mark.parametrize('request_kwargs, response_data, expected', iterator_data)
def test_resource_pagination_arguments(request_kwargs, response_data, expected):
    client = IuguClientAdapter()
    result = client.get_iterator_next_request_kwargs(request_kwargs, response_data, None)

    assert result == expected
