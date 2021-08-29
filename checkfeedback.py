import unittest

from feedback import Feedback

class CheckFeedback(unittest.TestCase):
        def test_feedback(self):
                feedback = Feedback('CODE','FEEDBACK')

                self.assertEqual(feedback.get_code_entered(),'CODE')
                
                self.assertEqual(feedback.get_feedback_given(),'FEEDBACK')

unittest.main()
