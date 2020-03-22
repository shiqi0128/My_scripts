# url = "https://qa.api.gmall.gaopeng.com/api/camera/upload"
        # with open(r"C:\Users\html_\Pictures\GMALL1图片/2.jpg", "rb")as f:
        #     form_data = {"image_face": ("2.jpg", f, "jpg/png"), "date": (None, "2018-02-12 13:25:26"),
        #                  "camera_code": (None, "GP_SH_005")}
        #     response = requests.post(url=url, files=form_data).json()
        #     print(response)





        # form_data = {"image_face": ("2.jpg", f, "jpg/png"), "date": (None, "2018-02-12 13:25:26"),
        #              "camera_code": (None, "GP_SH_005")}
        # form_data = {"images[]": (str(img_name) + ".jpg", photo, "jpg/png"), "date": (None, jd_time[1])}  # 只接受元组格式