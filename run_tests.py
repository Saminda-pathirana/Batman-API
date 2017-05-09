import unittest
from tests import stores_tests
from run import app
import tempfile


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        """Initial code bits that needs to run before starting unit testing"""
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_store_endpoints(self):
        """Unit tests for store endpoints"""
        stores_tests.store_list_test(self)

if __name__ == "__main__":
    unittest.main()
