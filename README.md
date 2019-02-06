# homemade_steganog
[Documentation](https://homemade-steganog.readthedocs.io/en/latest/)

```
pip install homemade-steganog
```
Example:
```python
from homemade_steganog import Steg

img_path = '../data/img.jpeg'
data_path = '../data/text.txt'
s = Steg()
image = s.load_img(img_path)
data = s.load_text(data_path)
data_in_img = s.encrypt(image, data)

from matplotlib.pyplot as plt
plt.imshow(data_in_img)
plt.show()
```
![alt text](https://github.com/zoomie/homemade_steg/blob/master/data/img.jpeg)

```python
from homemade_steganog import Steg
s_new = Steg()
# Recieve data_in_img
data_in_img = s_new.load_img('../data/data_in_img.png')
message = s_new.decrypt_img(data_in_img)
```
#### The following text was encoded into the photo show above.

How can entropy be reversed
The Last Question by Isaac Asimov 1956

The last question was asked for the first time, half in jest, on May 21, 2061, at a time when humanity first stepped into the light. The question came about as a result of a five dollar bet over highballs, and it happened this way:

Alexander Adell and Bertram Lupov were two of the faithful attendants of Multivac. As well as any human beings could, they knew what lay behind the cold, clicking, flashing face -- miles and miles of face -- of that giant computer. They had at least a vague notion of the general plan of relays and circuits that had long since grown past the point where any single human could possibly have a firm grasp of the whole.

Multivac was self-adjusting and self-correcting. It had to be, for nothing human could adjust and ...

The full short story can be found in [this file.](https://github.com/zoomie/homemade_steganog/blob/master/data/short_story.txt)
