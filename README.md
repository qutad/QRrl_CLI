# QRrl CLI

A simple command-line application that converts a URL into a QR code image.

## Features
- Accepts a URL from the terminal  
- Validates that the URL starts with `http://` or `https://`  
- Generates a QR code image (`qrcode.png`) in the current directory  
- Lightweight and easy to use  

## Requirements

Before running the program, install the required library:

```bash
pip install qrcode[pil]
```
You also need Python 3 installed.

How to Use

Run the script:

```bash
python qrrl_cli.py
```

## Output File

The generated QR code will be saved as:
```
qrcode.png
```


## Notes

- The URL must start with `http://` or `https://`
- Typing `q` or `quit` exits the program
