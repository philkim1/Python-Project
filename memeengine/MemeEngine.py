from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine():
    """This is the MemeEngine class."""

    def __init__(self, output):
        self.output = output

    def make_meme(self,
                  img_path,
                  text,
                  author,
                  width=500) -> str:  # generated image path
        img = Image.open(img_path)

        if width is not None:
            ratio = img.size[0]/img.size[1]
            height = int(width/ratio)
            img = img.resize((width, height), Image.NEAREST)

        if text is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()
            text = text.replace('"', '').strip()
            author = author.strip()
            line = f'"{text}"' + ' - ' + author
            draw.text((20, 10), line, font=font, fill='white')

        path = self.output + f'/{random.randint(0, 999999)}.png'

        img.save(path)

        return path
