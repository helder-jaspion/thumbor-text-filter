#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import ImageDraw
from PIL import ImageFont
from thumbor.filters import BaseFilter, filter_method


class Filter(BaseFilter):
    def str2rgb(s):
        rgba = s.split(",")
        if len(rgba) not in (3, 4):
            return (0, 0, 0)
        return tuple(map(int, rgba))

    @filter_method(
        BaseFilter.String,#word
        BaseFilter.PositiveNumber,#posX
        BaseFilter.PositiveNumber,#posY
        BaseFilter.String,#color name see: http://pillow.readthedocs.io/en/4.0.x/reference/ImageColor.html#color-names
        BaseFilter.PositiveNumber, #font-size
        BaseFilter.String, #font-family
    )
    def text(self, word, x, y, color, font_size, font_family="Arial"):
        image = self.engine.image
        usr_font = ImageFont.truetype(font_family, font_size)
        drawer = ImageDraw.Draw(image)
        color2 = str2rgb(color)
        drawer.text((x, y), word, fill=color2, font=usr_font)
        self.engine.image = image
