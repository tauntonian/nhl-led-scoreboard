from PIL import Image, ImageFont, ImageDraw, ImageSequence
from rgbmatrix import graphics
from utils import center_text
from renderer.screen_config import screenConfig

DrawOffDay.test()

class DrawOffDay:
    """docstring for ."""

    def __init__(self, matrix, data):
        self.matrix = matrix
        self.data = data
        self.screen_config = screenConfig("64x32_config")
        self.canvas = matrix.CreateFrameCanvas()
        self.width = 64
        self.height = 32

        self.image = Image.new('RGB', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)

        self.font = ImageFont.truetype("fonts/score_large.otf", 16)
        self.font_mini = ImageFont.truetype("fonts/04B_24__.TTF", 8)

    def test(self):
        self.draw.text((0, -1), 'NO GAME TODAY :(', font=self.font_mini)
        self.canvas.SetImage(self.image, 14, 25)
        self.canvas = self.matrix.SwapOnVsync(self.canvas)
