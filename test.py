import requests
import pymysql
import json

class get_info():
    def __init__(self):
        self.__url='http://api.avatardata.cn/Weather/Query?key=ce2d260ee1e34aa796c78e03b4f7376c&cityname=成都'
        self.__ip='122.51.168.67'
        self.__user='root'
        self.__password='IRVing777!'
        self.__databases='WebData'

    def __connect(self):
        conn=pymysql.connect(host=self.__ip,user=self.__user,password=self.__password,
                             database=self.__databases)
        cursor=conn.cursor()
        return conn,cursor

    def __close(self,conn,cursor):
        cursor.close()
        conn.close()

    def Insert(self,tablename,columns,values):
        conn,cursor=self.__connect()
        var='Insert Into '+tablename+'('
        for column in columns:
            if column != columns[-1]:
                var = var + column + ','
            else:
                var = var + column + ") Value('"
        for value in values:
            if value != values[-1]:
                var = var + str(value) + "','"
            else:
                var = var + str(value) + "')"
        res=cursor.execute(var)
        conn.commit()
        self.__close(conn,cursor)


    def get_data(self):
        response = requests.get(self.__url)
        res = json.loads(response.text)
        result=res['result']

        realtime = result['realtime']

        date = realtime['date']
        city = realtime['city_name']
        wind_info = realtime['wind']
        weather_info = realtime['weather']

        speed = wind_info['windspeed']
        direct = wind_info['direct']
        power = wind_info['power']

        humidity = weather_info['humidity']
        img = weather_info['img']
        info_weather = weather_info['info']
        temperature = weather_info['temperature']

        life = result['life']

        life_date = life['date']
        info = life['info']

        kongtiao = info['kongtiao'][1]
        yundong = info['yundong'][1]
        ziwaixian = info['ziwaixian'][1]
        ganmao = info['ganmao'][1]
        chuanyi = info['chuanyi'][1]

        realtime_list=[date,city,speed,direct,power,humidity,img,info_weather,temperature]
        life_list=[life_date,kongtiao,yundong,ziwaixian,ganmao,chuanyi]
        return realtime_list,life_list

    def main(self,):
        realtime_list,life_list=self.get_data()
        realtime_columns=['date','city','windspeed','direct','power','hummidity','img','info','temperature']
        life_columns=['date','kongtiao','yundong','ziwaixian','ganmao','chuanyi']
        self.Insert(tablename='realtime',columns=realtime_columns,values=realtime_list)
        self.Insert(tablename='life',columns=life_columns,values=life_list)

if __name__ == '__main__':
    mission=get_info()
    mission.main()
    # realtime_columns = ['date', 'city', 'windspeed', 'direct', 'power', 'hummidity', 'img', 'info', 'temperature']
    # life_columns = ['date', 'kongtiao', 'yundong', 'ziwaixian', 'ganmao', 'wuran', 'chuanyi']
    # mission.Insert('realtime',realtime_columns,[1,2,3,4,5,6,7,8,9])





