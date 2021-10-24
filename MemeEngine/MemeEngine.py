"""Meme Engine Module."""

import random
from PIL import Image, ImageDraw, ImageFont
import textwrap

class MemeEngine():
    """Responsible for manipulating and drawing text onto images."""

    def __init__(self, output_dir: str):
        """Create a class instance.
        
        :params: the output path 
        :returns: the path for the outputted meme
        """
        self.output_dir = output_dir

    def make_meme(self, img_path: str, text: str, author: str, width: int=500) -> str:
        """Create a meme with a quote on an image.
        
        :params: 
            img_path: location of input image
            text: quote body
            author: quote author
            width: width to resize image
        :returns: the location of the outputted meme as a string
        """
        #Resize the image to input width unless it is zero or greater than 500
        img_width = 500 if width == 0 else width if width < 500 else 500
        try:
            with Image.open(img_path) as image:
                height = round((width/image.width) * image.height)
                image_resized = image.resize((width, height), Image.NEAREST)
        except:
            print('Error opening image')

        try:
            if text is not None:
                #Set font
                font = ImageFont.truetype('../static/fonts/Rubik-SemiBold.ttf', size=20)
                #Add padding to the image
                padding_size = 30 if width > 200 else 40 if width > 300 else 5
                #Draw the body text on the image allowing multiple lines
                draw = ImageDraw.Draw(image_resized)
                start_height = padding_size
                lines = textwrap.wrap(text, width=40)
                for line in lines:
                    line_width, line_height = font.getsize(line)
                    draw.text((padding_size, start_height), 
                        line, font=font, fill='white', stroke_width=1, stroke_fill='black')
                    start_height += line_height
                #Draw the author name
                draw.text((padding_size, start_height+5), 
                        author, font=font, fill='white', stroke_width=1, stroke_fill='black')
                #Save the image
                out_path = f'{self.output_dir}/{random.randint(0,100000000)}.jpg'
                image_resized.save(out_path)
                return out_path
        except:
            print('Error creating the meme')
