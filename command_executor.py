import os
import subprocess

class CommandExecutor:
    def __init__(self):
        self.functions = {
            "打开文件": "打开指定路径的文件",
            "运行程序": "运行指定的应用程序",
            "启用AI": "启用AI聊天功能",
            "你能干什么": "查询语音助手的功能",
            "退出": "退出语音助手程序"
        }
    #在这里你可以添加自己经常想打开的文件or软件位置。
    def execute(self, command):
        try:
            structured_command = command
            if "打开文件" in structured_command:
                path = structured_command.replace("打开文件", "").strip()
                os.startfile(path)
                return f"已打开文件 {path}"
            elif "运行程序" in structured_command:
                app = structured_command.replace("运行程序", "").strip()
                subprocess.Popen(app)
                return f"已运行程序 {app}"
            elif "记事本" in structured_command:
                subprocess.Popen("notepad.exe")
                return "已打开记事本"
            elif "浏览器" in structured_command:
                os.startfile("http://")
                return "已打开浏览器"
            elif "邮箱" in structured_command:
                os.startfile("mailto:")
                return "已打开邮箱"
            elif "你能干什么" in structured_command:
                return "我可以:\n" + "\n".join([f"- {k}: {v}" for k, v in self.functions.items()])
            elif "退出" in structured_command:
                return "正在退出..."
            else:
                return "无法识别的指令"
        except Exception as e:
            return f"指令处理失败: {str(e)}"