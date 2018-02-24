# pyqiniu
对七牛云api封装了一些项目中比较实用的工具函数

# 安装环境
```
python 2.7.10
pip install qiniu==7.0.8
```
# 使用方法
配置好access_key、secret_key和bucket_name.
```
import pyqiniu

# 文件
file_path = u"/Users/ouyang/Desktop/新增测试/净空法师/封面.jpg"

# 上传, 返回key
key = pyqiniu.upload(file_path)
print key

# 获取文件key
key = pyqiniu.get_key(file_path)
print key

# 判断文件是否存在
is_exist = pyqiniu.check_file_exist(file_path)
print is_exist

```
