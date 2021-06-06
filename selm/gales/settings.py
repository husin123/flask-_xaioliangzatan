from pathlib import Path
import os

# 项目根目录
root_path = Path(os.path.dirname(
    os.path.dirname((os.path.abspath(__file__)))))

# 项目目录
project_path = root_path / "gale"

# data目录
DATA_DIR = project_path / "data"

# 测试cookies储存目录
TEST_COOKIES_PATH = project_path / "test" / "test_data" / "cookies.json"
