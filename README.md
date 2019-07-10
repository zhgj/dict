# dict

在linux终端上查英文单词意思，直接敲命令 dict 加要查的单词就行了，如：`dict english`

## 配置使用

1.`dict.py` 下载到linux机器

2.在`/usr/local/bin/`创建一个名为`dict`软链接指向`dict.py`.(不一定是`/usr/local/bin/`,也可能是`/usr/bin/`,不清楚的话可以执行'dict',会报找不到'dict',此时前面会有一个路径).软链接创建命令'sudo ln -s dict.py的全路径 dict'

3.把`dict.py`改为可执行文件.改为可执行文件命令'chmod +x dict.py的全路径'

4.输入`dict 单词1 单词2`就可以用了

## 目前支持

* iciba
* youdao

## 欢迎扩展

如果需要其他的翻译方请提出或自己扩展
