#!/usr/bin/env python3

from PIL import Image
from Crypto.Cipher import AES
from Crypto import Random
from argparse import ArgumentParser

def encrypt_image(image, key, iv=b''):
    image_array = bytes(image.tostring())
    padding_length = AES.block_size - len(image_array) % AES.block_size
    image_array += bytes(padding_length * ".", "UTF-8") # Just an arbitrary padding byte

    mode = AES.MODE_CBC if iv else AES.MODE_ECB
    aes = AES.new(key, mode, iv)

    encrypted_image = aes.encrypt(image_array)
    encrypted_image = encrypted_image[:-padding_length]

    return Image.fromstring("RGB", image.size, encrypted_image, "raw", "RGB")

if __name__ == "__main__":
    parser = ArgumentParser(description="Encrypt images with AES ECB/CBC")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-cbc", "--cbc", action="store_true")
    group.add_argument("-ecb", "--ecb", action="store_true")

    parser.add_argument("input_file", help="Input file")
    parser.add_argument("output_file", help="Output file")
    args = parser.parse_args()

    image = Image.open(args.input_file).convert('RGBA').convert('RGB') # The example Tux.png is in palette mode with transparency, and needs to be converted to RGBA first
                                                                       # TODO: Find a better way to do this in a general way

    key = Random.new().read(AES.key_size[0])

    if args.ecb:
        encrypt_image(image, key).save(args.output_file)
    else:
        iv = Random.new().read(AES.block_size)
        encrypt_image(image, key, iv).save(args.output_file)

