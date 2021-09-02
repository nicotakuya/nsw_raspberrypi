#web appli robot
import threading
from gpiozero import Motor
from webob import Request, Response
import time

html = """<center><form method="post">
<input type="submit" name="button" value="Forward"><br><br>
<input type="submit" name="button" value="Turn L">
<input type="submit" name="button" value="Stop">
<input type="submit" name="button" value="Turn R"><br><br>
<input type="submit" name="button" value="Back"><br>
</form></center>"""
right = Motor(23,24)
left  = Motor(20,21)
movreq = 0
movsec = 0
righttable = [0,1,2,1,2,3]
lefttable   = [0,1,1,2,2,3]

class MotorCtrl(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.daemon = True
		self.start()

	def run(self):
		global movsec,movreq
		while True:
			time.sleep(0.1)
			if(righttable[movreq]  == 1):right.forward()
			if(righttable[movreq]  == 2):right.backward()
			if(righttable[movreq]  == 3):right.stop()
			if(lefttable[movreq]  == 1):left.forward()
			if(lefttable[movreq]  == 2):left.backward()
			if(lefttable[movreq]  == 3):left.stop()
			if(movreq):movreq = 0
			if(movsec > 0):
				movsec = movsec - 0.1
				if(movsec <= 0):
					right.stop()
					left.stop()

class WebApp(object):
	def __call__(self ,environ ,start_response):
		global movsec,movreq
		req = Request(environ)
		button = req.params.get('button', '')
		if button=='Forward':movreq = 1
		if button=='Turn R' :movreq = 2
		if button=='Turn L' :movreq = 3
		if button=='Back'   :movreq = 4
		if button=='Stop'   :movreq = 5
		movsec = 3
		resp = Response(html)
		return resp(environ, start_response)

application = WebApp()
mot = MotorCtrl()

if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	port = 8080
	httpd = make_server('', port, application)
	print('Serving HTTP on port %s...' % port)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		right.stop()
		left.stop()
