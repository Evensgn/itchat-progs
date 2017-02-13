# wechat_autoreply.py 使用说明
## 简单介绍
这是一个实现微信个人账号自动回复的Python程序，使用[@LittleCoder](https://github.com/littlecodersh)开源的WeChat的Python接口[itchat](https://github.com/littlecodersh/ItChat)。是
可以实现针对特定的好友分别设置不同的自动回复内容，并可以使用第二个微信账号作为控制账号向应用此程序的账号发送控制命令进行各项功能的控制。
若没有第二个微信账号，也可以通过类似文件导入的方式，使用文件设置希望设定的自动回复列表，但无法进行方便的各种功能控制。

## 控制命令列表
使用控制账号向应用此程序的账号发送下列命令可以实现各种功能的控制：
```
- /help                         Show this table
- /autoreply off                Turn off auto-reply
- /autoreply on                 Turn on auto-reply
- /autodict reset               Reset auto-reply dictionary
- /autodict show                Show auto-reply dictionary
- /autodict add [A] [B]	        Add an auto-reply item for [A] as [B]
- /autodict del [A]             Delete the auto-reply item for [A]
- /autodict load [file]         Load auto-reply dictionary from [file]
- /autodict save [file]         Save auto-reply dictionary to [file]
- /autoprefix set [A]      	    Set auto-reply prefix as [A]
- /autoprefix off               Hide auto-reply prefix
- /autoprefix on                Show auto-reply prefix
- /remindmsg off                Turn off message reminder
- /remindmsg on                 Turn on message reminder
```

## 初始设置
在下面这段代码中：
```python
# The admin-account controls the auto-reply
adminRemarkName = 'Evensgn-R'

# default settings
autoReply = True
showAutoPrefix = True
remindMessage = True
# default auto-reply prefix
autoPrefix = '[Auto Reply] '
```
- adminRemarkName的初始值应设定为控制账号在应用此程序的微信账号中的备注
- 下方的几个布尔赋值语句为不同开关设置初始值
- autoPrefix为自动回复的前缀
