### 本脚本用于记录多级目录之间的脚本导入

```
├── ClearerVoice-Studio
│   ├── clearvoice
│   │   ├── clearvoice/ 
├── DeepFilterNet/
│   ├── .github/
│   ├── assets/
│   ├── DeepFilterNet/
│   │   ├── df/                # 目标模块
│   │   └── __pycache__/
│   └── ...
└── speech_prepro/
    ├── checkpoints/
    ├── output/
    └── your_script.py        # 您的脚本
```



### 1. 方式1

```
# 将ClearerVoice-Studio目录添加到Python路径
sys.path.append(os.path.abspath('/Bspace/henan/step2/ClearerVoice-Studio'))
from clearvoice import ClearVoice  # Import the ClearVoice class for speech processing tasks
```

### 2. 方法2

```
# 获取项目根目录（假设脚本在 speech_prepro/ 下）
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
```

