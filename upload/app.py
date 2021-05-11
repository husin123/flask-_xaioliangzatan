import os

from flask import Flask, render_template, request
from flask_uploads import DOCUMENTS, IMAGES, UploadSet, configure_uploads

app = Flask(__name__)
files = UploadSet('files')
# 上传的配置
app.config['UPLOADED_FILES_DEST'] = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "data")  # 配置文件保存的目录，本参数必须设置；
app.config['UPLOADED_FILES_ALLOW'] = [
    DOCUMENTS, IMAGES, 'sav']  # 配置允许的扩展名，其他的都是不允许
app.config['UPLOADED_FILES_DENY'] = ['html']  # 配置不允许的扩展名

configure_uploads(app, files)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('main.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            # 将文件保存到指定位置
            files.save(request.files['file'])
            return render_template('main.html', info='上传成功')
        except Exception:
            return render_template('main.html', info='上传失败,不支持该类型文件')
    else:
        return render_template('main.html', info='请使用POST方法')


if __name__ == '__main__':
    app.run(port=3030)
