from models.store import StoreModel
from tests.unit.unit_base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store(self):
        store = StoreModel('test')

        self.assertEqual(store.name, 'test', "The name of the store after creation does not equal constructor argument.")
