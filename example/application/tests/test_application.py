# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import requests


def test_example():
    host = "127.0.0.1:8000"
    url = 'http://{}/admin/'.format(host)
    response = requests.get(url)
    assert response.status_code == 200
    assert "Error" not in response.text

def test_error():
    assert False
