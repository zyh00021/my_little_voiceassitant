from config import GLMConfig
import requests

class AIChat:
    def chat(self, prompt):
        headers = {
            "Authorization": f"Bearer {GLMConfig.API_KEY}",
            "Content-Type": "application/json"
        }
        
        # 标准化指令转换
        if "将以下自然语言指令转换为标准化命令" in prompt:
            command = prompt.replace("将以下自然语言指令转换为标准化命令: ", "")
            standardized_prompt = f"将以下指令转换为标准格式:\n1. 打开文件 [路径]\n2. 运行程序 [程序名]\n3. 记事本\n4. 浏览器\n5. 邮箱\n6. 你能干什么\n7. 退出\n\n原始指令: {command}"
            data = {
                "model": GLMConfig.MODEL_NAME,
                "messages": [{"role": "user", "content": standardized_prompt}]
            }
        else:
            data = {
                "model": GLMConfig.MODEL_NAME,
                "messages": [{"role": "user", "content": prompt}]
            }
            
        response = requests.post(GLMConfig.API_URL, headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"]