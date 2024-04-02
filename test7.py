import pyttsx3

# 初始化
engine = pyttsx3.init()

# 要转换的文本
text = "he error message you're seeing indicates that the Python pyttsx3 package is trying to load the libespeak.so.1 shared library, which is part of the espeak text-to-speech engine, but it cannot find it on your system. This usually means that espeak is not installed or not properly set up."

# 设置属性，例如语速和音量
engine.setProperty('rate', 150)    # 语速
engine.setProperty('volume', 0.9)  # 音量

# 选择语言和声音（这里是中文）
voices = engine.getProperty('voices')
for voice in voices:
    if 'chinese' in voice.name:
        engine.setProperty('voice', voice.id)
        break

# 进行朗读
engine.say(text)
engine.runAndWait()
