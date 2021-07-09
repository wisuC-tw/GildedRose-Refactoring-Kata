# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item = self.update_quality_each(item)

    def update_quality_each(self, item):
        if item.name == "Aged Brie":
            item = self.update_quality_aged_brie(item)
        elif "Backstage passes" in item.name:
            item = self.update_quality_backstage_pass(item)
        elif "Conjured" in item.name:
            item = self.update_quality_conjured_item(item)
        else:
            item = self.update_quality_normal_item(item)

        item.sell_in -= 1
        item.quality = max(min(item.quality, 50), 0)

        return item

    def update_quality_normal_item(self, item):
        if item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality -= 2
        return item

    def update_quality_conjured_item(self, item):
        if item.sell_in > 0:
            item.quality -= 2
        else:
            item.quality -= 4
        return item

    def update_quality_aged_brie(self, item):
        item.quality += 1
        return item

    def update_quality_backstage_pass(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1
        return item


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
