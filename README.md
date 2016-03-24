# Requirements
Ubuntu packages:
    python3-crypto
    python3-pil

# Usage
  $ ./encrypt_image.py -h
    usage: encrypt_image.py [-h] (-cbc | -ecb) input_file output_file

    Encrypt images with AES ECB/CBC

    positional arguments:
      input_file   Input file
      output_file  Output file

    optional arguments:
      -h, --help   show this help message and exit
      -cbc, --cbc
      -ecb, --ecb

# Examples
Encrypt Tux in ECB mode:
  $ ./encrypt_image.py --ecb Tux.png Tux_ecb.png

Encrypt Tux in CBC mode:
  $ ./encrypt_image.py --cbc Tux.png Tux_cbc.png

Example image taken from https://commons.wikimedia.org/wiki/File:Tux.png
