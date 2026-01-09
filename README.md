# 🚀 Smart QR Code Generator

A smart and user-friendly QR Code generator built with Python. It doesn't just create QR codes; it also validates and fixes your URLs to ensure they work perfectly.



## ✨ Features
- **Smart URL Validation:** Checks if your link has `http://`, `https://`, or `www.` and offers to add them automatically.
- **TLD Checker:** Ensures your link ends with a valid extension like `.com`, `.net`, etc.
- **Unique Filenames:** Uses Unix timestamps to prevent overwriting old QR codes.
- **User-Friendly:** Interactive command-line interface with English prompts.

## 🛠️ Requirements
To run this project, you need the `qrcode` library installed with Pillow support:

```bash
pip install qrcode[pil]

## 🚀 How to Use
1. Clone this repository.
2. Install requirements: `pip install qrcode[pil]`
3. Run the script: `python qrcode_gen.py`
4. Enter your link and follow the prompts!
