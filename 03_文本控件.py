import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

# 1. 创建应用程序
app = QApplication(sys.argv)

# 2. 创建窗口
w = QWidget()
# ----------------------------------------------------
w.setWindowTitle("文本展示")

label = QLabel()
label.setText("这是第一个文本")
# 将文本添加到窗口
label.setParent(w)

# ----------------------------------------------------
# 3. 显示窗口
w.show()

# 4. 等待窗口停止
sys.exit(app.exec_())