from constants import BG

class ScrollBackground():
      def __init__(self, bg_img, moving_speed = 3):
            self.bgimage = bg_img
            self.rectBGimg = self.bgimage.get_rect()

            self.bgY1 = 0
            self.bgX1 = 0

            self.bgY2 = - self.rectBGimg.height
            self.bgX2 = 0

            self.moving_speed = moving_speed

      def update(self):
        self.bgY1 += self.moving_speed
        self.bgY2 += self.moving_speed
        if self.bgY1 >= self.rectBGimg.height:
            self.bgY1 = - self.rectBGimg.height
        if self.bgY2 >= self.rectBGimg.height:
            self.bgY2 = - self.rectBGimg.height

      def render(self, CANVAS):
         CANVAS.blit(self.bgimage, (self.bgX1, self.bgY1))
         CANVAS.blit(self.bgimage, (self.bgX2, self.bgY2))

bg_obj = ScrollBackground(BG)
slow_bg_obj = ScrollBackground(BG, 1.5)
