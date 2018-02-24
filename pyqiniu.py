# coding=utf-8
from qiniu import Auth, put_file, etag
from qiniu import BucketManager  # 构建鉴权对象

access_key = "your-access-key"
secret_key = "your-secret-key"
bucket_name = 'your-bucket-name'


def upload(file_path):
    """
    上传文件
    :param file_path: 文件路径
    :return: key
    """
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 上传到七牛后保存的文件名
    key = None

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    # 要上传文件的本地路径
    ret, info = put_file(token, key, file_path)

    assert ret['hash'] == etag(file_path)
    return ret['key']


def get_img_info(img_url):
    """
    获取七牛上图片的基本信息：长宽、后缀
    :param img_url:
    :return: tuple(长、宽、后缀)
    """
    info_url = img_url + '?imageInfo'  # 基本信息
    import requests
    r = requests.get(info_url)
    body = r.content
    r.close()
    import json
    info_dic = json.loads(body)
    height = info_dic['height']
    width = info_dic['width']
    suffix = info_dic['format']
    return height, width, suffix


def get_key(file_path):
    """
    获取一个文件的key，七牛的算法是获取文件的hash值，使用的是 qiniu.etag()
    :param file_path:
    :return: key (str)
    """
    key = etag(file_path)
    return key


def check_file_exist(file_path):
    """
    判断key在你空间中存在
    :param file_path:
    :return: True False
    """
    key = get_key(file_path)

    # 初始化Auth状态
    q = Auth(access_key, secret_key)

    # 初始化BucketManager
    bucket = BucketManager(q)

    ret, info = bucket.stat(bucket_name, key)

    text_body = info.text_body
    if 'error' in text_body:
        return False
    return True


if __name__ == '__main__':
    # 文件
    file_path = u"/Users/ouyang/Desktop/新增测试/净空法师/封面.jpg"

    # 上传, 返回key
    key = upload(file_path)
    print key

    # 获取文件key
    key = get_key(file_path)
    print key

    # 判断文件是否存在
    is_exist = check_file_exist(file_path)
    print is_exist
