import unittest

from usermanager import UserManager

class CheckUserManager(unittest.TestCase):
        def test_user_registration(self):
                user_manager = UserManager()
                
                user_manager.register_user('Alan')
                self.assertEqual(user_manager.users[2].get_name(),'Alan')
                
                user_manager.register_user('Alan')
                self.assertEqual(len(user_manager.users),3)

                user_manager.register_user('Tyler')
                self.assertEqual(len(user_manager.users),4)

                user_manager.register_user('Tyler')
                self.assertEqual(len(user_manager.users),4)

unittest.main()
