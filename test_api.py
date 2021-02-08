"""
    Unit tests for read root rout API
"""

import api
import requests


class TestAPI:
    def test_root(self):
        code = requests.get('http://127.0.0.1:8000')
        assert {'plataforma': 'Linux'} == api.root()
        assert 200 == code.status_code
