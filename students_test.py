import unittest
from students import Students


# hall nadaram test benivasam bashe bara bad hahahaha
class TestStudent(unittest.TestCase):
    def test_add_score(self, score):
        with self.assertRaises(ValueError):
            return score == int(score)
        
if __name__ == "__main__":
    unittest.main()