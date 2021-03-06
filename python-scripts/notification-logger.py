import threading
import sys
import os
import json
"""
import signal

i = 0

def check_stdin():
	global i
	while True:
		try:
			lines = sys.stdin.readline()
			if "stop logging" in lines:
				close_log_file()
				break
			write_log(lines)
			i += 1
		except:
			break

def write_log(logEntry):
	#to_node("Writing: " + logEntry + "to " + logFile.name)
	logFile.write(logEntry)

def close_log_file():
	logFile.close()
	#to_node("Logfile saved to " + config['logFilePath'])
	#to_node(str(i) + " new entries saved")

def shutdown():
	write_log("!!!!!!!!!!!!!!!!!")
	logFile.close()

"""

def to_node(message):
	print(message)
	# stdout is buffered and has to be flushed manually to prevent delays in the node helper communication
	sys.stdout.flush()

if __name__ == "__main__":
		
	config = json.loads(sys.argv[1])
	to_node("open log file " + config['logFilePath'] + " in mode '" + config['writeMode'] + "'")
	to_node("This working directory path: " + os.getcwd())
	logFile = open(config['logFilePath'], config['writeMode'], buffering=1)
		
	while True:
		try:
			line = sys.stdin.readline()
			logFile.write(line)
		except:
			break
	
	""" debugging code
	logFile = open("/opt/dev/MagicMirror_aderiglasow/modules/smartmirror-notification-logger/notification_log.csv", 'a', buffering=1)

	t = threading.Thread(target=check_stdin)
	t.start()
	
	signal.signal(signal.SIGINT, shutdown)
	"""
