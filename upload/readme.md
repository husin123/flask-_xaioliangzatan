# 使用
- 激活虚拟环境后 python app.py
- 访问 http://127.0.0.1:3030/

# 报错
- ImportError: cannot import name 'secure_filename'
- 解决如下
  
```
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
```