# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_quality_should_not_be_negative(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_quality_should_drop_twice_as_fast_after_sell_date_passed(self):
        items = [Item("foo", 0, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_should_increases_in_quality(self):
        items = [Item("Aged Brie", 1, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_quality_never_more_than_50(self):
        items = [Item("Aged Brie", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_should_not_update(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_pass_should_increase_quality_by_1_when_sellin_more_than_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_backstage_pass_should_increase_quality_by_2_when_sellin_less_than_or_equal_to_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_backstage_pass_should_increase_quality_by_3_when_sellin_less_than_or_equal_to_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(13, items[0].quality)
    
    def test_backstage_pass_should_drop_quality_to_0_when_sellin_equal_to_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    @unittest.skip("new feature not implemented skip for now")
    def test_conjured_item_should_degrade_in_quality_twice_as_fast(self):
        items = [Item("Conjured foo", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured foo", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
