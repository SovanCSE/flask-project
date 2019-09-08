import MySQLdb


class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', 'welcome',
                                    'hotel_livedb', charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        print("item===", item)
        return item