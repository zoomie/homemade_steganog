.. homemade_steganog documentation master file, created by
   sphinx-quickstart on Fri Feb  1 16:56:52 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

homemade_steganog
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. autoclass:: main.Steg
  :members:

Purpose
=======
The purpose of steganography is concealing
particular data in normal data. In this module,
the particular data is a message while the
normal data is an image.

As can be seen in the simple example below,
the message can be hidden in the image using
the encrypt method and removed at its endpoint
using the decrypt method.

Simple example
==============
Sending a text file hidden in an image::

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

.. image:: ../data/data_in_img.png
    :width: 600px
    :align: center
    :height: 400px

On the second users machine::

    from homemade_steganog import Steg
    s_new = Steg()
    # Recieve data_in_img
    data_in_img = s_new.load_img('../data/data_in_img.png')
    message = s_new.decrypt_img(data_in_img)

Custom example
==============
Using custom_indexs specifies the locations
(pixel indexes) where each digit of the message
is hidden::

    img_path = '../data/img.jpeg'
    data_path = '../data/short_story.txt'
    s = Steg()
    image = s.load_img(img_path)
    data = s.load_text(data_path)

    custom_indexs = [145, 82, 39, 94, 109]
    data_in_img = s.encrypt(image, data, custom_indexs)
    s.save_img('../data/data_in_img.png', data_in_img)
    # Send image here

    # New machine
    s_new = Steg()
    img = s_new.load_img('../data/data_in_img.png')
    message = s_new.decrypt_img(data_in_img, custom_indexs)


License
=======

    .. include:: ../LICENSE

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
