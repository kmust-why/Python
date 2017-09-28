
from tkinter import *
from tkinter.filedialog import *
import urllib.request

def upload():
    #print('1')
    filename = askopenfilename()
    print(filename)
    file = open(filename,'rb').read()
    data = '''------WebKitFormBoundaryJavbhG60tiqa7MGH
Content-Disposition: form-data; name="file"; filename="%s"
Content-Type: text/plain

[file]
------WebKitFormBoundaryJavbhG60tiqa7MGH--''' %filename.split('/')[-1]
    data = bytes(data)
    data = data.replace(bytes('[file]'),file)
    req = urllib.request
    req.add_head('Content-Type','multipart/form-data; boundary=----WebKitFormBoundaryJavbhG60tiqa7MGH')
    html = req.urlopen('http://127.0.0.1:8080/upload/',data=data).read()

    text.delete(0,END)
    text.insert(END,html)


def download():
    print('3')

root = Tk()
root.title('文件分享软件')
root.geometry('+400+300')

text = Entry(width=50)
text.grid()
btn_upload = Button(text='上传',command=upload)
btn_upload.grid()
btn_download = Button(text='下载',command=download)
btn_download.grid()
root.mainloop()