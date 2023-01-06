# Watermark-image

A simple Python script that adds a watermark to an image.

## Requirements

- Python 3
- PIL (Python Imaging Library)

## Usage

1. Clone the repository:
```
git clone https://github.com/GivenBY/Watermark-image.git
```
2. Install the required Dependencies.
```
pip3 install -r requirements.txt
```
3. Navigate to the directory:
```
cd Watermark-image
```
4. Run the script:
```
python watermark.py
```

5. Follow the prompts to enter the file path of the image you want to watermark, the watermark message, and the color of the watermark text.

6. The watermarked image will be saved with the name "Output.png" in the same directory as the script.

7. (Optional) Choose a font file by placing it in the same directory and making changes in the `watermark.py` file.
    ImageFont.truetype(`"FreeMono.ttf"`, 40) make the changes according to your font file name.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
