#Telegram 
# "1958129912:AAFLQ0pn56FhI_fpyJCl8-opWQx6xpn2XOU","1942030266:AAG64BLjBFvatF4newdLIc0D3XhDS-Uuqio"
# @newsalarm6203","1472478647"
telgm_nms = "NOMAL"
telgm_tokens = "1958129912:AAFLQ0pn56FhI_fpyJCl8-opWQx6xpn2XOU"
chat_ids = "@newsalarm6203"
# telgm_nms = ["NOMAL","MY","NOMAL","NOMAL"]
# telgm_tokens = ["1958129912:AAFLQ0pn56FhI_fpyJCl8-opWQx6xpn2XOU","1958129912:AAFLQ0pn56FhI_fpyJCl8-opWQx6xpn2XOU","1958129912:AAFLQ0pn56FhI_fpyJCl8-opWQx6xpn2XOU","1958129912:AAFLQ0pn56FhI_fpyJCl8-opWQx6xpn2XOU"]
# chat_ids = ["@newsalarm6203","@newsalarm6203","@newsalarm6203","@newsalarm6203"]

#Naver API Params
client_id = "ObqxYuxknqyCoMz1j7j8"
client_secret = "Qfl_AsGOFa"
# keyword = ["속보"]
# keywords = [["NFT","이더리움","메타버스","비트코인","비트토렌트"],["솔라나","폴카닷","에이다","넴"],["스택스","SEC","샌드박스","세럼"],["코인베이스","업비트","창펑자오","near"]]
# sortTypes = ["date","date","date","sim"]
keywords = ["NFT","이더리움","메타버스","비트코인","비트토렌트","솔라나","폴카닷","에이다","넴","스택스","SEC","샌드박스","세럼","코인베이스","업비트","창펑자오","near"]
sortTypes = "date"
url = "https://openapi.naver.com/v1/search/news.json"
displayNum = 3
startNum = 1
headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}

#common
thread_sleep_time = 7 #초
night_mode = True