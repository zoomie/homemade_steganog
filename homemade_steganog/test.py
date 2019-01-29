import unittest
from steg import Steg


class Package_test(unittest.TestCase):

    def test_steg(self):
        input_text = 'a string of text'
        s = Steg()
        s.encode_data = s._char_to_num('a string of text')
        s.load_img('../data/img.jpeg')
        img = s.encrypt()
        output_text = s.decrypt_img(img)
        self.assertEqual(input_text, output_text)


if __name__ == "__main__":
    unittest.main()