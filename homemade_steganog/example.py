# Example usage
from .steg import Steg

img_path = '/Users/andrewarderne/work/homemade_steg/data/iu.jpeg'
data_path = '/Users/andrewarderne/work/homemade_steg/data/text.txt'
s = Steg()
s.load_img(img_path)
s.load_data(data_path)
data_in_img = s.encrypt()

# Send image here

message = s.decrypt_img(data_in_img)
print(message)