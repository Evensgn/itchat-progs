#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests, itchat
from itchat.content import *
import re

# default settings
autoReply = True
showAutoPrefix = True
# default auto-reply prefix
autoPrefix = '[Auto Reply] '
autoDict = {}

def underlineToSpace(s):
	rs = ''
	for c in s:
		if c == '_':
			rs += ' '
		else:
			rs += c
	return rs

@itchat.msg_register([TEXT, PICTURE, RECORDING], isGroupChat = False)
def reply(msg):
	global autoReply
	global showAutoPrefix
	global autoPrefix
	global autoDict
	# react to message from yourself
	if msg['ToUserName'] == 'filehelper':
		arg = re.compile(' ').split(msg['Text'])
		nonSense = False
		try:
			if arg[0] == '/help':
				reply = '''[Help Information]
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
				'''
			elif arg[0] == '/autoreply':
				if arg[1] == 'off':
					autoReply = False
					reply = 'Turn off auto-reply.'
				elif arg[1] == 'on':
					autoReply = True
					reply = 'Turn on auto-reply.'
				else:
					nonSense = True
			elif arg[0] == '/autodict':
				if arg[1] == 'reset':
					autoDict = {}
					reply = 'Reset auto-reply dictionary.'
				elif arg[1] == 'show':
					reply = '[Auto-reply Dictionary]'
					for k in autoDict:
						reply += '\n[' + k + '] ' + autoDict[k]
				elif arg[1] == 'add':
					autoDict[arg[2]] = underlineToSpace(arg[3])
					reply = 'Add an auto-reply item for \'' + arg[2] + '\'.'
				elif arg[1] == 'del':
					autoDict.pop(arg[2])
					reply = 'Delete the auto-reply item for \'' + arg[2] + '\'.'
				elif arg[1] == 'load':
					fileName = arg[2]
					with open(fileName, 'r') as inFile:
						allText = inFile.read()
					pattern = re.compile('<item><name>(.*?)</name><text>(.*?)</text></item>', re.S)
					items = re.findall(pattern, allText)
					autoDict = {}
					for item in items:
						autoDict[item[0]] = item[1]
					reply = 'Load auto-reply dictionary from file \'' + fileName + '\'.'
				elif arg[1] == 'save':
					fileName = arg[2]
					allText = ''
					for k in autoDict:
						allText += '<item><name>' + k + '</name><text>' + autoDict[k] + '</text></item>\n'
					with open(fileName, 'w') as outFile:
						outFile.write(allText)
					reply = 'Save auto-reply dictionary to file \'' + fileName + '\'.'
				else:
					nonSense = True
			elif arg[0] == '/autoprefix':
				if arg[1] == 'set':
					autoPrefix = underlineToSpace(arg[2])
					reply = 'Set auto-reply prefix as \'' + autoPrefix + '\'.'
				elif arg[1] == 'off':
					showAutoPrefix = False
					reply = 'Hide auto-reply prefix \'' + autoPrefix + '\'.'
				elif arg[1] == 'on':
					showAutoPrefix = True
					reply = 'Show auto-reply prefix \'' + autoPrefix + '\'.'
				else:
					nonSense = True
		except:
			nonSense = True
		if nonSense:
			reply = 'Use /help to view help information.'
		itchat.send(reply, toUserName = 'filehelper')
	# if message is from other accounts
	else:
		friend = itchat.search_friends(userName = msg['FromUserName'])
		if friend:
			remarkName = friend['RemarkName']
		# if cannot find this friend
		else:
			remarkName = 'RemarkName Error'
		reply = ''
		# auto-reply
		if autoReply:
			if remarkName in autoDict:
				if showAutoPrefix:
					reply = autoPrefix
				reply += autoDict[remarkName]
		itchat.send(reply, msg['FromUserName'])

itchat.auto_login(enableCmdQR = True)
itchat.run()
