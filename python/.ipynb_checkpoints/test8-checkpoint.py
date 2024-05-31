# 文字转语音
from gtts import gTTS

# 要转换的文本
# text5 = "位置信息正在初始化，请等待上方所有指示灯变为绿色"
# text6 = "网络连接断开，请刷新平板，如果还是不行，则重启设备"
text = "当前位置不合适,请移动到挡墙八到十米处开始测量"
# 选择语言
language = 'zh-cn'

# 将文本转换成语音
speech = gTTS(text=text, lang=language, slow=False)

# 保存语音文件
speech.save("8.mp3")
