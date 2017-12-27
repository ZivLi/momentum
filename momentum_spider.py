# coding: utf-8
import re
import os
import urllib
from multiprocessing.pool import ThreadPool

MOMENTUM_URL = 'https://d3cbihxaqsuq0s.cloudfront.net/'


def spider():
    context = urllib.urlopen(MOMENTUM_URL).read()
    return context


def parse_context(c):
    image_keys = re.findall(r'\<Key\>(.+?)\<\/Key\>', c)
    return [
        MOMENTUM_URL + key for key in image_keys
    ]


def main():
    context = spider()
    images = parse_context(context)[1:]

    pool = ThreadPool(6)
    pool.map(save_img, images)
    pool.close()
    pool.join()
    

def save_img(img_url, file_path='/Users/ziv/Downloads/momentums'):
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_suffix = os.path.basename(img_url)
        filename = '{}{}{}'.format(file_path, os.sep, file_suffix)
        urllib.urlretrieve(img_url, filename=filename)
        print filename
    except IOError as e:
        print e
    except Exception as e:
        print e


if __name__ == '__main__':
    import time
    s = time.time()
    main()
    print 'finished.'
    print time.time() - s

