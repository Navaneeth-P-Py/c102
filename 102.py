import cv2
from time import time
from random import randint
import dropbox

start_time = time()

def take_snapshot():
    num = randint(1,100)
    #video capture object from cv2
    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(num) + ".png"
        cv2.imwrite(img_name,frame)
        #start_time = time()
        result = False
        return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BF6Z7MZ5e0VO-dWamlBSV2PLwfjFbkwDXlrknQKa7VRsUZYEJh__pHyL9M_Kd9zvgVhnguMaREVCx0rPHHdtrmbuBa9IER-vHra0VrKN6MXZLHJduEkWhQQZ6czTK6XJuEMSwgXgfKup"
    file_from = img_name
    file_to = "/Python/" + img_name
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if ((time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()
