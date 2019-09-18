import subprocess
cmd = ['netsh', 'wlan', 'show', 'profiles']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
for line in proc.stdout.readlines():
	if '     :' in line:
		cmd = ['netsh', 'wlan', 'show', 'profiles', line.split("     : ",1)[1].rstrip(), 'key=clear']
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		counter = 0
		counter2 = 0
		for line2 in proc.stdout.readlines():
			if '----------------------' in line2 or counter == 3:
				if counter ==  3:
					counter2 +=1
					if counter2 == 6:
						try:
							print line.split("     : ",1)[1].rstrip() + " - " + line2.split("  :",1)[1].rstrip()
						except:
							print line.split("     : ",1)[1].rstrip() + " - "
						continue
				else:
					counter += 1