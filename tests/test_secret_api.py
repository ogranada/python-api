"""Test calling the Shotgun API server secret endpoints.
"""

import unittest

import base


class TestServerSecretAPI(base.TestBase):

    def setUp(self):
        """
        Set up the test to use a session token, which is the only way the server secret API
        can be used.
        """
        super(TestServerSecretAPI, self).setUp(auth_mode="SessionToken")

    def test_retrieve_same_id(self):
        """
        Ensures asking for a key twice returns the same result.
        """
        secret_key = self.sg.retrieve_ws_server_secret("12345")
        another_secret_key = self.sg.retrieve_ws_server_secret("12345")
        self.assertTrue("ws_server_secret" in secret_key)
        self.assertEqual(secret_key, another_secret_key)

    def test_bad_id(self):
        """
        Ensures invalid payloads generate an error.
        """
        self.assertRaises(
            Exception,
            self.sg.retrieve_ws_server_secret,
            ("",)
        )
        self.assertRaises(
            Exception,
            self.sg.retrieve_ws_server_secret,
            (1,)
        )

        self.assertRaises(
            Exception,
            self.sg.retrieve_ws_server_secret,
            ({},)
        )

        self.assertRaises(
            Exception,
            self.sg.retrieve_ws_server_secret,
            (None,)
        )

    def test_retrieve_diffrent_id(self):
        """
        Ensures the same session can provide two different server ids.
        """
        secret_key = self.sg.retrieve_ws_server_secret("12345")
        another_secret_key = self.sg.retrieve_ws_server_secret("56789")

        self.assertTrue(isinstance(secret_key["ws_server_secret"], str))
        self.assertTrue(isinstance(another_secret_key["ws_server_secret"], str))

        self.assertNotEqual(
            secret_key["ws_server_secret"],
            another_secret_key["ws_server_secret"]
        )


if __name__ == '__main__':
    unittest.main()
