import os, platform

class Welcome:

	def __init__(self):

		if 'Windows' in str(platform.platform()):

			os.system('cls')

			import ctypes
			kernel32 = ctypes.windll.kernel32
			kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)  

		else:            #(Linux/GNU)
			os.system('clear')



		self.Logo='''
		                       \033[38;5;226m.i72KPdDPPX17:
		                   :UgBBBBBBBQBBBBBBBBBBBdJ. 
		                sBQBQBBBBBBBRQDMgMDggRRQBBBBQR7   
		             vBQBBQdK52u7 i7rPMDgDgZgZMQBRRMQBBBQi 
		           KBBBQg1LUUPbgMurKbDZgZgDgZgRi.2ggDggQBBBj 
		         5BQQggDgZMRRgRgRQBRMDDZDDDEgZM7PZgZDZgZMgBBBv 
		       rBBQMZgZgZgDgDgdPZRggDgZDZgDgZgDBEgggEgZgDggMQBB: 
		      DBBgMDgDgDgDgDgggPKSZggZDDgZgZgDgEIggZgDgDPdRgMgBQ2 
		     BBQMRgQQBQQQQQBQBBBQgKPMgDDZgEgDgg5PRgggMgMZ1XQgggQBM 
		    BdRBBBgIsvvrv7Yj52gQBBBqqggZDZgZgZRUUMBBBZEDBBEYQQMgQBB\033[0m 
		   \033[38;5;226mBQ\033[0m \033[38;5;231muP..:UdRQBBBBq\033[0m     \033[38;5;226m.JEPMDgZDZgZggQDBPi\033[0m\033[38;5;226muurJLvsbgvBBggRQ\033[0m 
		  \033[38;5;226mBBQ\033[0m::\033[38;5;231muYYuvY77vuuS1...vi\033[0m \033[38;5;226m:UggDDZDZgDQDi\033[0m;  \033[38;5;231mvBBBBg\033[0m   . \033[38;5;226mBBggRBE\033[0m 
		 \033[38;5;226mUBQgQbL1\033[0m:::::::::::::::..\033[38;5;226mvDEgDgZDEDZgR\033[0m;J. \033[38;5;231m:i:i:iri:::\033[0m  \033[38;5;226m5QgDQ\033[0m 
		 \033[38;5;226mBBggDMD57LIQRQQBDX7svv7u\033[0m\033[38;5;226mMBQRZgEgZDZgZMMg\033[0m;::::::::::::::.\033[38;5;226mQgggB\033[0m  
		\033[38;5;226m5BggDggRgDXDQQQRPP52KgRB\033[0m\033[38;5;226mBBQDDgZDEgZgZDDMQBM\033[0m\033[38;5;226mbsL1BBBQBBBQ7ggZggBB\033[0m 
		\033[38;5;226mBQgZgZgZMgPIKXPdgQBBBBBMZUiuMDDDgDgDgZDDggRQQqL1ZgBBBBjvQDgZMBQ 
		BBQDgDgDgZggZS5sJ5rr7:ri7iruQggZgZDDDEDDgZgDggQbJr:vDIIIQDgEgDQB   
		BBggEDZgZgZggMMgBQ IBQgZDQQQgMDgZDZgZgZDZgZDDggQMX7i sUDMgDgZgRB  
		BBMZgZgZDZgZgZgMB  .7uPQBBBRQgMgMgMDgggDgDgggDMMQBBBv BBMDgEgDQQ  
		LBggZgZDZgEgZgDRqr      :7s5PZgQQBQBQBQBQBQBQBQQdXY7.  BggZgZgMB  
		BBRZgEgZgEDZDZDDMQZgQQ                                 BgZDEgDQB  
		BBRgZgDgZgEgZgEgDMMMDggMgQRBQBRREdPPSKSKSKqPKPEQQBQ:7i7BgDZgZgQB   
		BBggZgDDDgZDDgEgZgDgDgDgDgDgDMgRMQMQRQMQQRRQMMgMQB SBBggDgZggBM
		UBRDgDDZgEgZgZDZgEDZgZgZgZgZgDgDgZgDgDgZgDgDgZgDB7:BQggZDZDDRBB
		 BBgZDZgZDZgDgZgZgZgEgEgZgDgEgZgZgDgZDZDDgZgDgZMPrQRggDgZgZMQB 
		 vBMgDDZgEgZDZgZgEDZDZgZgggDgZgEDZgZDEgZgZggRZgDgMMDgZgZgDMQBB
		  RBggZgDgZgEDZgZDZgZDDgbIgQMgggDgDgDgDgDRRRiSQgggDgEgZDZgRBI 
		   BBggDgZgZgZgZgDMDgZDDZL7YPZRMRMRMQMQggKJrXduBQggDDDgZggBD 
		    BBMgZDEDZgZggdXQggDggQgSJsvjuIIX5SjYvuXQQQi2IQDgZgDgQBg  
		     QBQMDDZgZDZRqr1BMgZggggQRRZdPPPPPdDQRRgMQS 11QZDDMQBq 
		      IBBMggZgDggb7vvgQMDRggDggggMgMgMggDgZggBU.YuQgDQBB7   
		       :BBBgMDgZgMq7s7IMBdRQQgMDgDgZgDgZDZDZQQ.i7gQMBBQ   
		         YQBBQggDgRRYvvJusJUSgQQMQggDgDgZgDRQY.XJBBBQr   
		           LBBBQRgggBqJvjuJJusJ55KZgQRQQQRQgj7qJBBBr  
		             igBBBQQMQQb7dESJuJ1uu7vv7YsYS2YPQPBE:   
		                rdBQBBBBBMBBBgdSbQBQREDdgBBQB5i    
		                 .rPQBBBBBBBBBQBBBQBQBBBBBBBB      
		                        .i7uuUUUUUUUU1jri.\033[0m       '''



