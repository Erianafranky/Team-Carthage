import os
import unittest



class AddBookTestCase(unittest.TestCase):
    def test_empty_fields_registration(self, username, password,confirm):
        app = User()
        result = app.register('', '','Pearson', '')
        self.assertEqual(result, "Error fields cannot be empty")

    def test_incorect_password(self,username, password):
        app = User()
        result = app.logink('admin', 'bad password')
        self.assertEqual(result, "Password error")

    def test_empty_comment(self):
        app = User()
        pass

    def test_unexpected_input(self):
        pass

if __name__ == '__main__':
    unittest.main()