from skimage.io import imread
from random import randint 


class Steg:
    """
    This class encodes text data into an 
    image. 
    """
    def __init__(self):
        self.letters =\
        """0123456789abcdefghijklmnopqrstuvwxyz ,.:-'"?;()!"""
        self.input_img = None
        self.encode_data = None
        self.data_img = None
        self.char_num = None

    def load_img(self, img_path):
        """
        Input the path to the image file
        """
        self.input_img = imread(img_path)

    def load_data(self, data_path, ending_numbers=None):
        """
        Input path to the txt file.
        Add the number of digits to the
        start of the data.
        """
        with open(data_path, 'r') as f:
            data = f.read().lower()
        data_in_nums = self._char_to_num(data)
        if not ending_numbers:
            ending_numbers = [0, 99]
        self.encode_data = data_in_nums + ending_numbers

    def _char_to_num(self, chars):
        nums = list()
        char_num = {char: num for num, char in enumerate(self.letters)}
        char_num['\n'] = int(len(self.letters)+1)
        char_num['\t'] = int(len(self.letters)+2)
        for char in chars:
            num = char_num[char]
            nums.append(num)
        return nums

    def encrypt(self, num_generator=None):
        """
        The encrypt methods encoded the data into
        the image by changing pixels value, the index 
        is chosen base on the random number generator.
        The encryption and decryption methods must both
        use the same num_generator.
        """
        index_gen = self._yield_indexs(self.input_img, 
                                       num_generator)
        data_in_img = self._input_data(self.input_img, 
                                       self.encode_data, 
                                       index_gen)
        return data_in_img

    def _yield_indexs(self, img, num_generator=None):
        if not num_generator:
            num_generator = self.default_num_generator()
        indexs = list()
        position = 0
        num = 0
        xs, ys, zs = img.shape
        for x in range(xs):
            for y in range(ys):
                for z in range(zs):
                    if position == num:
                        yield x, y, z
                        position = 0
                        num = next(num_generator)
                    position += 1

    def _input_data(self, img, data, index_gen):
        # zip loops to the lenght of the smallest 
        # iterable, therefore it will stop at the 
        # end of data
        for digit, (x, y, z) in zip(data, index_gen):
            img[x][y][z] = digit
        return img

    def decrypt_img(self, img, num_generator=None):
        """
        Extracts text from the image.
        """
        if not num_generator:
            num_generator = self.default_num_generator()
        index_gen = self._yield_indexs(img, num_generator)
        data = list()
        for i, (x, y, z) in enumerate(index_gen):
            data.append(img[x, y, z])
            if i > 10 and data[i] == 99 and data[i-1] == 0:
                # Remove the ending values
                data = data[:-2]
                break
        message = self._num_to_char(data)
        return ''.join(message)
    
    def _num_to_char(self, nums):
        chars = list()
        num_char = {num: char for num, char in enumerate(self.letters)}
        num_char[int(len(self.letters)+1)] = '\n'
        num_char[int(len(self.letters)+2)] = '\t'
        for num in nums:
            chars.append(num_char[num])
        return chars

    def default_num_generator(self):
        """
        The following generator specifies where the 
        index of the encoded data.
        """
        while True:
            yield 184