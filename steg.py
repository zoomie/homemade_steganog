import skimage
from skimage import data
from skimage.io import imread
from numpy import array
from random import randint as r
import numpy as np
import matplotlib.pyplot as plt

# img = imread('/Users/andrewarderne/work/homemade_encryption/steganog/iu.jpeg')

class Steg:
    def __init__(self):
        self.settings = dict()
        self.letters = """
                        abcdefghijklmnopqrstuvwxyz ,.:-'"?;()!
                       """
        # Sending variables
        self.normal_img = None
        self.encode_data = None
        self.flat_img = None
        self.encode_indexs = None
        self.data_img = None

        # Recieving variables
        self.hidden_img = None
        self.decode_data =  None

    def load_img(self, img_path):
        self.normal_img = imread(img_path)

    def load_data(self, data_path):
        with open(data_path, 'r') as f:
            data = f.read().lower()
        self.encode_data = self._char_to_num(data)

    def encrypt(self):
        self.encode_indexs = self._create_indexs(self.normal_img, self.encode_data)
        self.data_img = self._input_data(self.normal_img, 
                                         self.encode_indexs, 
                                         self.encode_data)
        return self.data_img

    def _char_to_num(self, chars):
        nums = list()
        char_num = {char: num for num, char in enumerate(self.letters)}
        for char in chars:
            if char in '1234567890': continue
            # num = char_num.get(char, 33)
            num = char_num[char]
            nums.append(num)
        return nums

    def _create_indexs(self, img, data, div=116*2):
        indexs = list()
        position = 0
        print(img.shape)
        xs, ys, zs = img.shape
        for x in range(xs):
            for y in range(ys):
                for z in range(zs):
                    position += 1
                    if position%div==0:
                        indexs.append((x, y, z))
                    if len(indexs) == len(data):
                        return indexs


    def _input_data(self, img, encode_indexs, data):
        for num, (x, y, z) in enumerate(encode_indexs):
            # print(img[x][y][z], data[num])
            img[x][y][z] = data[num]
        return img

    def decrypt_img(self, img, encode_indexs):
        data = list()
        for x, y, z in encode_indexs:
            data.append(img[x, y, z])
        message = self._num_to_char(data)
        return ''.join(message)
    
    def _num_to_char(self, nums):
        chars = list()
        num_char = {num: char for num, char in enumerate(self.letters)}
        for num in nums:
            chars.append(num_char[num])
        return chars


img_path = '/Users/andrewarderne/work/homemade_encryption/data/iu.jpeg'
data_path = '/Users/andrewarderne/work/homemade_encryption/data/text.txt'
s = Steg()
s.load_img(img_path)
s.load_data(data_path)
other_img = s.encrypt()
plt.imshow(other_img)
plt.show()

# secret_message = s.decrypt_img(data_img, s.encode_indexs)
# print(secret_message)
