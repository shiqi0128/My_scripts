from urllib3 import encode_multipart_formdata

def fenzhuang(filename, filepath, **kwargs):
    files = {"image": (filename, open(filepath, "rb").read(), "jpg/png")}  # 读取文件赋值给file
    encode_data = encode_multipart_formdata(files)  # encode_multipart_formdata是导入的一个方法,这个方法下面的文件赋值给encode_data
    data_file = encode_data[0]  # encode的返回结果第一个值是上传的文件
    header_data = \
        {
            "Content-Type": encode_data[1],  # 指要上传文件的方式，输出encode_data的结果，头部变更为第2个值才能上传
            # "Authorization": "Bearer df6ffc7f56271c3b079e3d79381b02704e2d50d4"
        }
    kwargs = {"camera_code": "GP_SH_003", "image_face": data_file, "date": "2017-12-12 09:00:00"}
    return kwargs