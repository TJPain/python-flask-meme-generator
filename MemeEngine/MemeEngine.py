"""Meme Engine Module."""

import random
from PIL import Image, ImageDraw, ImageFont

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
                height = ((img_width/image.width) * image.height)
                image_resized = image.resize((width, height))
        except:
            print('Error opening image')  

        try:
            if text is not None:
                draw = ImageDraw.Draw(image_resized)
                font = ImageFont.truetype('./fonts/Rubik-SemiBold.ttf', size=20)
                #Add padding to the image
                padding_size = 20 if width > 200 else 5                
                #Draw the text on the image
                draw.multiline_text((padding_size, random.randint(padding_size, height/2)), f'{text}\n{author}', font=font, fill='white', stroke_fill='black')
                out_path = f'{self.output_dir}/{random.randint(0,100000000)}.jpg'
                image_resized.save(out_path)
                return out_path
        except:
            print('Error creating the meme')
