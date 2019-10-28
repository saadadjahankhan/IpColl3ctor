import socket, sys

def g3tip():
	ban = """

 (   (           )  (    (                        )  (     
 )\ ))\ )  (  ( /(  )\ ) )\ )       (    *   ) ( /(  )\ )  
(()/(()/(  )\ )\())(()/((()/( (     )\ ` )  /( )\())(()/(  
 /(_))(_)|((_|(_)\  /(_))/(_)))\  (((_) ( )(_)|(_)\  /(_)) 
(_))(_)) )\___ ((_)(_)) (_)) ((_) )\___(_(_())  ((_)(_))   
|_ _| _ ((/ __/ _ \| |  | |  | __((/ __|_   _| / _ \| _ \  
 | ||  _/| (_| (_) | |__| |__| _| | (__  | |  | (_) |   /  
|___|_|   \___\___/|____|____|___| \___| |_|   \___/|_|_\  
                                                           
                                                                   --COD3D BY V3N0M                                                           
  
  Mass ip Collector                                                                  
	"""
	print(ban)
	site_files = open(sys.argv[1])
	for i in site_files.readlines():
		site = i.strip()
		try:
			if 'http://' not in site:
				ips_1 = socket.gethostbyname(site)
				print ("[-IP-] "+ips_1)
				open('iplist.txt', 'a').write(ips_1+'\n')
			elif 'http://' in site:
				site2 = site.replace('http://', '').replace('https://', '').replace('/', '')
				ips_2 = socket.gethostbyname(site2)
				print ("[-IP-] "+ips_2)
				open('iplist.txt', 'a').write(ips_2+'\n')
	
		except Exception as e:
			print(e)
		
g3tip()


#CODED BY MR.V3N0M
#T34M ROYAL BATTL3R BD