import unittest
from main import Steg
import matplotlib.pyplot as plt
import numpy as np
#TODO: write full unittests

TEXT_PATH = '../data/tests/test_load_text.txt'
IMAGE_PATH  = '../data/tests/test_img.png'

class Package_test(unittest.TestCase):

    def test_load_data(self):
        s = Steg() 
        with open(TEXT_PATH, 'w') as f:
            f.write(s.letters)
        data = s.load_text(TEXT_PATH)
        nums = [i for i in range(len(s.letters))]
        for file_num, original in zip(data, nums):
            self.assertEqual(file_num, original)

    def test_encrypt(self):
        s = Steg()
        # Setup
        input_text =\
        '''This is the test string:.,20394872ad;lfkhsaz()'''
        with open(TEXT_PATH, 'w') as f:
            f.write(input_text)
        setup_image = np.zeros((10, 10, 3), dtype=np.uint8)
        s.save_img(IMAGE_PATH, setup_image)
        # Test
        image = s.load_img(IMAGE_PATH)
        data = s.load_text(TEXT_PATH)
        custom_indexes = [4, 5]
        data_in_img = s.encrypt(image, data, custom_indexes)
        output_text = s.decrypt_img(data_in_img, custom_indexes)
        for input_char, output_char in zip(input_text, output_text):
            self.assertEqual(input_char, output_char)


if __name__ == "__main__":
    unittest.main()