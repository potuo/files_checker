# Files_checker
[ :us: ](https://gitee.com/potuo/files_checker/blob/master/README.en.md)
#### 介绍
对于一组文件与目录的校验工具

#### 使用说明

> 创建校验文件:
> `python files_checker.py -m [folder]`

- -m [folder]	创建文件与文件夹列的校验文件
- -c [file1] [file2]	对比两个生成的校验文件

对一个目录进行校验文件生成后,可手动更改校验文件名称,在需要进行校验时再次对此目录进行校验文件生成,然后对比两个校验文件即可