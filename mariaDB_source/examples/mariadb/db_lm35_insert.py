import time
import Adafruit_DHT    # 온습도 센서 라이브러리 임포트
import pymysql    # pymysql 임포트

def Humi_Temp_read(pin):     # 온도 읽고 반환하는 함수
    (h, t) = Adafruit_DHT.read_retry(sensor, pin)
    if (h is not None) and (t is not None):
        return h, t

# 전역변수 선언부 
db = None 
cur = None 
sensor = Adafruit_DHT.DHT11  #온습도 센서 지정

# 접속정보
db = pymysql.connect(host='20.200.220.207', user='azureuser', password='1234', db='DCTDB', charset='utf8')  

try:
  cur = db.cursor() # 커서생성 
  
  while True:
    humi, temp = Humi_Temp_read(4)
    print ("%4.1f%%, %4.1f°C" % (humi, temp) )  # 입력할 온도값 출력
	
    sql = "INSERT INTO temperature(HUMI, TEMP) VALUES (%4.1f, %4.1f)" %(humi, temp)
    print(sql)

    # 실행할 sql문 
    cur.execute(sql)
	
    # 커서로 sql문 실행
    db.commit() # 저장 
	
    time.sleep(10)
except KeyboardInterrupt:
  pass	
finally:
  db.close() # 종료