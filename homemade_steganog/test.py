import unittest
from main import Steg


class Package_test(unittest.TestCase):

    def test_integration(self):
        input_text = 'this is a small test'
        s = Steg()
        s.load_data('../data/small.txt')
        s.load_img('../data/img.jpeg')
        img = s.encrypt()
        output_text = s.decrypt_img(img)
        self.assertEqual(input_text, output_text)


if __name__ == "__main__":
    unittest.main()