def upload():
    file_name = ["1.png", "2.png", "3.jpg", "4.png"]
    for name in file_name:
        with open(r"C:\Users\gp002\Pictures\photo" + name, "rb") as f:
            files = {
                "image_face": (name, f, "jpg/png"),
                "camera_code": (None, "GP_SH_003"),
                "date": (None, "2018-11-12 13:25:26")
            }  # 读取文件赋值给file

    return