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

    def load_data(self, data):
        self.encode_data = self._char_to_num(data)

    def encrypt(self):
        self.encode_indexs = self._create_indexs(self.encode_data)
        self.data_img = self._input_data(self.normal_img, 
                                         self.encode_indexs, 
                                         self.encode_data)
        return self.data_img

    def _char_to_num(self, chars):
        nums = list()
        letters= 'abcdefghijklmnopqrstuvwxyz '
        char_num = {char: num for num, char in enumerate(letters)}
        for char in chars:
            nums.append(char_num[char])
        return nums

    def _create_indexs(self, data, div=20):
        num = len(data)*div
        xs = [i for i in range(num) if i%div==0]
        indexs = list()
        for x in xs:
            indexs.append((x, 10, 1))
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
        letters = 'abcdefghijklmnopqrstuvwxyz '
        num_char = {num: char for num, char in enumerate(letters)}
        for num in nums:
            chars.append(num_char[num])
        return chars


data = "what ever lfdagsd"
s = Steg()
s.load_img('/Users/andrewarderne/work/homemade_encryption/steganog/iu.jpeg')
s.load_data(data)
data_img = s.encrypt()

plt.imshow(data_img)
plt.show()

secret_message = s.decrypt_img(data_img, s.encode_indexs)
print(secret_message)
