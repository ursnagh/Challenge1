from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings

class Challenge1Pipeline:
    settings = get_project_settings()
    item_count = 0
    def process_item(self, item, spider):
        if self.item_count >= self.settings['ITEMCOUNT'] and self.settings['ITEMCOUNT'] != 0:
            raise DropItem(
                "ITEMCOUNT limit has been reached - " + str(self.settings['ITEMCOUNT']))
        else:
            self.item_count += 1
            pass
        return item
