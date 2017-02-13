# wechat_autoreply.py 使用说明
## 简单介绍
这是一个实现微信个人账号自动回复的Python程序，使用[@LittleCoder](https://github.com/littlecodersh)开源的WeChat的Python接口[itchat](https://github.com/littlecodersh/ItChat)。

可以针对特定的好友分别设置不同的自动回复内容，并可以通过向**文件传输助手**发送控制命令进行各项功能的控制。可以将自动回复列表保存到文件，也可以从文件导入自动回复列表。
### 自动回复Demo
![autoreply-demo-0](demo/autoreply-demo-0.jpg) ![autoreply-demo-1](demo/autoreply-demo-1.jpg)
## 控制命令列表
在本程序的命令中均使用好友的**备注名**识别好友账号。
使用控制账号向应用此程序的账号发送下列命令可以实现各种功能的控制：
```
/help                         Show this table
/autoreply off                Turn off auto-reply
/autoreply on                 Turn on auto-reply
/autodict reset               Reset auto-reply dictionary
/autodict show                Show auto-reply dictionary
/autodict add [A] [B]	      Add an auto-reply item for [A] as [B]
/autodict del [A]             Delete the auto-reply item for [A]
/autodict load [file]         Load auto-reply dictionary from [file]
/autodict save [file]         Save auto-reply dictionary to [file]
/autoprefix set [A]      	  Set auto-reply prefix as [A]
/autoprefix off               Hide auto-reply prefix
/autoprefix on                Show auto-reply prefix
```
### 控制命令Demo
![autoreply-control-demo](demo/autoreply-control-demo.jpg)
## 初始设置
在下面这段代码中进行初始设置：
```python
# default settings
autoReply = True
showAutoPrefix = True
# default auto-reply prefix
autoPrefix = '[Auto Reply] '

# autoReply: 是否进行自动回复
# showAutoPrefix: 是否在自动回复消息前添加前缀
# autoPrefix: 自动回复的前缀
```

## 编辑自动回复列表存储文件
在需要批量添加自动回复或回复内容较长时，使用控制命令逐条添加较为繁琐，可以直接将自动回复列表保存到一个文件中，再使用**'/autodict load [file]'**命令从文件导入自动回复列表，在文件中存储自动回复列表的格式如下：
```
<item><name>好友A备注</name><text>对A的自动回复内容</text></item>
<item><name>好友B备注</name><text>对B的自动回复内容</text></item>
<item><name>好友C备注</name><text>对C的自动回复内容</text></item>
```
