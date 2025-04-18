import pyttsx3

class VoiceOutput:
    def __init__(self):
        self.engine = pyttsx3.init()
        # 设置更自然的语音参数
        self.engine.setProperty('rate', 150)  # 适中语速
        self.engine.setProperty('volume', 0.9)  # 音量(0-1)
        self.engine.setProperty('pitch', 110)  # 音调(50-200)
        
        # 尝试获取最佳语音引擎
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'chinese' in voice.languages or 'zh' in voice.languages:
                self.engine.setProperty('voice', voice.id)
                break
    
    def speak(self, text):
        # 添加自然停顿
        sentences = text.split('。')
        for sentence in sentences:
            if sentence.strip():
                self.engine.say(sentence.strip())
                self.engine.runAndWait()
                self.engine.setProperty('rate', 150)  # 重置语速