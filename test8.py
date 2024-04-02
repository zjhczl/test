# 文字转语音
from gtts import gTTS

# 要转换的文本
# text5 = "位置信息正在初始化，请等待上方所有指示灯变为绿色"
# text6 = "网络连接断开，请刷新平板，如果还是不行，则重启设备"
text = "位置信息初始化完成，可以开始测图啦"
# 选择语言
language = 'zh-cn'

# 将文本转换成语音
speech = gTTS(text=text, lang=language, slow=False)

# 保存语音文件
speech.save("7.mp3")
