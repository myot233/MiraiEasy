import os
import md5list
import requests
import time
import sys
import easygui
import configparser


class main():
	def __init__(self):
		pass

	def main(self):
		che = check()
		print("如启动后报错，请删除java.ini")
		che.Checkmethod()

		# 检测文件
		#     检测是否为第一次使用
		#
		# 检查更新
		# 进入界面
		pass


class check():
	def __init__(self):
		self.cwd = os.getcwd()
		self.result = []

	def Checkmethod(self):
		if os.path.exists(self.cwd + '/libs'):
			print("已检测到文件夹")
			if self.checkjar():
				if not os.path.exists(self.cwd + "/java.ini"):
					s = easygui.diropenbox('选择java所在的文件夹', '文件对话框')
					lt = s + '\\java.exe'
					p = configparser.ConfigParser()
					p.add_section('java')
					p.set('java', 'java',lt)
					p.write(open("java.ini", 'w+'))
					print(lt)
					sth = os.system(f'''{lt} -cp "./libs/*" net.mamoe.mirai.console.pure.MiraiConsolePureLoader %*''')
					os.system('title Mirai Console')
					print(sth)

					pass
				else:

					p = configparser.ConfigParser()
					p.read(self.cwd + "/java.ini", encoding='utf-8')
					lt = p['java']['java']
					sth = os.system(f'''{lt} -cp "./libs/*" net.mamoe.mirai.console.pure.MiraiConsolePureLoader %*''')
					os.system('title Mirai Console')
					print(sth)
			else:

				self.getjar()
		else:
			os.mkdir(self.cwd + "\\libs")
			print('正在创建文件中...')
			self.result = [False, False, False]
			self.getjar()

	def getjar(self):
		print(1)
		adm = 0
		dir1 = self.cwd + "\\libs"

		def downloadFile(name, url):
			headers = {'Proxy-Connection': 'keep-alive'}
			r = requests.get(url, stream=True, headers=headers)
			length = float(r.headers['content-length'])
			f = open(name, 'wb')
			count = 0
			count_tmp = 0
			time1 = time.time()
			for chunk in r.iter_content(chunk_size=512):
				if chunk:
					f.write(chunk)
					count += len(chunk)
					if time.time() - time1 > 2:
						p = count / length * 100
						speed = (count - count_tmp) / 1024 / 1024 / 2
						count_tmp = count
						print(name + ': ' + formatFloat(p) + '%' + ' Speed: ' + formatFloat(speed) + 'M/S')
						time1 = time.time()
			f.close()

		def formatFloat(num):
			return '{:.2f}'.format(num)

		for s in self.result:
			if s == False and adm == 0:
				# print(1)
				downloadFile('libs\mirai-core-qqandroid-1.2.3.jar',
				             'https://raw.githubusercontent.com/project-mirai/mirai-repo/master/shadow/mirai-core-qqandroid/mirai-core-qqandroid-1.2.3.jar')
			if s == False and adm == 1:
				downloadFile('libs\mirai-console-pure-1.0-M4-dev-3.jar',
				             'https://raw.githubusercontent.com/project-mirai/mirai-repo/master/shadow/mirai-console-pure/mirai-console-pure-1.0-M4-dev-3.jar')
				# print(1)
				pass
			if s == False and adm == 2:
				downloadFile('libs\mirai-console-1.0-M4-dev-3.jar',
				             'https://raw.githubusercontent.com/project-mirai/mirai-repo/master/shadow/mirai-console/mirai-console-1.0-M4-dev-3.jar')
				# print(1)
				pass
			adm += 1

		pass

	def checkjar(self):
		dir1 = self.cwd + "\\libs"
		for root, dirs, files in os.walk(dir1):
			h = [os.path.join(root, name) for name in files if name.endswith('.jar')]

		if h == [] or h is None:
			return False
		else:
			pure = console = core = False
			geter = []
			result = [md5list.get_hash(lit) for lit in h]
			for f1 in result:
				for f2 in md5list.hashlist:
					if f1 == f2:
						geter.append(f1)
						if f1 in md5list.PURE_hashlisT:
							print('检测到pure内核，版本:' + md5list.Maindict[f1])
							pure = True
						if f1 in md5list.CORE_hashlisT:
							print('检测到主内核，版本:' + md5list.Maindict[f1])
							core = True
						if f1 in md5list.CONSOLE_hashlisT:
							print('检测到控制台，版本:' + md5list.Maindict[f1])
							console = True

			if core and pure and console:
				print("检测完毕，一切正常")
				return True
			else:
				print("缺少文件，正在下载...")
				self.result = [core, pure, console]

				return False

			pass


if __name__ == '__main__':
	s = main()
	s.main()
