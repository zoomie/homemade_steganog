# Example usage
import matplotlib.pyplot as plt
# from homemade_steganog import Steg
from main import Steg

img_path = '../data/img.jpeg'
data_path = '../data/short_story.txt'
s = Steg()
image = s.load_img(img_path)
data = s.load_text(data_path)

custom_indexs = [145, 82, 39, 94, 109]
data_in_img = s.encrypt(image, data, custom_indexs)
s.save_img('../data/data_in_img.png', data_in_img)
# Send image here
plt.imshow(data_in_img)
plt.show()

# New machine
s_new = Steg()
img = s_new.load_img('../data/data_in_img.png')
message = s_new.decrypt_img(data_in_img, custom_indexs)
print(message)
