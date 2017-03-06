#coding =utf-8
import os
import urllib
import urllib.request
import re


def download_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '

                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    htm = response.read()
    return htm


def get_image(html):
    regx = r'src="(http://[\S]*\.jpg)" '
    pattern = re.compile(regx)
    get_image = re.findall(pattern, repr(html))
    dir_path = 'D:\\test'
    path = '\\1'
    image_path = dir_path + path
    if not os.path.isdir(image_path):
        os.makedirs(image_path)
    count = 1
    for img in get_image:
        if 'tianjimedia' not in img:
            image_dir = image_path + '\\' + '{}.jpg'.format(count)
            image = download_page(img)
            with open(image_dir, 'wb') as fp:
                fp.write(image)
                count += 1
                print('图片%s下载完成' % count)
    return

url = 'http://pic.yesky.com/451/106166451.shtml'
url2 = 'https://tieba.baidu.com/p/2460150866'

html = download_page(url)
get_image(html)
