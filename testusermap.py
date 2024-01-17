import unittest
from usermap import UserMap, PasswordError

class TestUserMap(unittest.TestCase):
    def setUp(self):
        self.um = UserMap()

    def test_add_user(self):
        self.um.add_user("user1", "password1")
        self.assertEqual(len(self.um), 1)
        self.assertTrue("user1" in self.um)

    def test_add_existing_user(self):
        self.um.add_user("user1", "password1")
        with self.assertRaises(RuntimeError):
            self.um.add_user("user1", "password2")

    def test_update_password(self):
        self.um.add_user("user1", "password1")
        self.assertTrue("user1" in self.um)

        self.um.update_password("user1", "password1", "newpassword")
        record = self.um["user1"]
        self.assertEqual(record.password_hash, record._hash_password(record.salt, "newpassword"))

    def test_update_password_with_wrong_password(self):
        self.um.add_user("user1", "password1")
        with self.assertRaises(PasswordError):
            self.um.update_password("user1", "wrongpassword", "newpassword")

    def test_update_password_nonexistent_user(self):
        with self.assertRaises(KeyError):
            self.um.update_password("nonexistent_user", "password", "newpassword")

if __name__ == "__main__":
    unittest.main()
