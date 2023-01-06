from PIL import Image, ImageDraw, ImageFont

file_path = input("Enter the path: ")
msg = input("Enter a Msg: ")

# Get the color
color = tuple(map(int, input("Enter Color RGB Color Seperated By space(" "): ").split(" ")))

with Image.open(file_path) as im:

    # Get the width and height of the image
    width, height = im.size
    draw = ImageDraw.Draw(im)

    # Load the font or Change the font You Wish to use
    font = ImageFont.truetype("FreeMono.ttf", 40)
    \
    x, y, w, h = draw.textbbox((0, 0), msg, font=font)

    x = (width - w) / 2
    y = (height - h) / 2
    
    draw.multiline_text((x, y), msg, font=font, fill=color, align="center")

    im.save("Output.png", "PNG")
