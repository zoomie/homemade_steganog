from skimage.io import imread
from random import randint 


class Steg:
    def __init__(self):
        self.settings = dict()
        self.letters =\
        """0123456789abcdefghijklmnopqrstuvwxyz ,.:-'"?;()!"""
        self.normal_img = None
        self.encode_data = None
        self.flat_img = None
        self.encode_indexs = None
        self.data_img = None
        self.char_num = None

    
    def load_img(self, img_path):
        self.normal_img = imread(img_path)

    def load_data(self, data_path):
        with open(data_path, 'r') as f:
            data = f.read().lower()
        self.encode_data = self._char_to_num(data)

    def encrypt(self):
        self.encode_indexs = self._create_indexs(self.normal_img, 
                                                 self.encode_data)
        self.data_img = self._input_data(self.normal_img, 
                                         self.encode_indexs, 
                                         self.encode_data)
        return self.data_img

    def _char_to_num(self, chars):
        nums = list()
        char_num = {char: num for num, char in enumerate(self.letters)}
        char_num['\n'] = int(len(self.letters)+1)
        char_num['\t'] = int(len(self.letters)+2)
        self.char_num = char_num
        for char in chars:
            num = char_num[char]
            nums.append(num)
        return nums

    def _create_indexs(self, img, data):
        indexs = list()
        position = 0
        num = 0
        generator = self._num_generator(img, data)
        xs, ys, zs = img.shape
        for x in range(xs):
            for y in range(ys):
                for z in range(zs):
                    if position == num:
                        indexs.append((x, y, z))
                        position = 0
                        num = next(generator)
                    position += 1
                    if len(indexs) == len(data):
                        return indexs  


    def _input_data(self, img, encode_indexs, data):
        for num, (x, y, z) in enumerate(encode_indexs):
            img[x][y][z] = data[num]
        return img

    def _num_generator(self, img, data):
        x, y, z = img.shape
        space_between_data = int((x*y*z)/len(data))
        largest_space = space_between_data + 10
        smallest_space = space_between_data - 40
        while True:
        #     yield 50
            yield randint(smallest_space, largest_space)

    def decrypt_img(self, img):
        data = list()
        for x, y, z in self.encode_indexs:
            data.append(img[x, y, z])
        message = self._num_to_char(data)
        return ''.join(message)
    
    def _num_to_char(self, nums):
        chars = list()
        num_char = {num: char for char, num in self.char_num.items()}
        for num in nums:
            chars.append(num_char[num])
        return chars
