from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont
from highlight import Highlight
import random

class DisplayControler:
    self.WIDTH = 800
    self.HEIGHT = 480
    self.H_MARGIN = 30
    self.V_MARGIN = 30
    self.FONT_SIZE = 24
    self.LINE_PADDING = 6
    self.FONT_LOC = "resources//DejaVuSerif.ttf"
    #TODO seperate displayhiglight into various class functions
    def __init__(self):
        self.display = auto()

    def displayHighlight(self, highlight):

        # Load the image and resize it to fit screen
        try:
            img = Image.open(f"resources//{b.title}.jpg")
        except:
            img = Image.open("resources//nightSkytest.png")
        img = img.resize((self.WIDTH, self.HEIGHT)) # TODO move elsewhere

        # Get the width and height of the image
        width, height = img.size

        # Create a new ImageDraw object
        draw = ImageDraw.Draw(img)

        # Define the font and size for the text
        textFont = ImageFont.truetype(self.FONT_LOC, self.FONT_SIZE)
        titleFont = ImageFont.truetype(self.FONT_LOC, round(self.FONT_SIZE*0.6))
        authorFont = ImageFont.truetype(self.FONT_LOC, round(self.FONT_SIZE*0.4))

        # display book title and author
        authors = ', '.join(highlight.book.authors)

        length = max(titleFont.getlength(highlight.book.title), authorFont.getlength(author))
        authorHeight = titleFont.getbbox(author)[3]
        titleHeight = titleFont.getbbox(highlight.book.title)[3] + authorHeight

        # draw highlight text
        draw.text(
            (self.WIDTH - self.H_MARGIN - self.length, 
            self.HEIGHT - self.V_MARGIN - titleHeight), 
            highlight.book.title, 
            font=titleFont, fill=(255, 255, 0)
            )
        # draw authors and book title
        draw.text(
            (self.WIDTH - self.H_MARGIN - self.length, 
            self.HEIGHT - self.V_MARGIN - authorHeight),
            author, 
            font=authorFont, fill=(255, 255, 0)
            )

        # Wrap the text to fit on the image
        lines = []
        words = str(highlight.text).replace('\n',' ').split(' ')
        currentLine = words[0]
        # for each word in the highlight
        for word in words[1:]:
            # if the current line plus the next word is shorter than the image width minus the hoizontal padding
            if textFont.getlength(currentLine + " " + word) < width - (self.H_MARGIN * 2):
                # add word to current line
                currentLine += " " + word
            else:
                # end current line and start next line
                lines.append(currentLine)
                currentLine = word
        lines.append(currentLine)

        # Draw the text on the image
        #yText = height - (len(lines) * 30) # adjust the 30 value to set the line spacing
        yText = self.V_MARGIN
        # for each line
        for line in lines:
            # get witdth and hiehgt of line
            lineWidth, lineHeight = textFont.getbbox(line)[2:]
            xText = self.H_MARGIN
            draw.text((xText, yText), line, font=textFont, fill=(255, 255, 255))
            yText += lineHeight

        # Save the image with the text
        #img.save("resources//imageOut.png")
        display.set_image(img)
        display.show()

