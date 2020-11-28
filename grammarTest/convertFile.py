# import pandas
import os


def convert_file(file_dir, new_dir, desc_type, previous_type):
    error_list = list()
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # try:
            #     df1 = pandas.read_csv(file_path,encoding=previous_type)
            #     new_path = os.path.join(new_dir,file)
            #     df1.to_csv(new_path,encoding=desc_type)
            # except Exception as e:
            #     print(e)
            #     print("file :{}  open is error and continue".format(file_path))
            #     error_list.append(file_path)
            #     continue
            try:
                with open(file_path, "rb") as f:
                    res = f.read().decode(previous_type)  # decode 是将二进制bytes编码转换为unicode,
                with open(os.path.join(new_dir, file), "w", encoding=desc_type) as f:  # encode 是将unicode编码转换为其他编码
                    f.write(res)
            except Exception as e:
                print("file :{} because error : [{}] continue".format(file, e))
                error_list.append(file)
        print(error_list)


if __name__ == '__main__':
    # 如果想要知道原始文件的格式,使用notepad++打开文件,右下角有文件的编码格式
    file_dir = '‪C:/Users/33054/Desktop/新建文本文档.txt'  # 存放原文件数据的目录
    new_dir = "C:/Users/33054/Desktop/新建文本文档01.txt"  # 存放新数据的目录
    desc_type = "utf-8"  # 新文件的格式
    previous_type = "utf-16-le"  # UCS-2 Little Endian(即 utf-16)  # 新文件的原格式
    convert_file(file_dir, new_dir, desc_type, previous_type)
