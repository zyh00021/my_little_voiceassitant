import speech_recognition as sr
from pynput import keyboard
import threading
import queue

class VoiceInput:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.operation_timeout = 0.5  # 减少超时时间
        self.recognizer.pause_threshold = 0.5  # 减少静音检测时间
        self.is_recording = False
        self.audio = None
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        self.result_queue = queue.Queue()
        # 麦克风预热
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)  # 减少预热时间
    
    def on_press(self, key):
        if key == keyboard.Key.space and not self.is_recording:
            self.is_recording = True
            print("开始录音...")
            self.audio_thread = threading.Thread(target=self.record_audio)
            self.audio_thread.start()
    
    def on_release(self, key):
        if key == keyboard.Key.space and self.is_recording:
            self.is_recording = False
            print("结束录音...")
    
    def record_audio(self):
        with sr.Microphone() as source:
            self.audio = self.recognizer.listen(source, phrase_time_limit=3)  # 限制最长录音时间
    
    def recognize_audio(self):
        try:
            text = self.recognizer.recognize_google(
                self.audio, 
                language='zh-CN',
                show_all=False  # 不返回所有可能结果
            )
            self.result_queue.put(text)
        except Exception as e:
            self.result_queue.put(None)
            print(f"识别错误: {e}")
    
    def listen(self):
        try:
            while self.audio is None and self.is_recording:
                pass
            if self.audio:
                recognition_thread = threading.Thread(target=self.recognize_audio)
                recognition_thread.start()
                recognition_thread.join(timeout=2)  # 减少等待时间
                
                if not self.result_queue.empty():
                    text = self.result_queue.get()
                    if text:
                        print(f"你说: {text}")
                    self.audio = None
                    return text
                return None
            return None
        except KeyboardInterrupt:
            print("录音被用户中断")
            self.is_recording = False
            self.audio = None
            return None