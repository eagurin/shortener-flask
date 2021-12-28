import random
import string
import unittest

from app import app

app.testing = True


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_url(self):
        data = {"url": "https://google.com/"}
        response = self.app.post("/_short", json=data)
        self.assertEqual(response.status_code, 201)

    def test_create_custom_url(self):
        shorten = "Test"
        data = {"url": "https://google.com/", "shorten": shorten}
        response = self.app.post("/_short", json=data)
        self.assertEqual(response.status_code, 201)

    def test_create_existing_url(self):
        shorten = hashed()
        data = {"url": "https://google.com/", "shorten": shorten}
        self.app.post("/_short", json=data)
        response = self.app.post("/_short", json=data)
        self.assertEqual(response.status_code, 400)

    def test_redirect_url(self):
        data = {"url": "https://google.com/"}
        response_create = self.app.post("/_short", json=data)
        response = self.app.get(response_create.json["shorten"])
        self.assertEqual(response.status_code, 302)


if __name__ == "__main__":
    unittest.main()
