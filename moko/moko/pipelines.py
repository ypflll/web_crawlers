#refer to: https://segmentfault.com/a/1190000003870052#articleHeader0

import requests
import os
from moko.items import MokoItem
from moko import settings

class MokoPipeline(object):

    def process_item(self, item, spider):
        images = []
        dir_path = '%s/%s/%s' % (settings.IMAGES_STORE, spider.name, spider.name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        if 'url' in item:
            us = item['url'].split('/')[3:]
            image_file_name = '_'.join(us)
            file_path = '%s/%s' % (dir_path, image_file_name)
            images.append(file_path)

                    
            with open(file_path, 'wb') as handle:
                response = requests.get(item['url'], stream=True)
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)

        item['images'] = images
        return item


















