Let us MAKE SEVEN GRATE AGAIN！！！！！！！

Run this command to build

打包为一个exe文件
uv run pyinstaller --onefile --windowed --name "MyAppexe" --additional-hooks-dir=./pyinstaller_hooks --collect-all PySide6 --collect-all blivedm --paths ./src src/main.py

dll单独放到lib中
uv run pyinstaller --windowed --name "MakeSevenGreatAgain" --additional-hooks-dir=./pyinstaller_hooks --collect-all PySide6 --collect-all blivedm --paths ./src src/main.py

待添加WeChatPYAPI
待添加nonebot2和go-cqhttp

待做功能：
界面显示弹幕列表
超过一定时间自动隐藏过往消息

