from voice_input import VoiceInput
from voice_output import VoiceOutput
from command_executor import CommandExecutor
from ai_chat import AIChat

class VoiceAssistant:
    def __init__(self):
        self.voice_input = VoiceInput()
        self.voice_output = VoiceOutput()
        self.command_executor = CommandExecutor()
        self.ai_chat = AIChat()
        self.ai_enabled = False

    def run(self):
        self.voice_output.speak("语音助手已启动")
        
        while True:
            command = self.voice_input.listen()
            if command:
                if "退出" in command:
                    self.voice_output.speak("语音助手正在退出")
                    break
                
                result = self.command_executor.execute(command)
                self.voice_output.speak(result)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()