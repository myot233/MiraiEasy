# coding:utf-8
import hashlib

CONSOLE_hashlisT = ['453597fd63e0275552479c008b90cf9c', ]
PURE_hashlisT = ['c0440db206c4475e48a58a1a80f5d466', ]
CORE_hashlisT = ['6f75ad34da4ee2c19b63ccb510b63998', ]
hashlist = CONSOLE_hashlisT + CORE_hashlisT + PURE_hashlisT

Maindict = {
	'453597fd63e0275552479c008b90cf9c':'console-1.0-M4-dev',
	'c0440db206c4475e48a58a1a80f5d466':'console-pure-1.0-M4-dev',
	'6f75ad34da4ee2c19b63ccb510b63998':'mirai-core-qqandroid-1.2.3',
}

def get_hash(jar):
	s = open(jar, 'rb')
	return hashlib.md5(s.read()).hexdigest()

if __name__ == '__main__':
    pass