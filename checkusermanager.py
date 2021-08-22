import unittest

from usermanager import UserManager

class CheckUserManager(unittest.TestCase):
        def test_user_registration(self):
                user_manager = UserManager()
                
                user_manager.register_user('Alan')
                self.assertEqual(user_manager.users[0].name,'Alan')
                
                user_manager.register_user('Alan')
                self.assertEqual(len(user_manager.users),1)

                user_manager.register_user('Tyler')
                self.assertEqual(len(user_manager.users),2)

                user_manager.register_user('Tyler')
                self.assertEqual(len(user_manager.users),2)

unittest.main()
