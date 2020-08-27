# Server Side
from flask import Flask
from flask_restful import Api,Resource, abort ,reqparse
from flask_sqlalchemy import SQLAlchemy, Model
#reqparse คือการรับ รีควายเม้นมาแล้วไปแมคกับชื่อคอลัม
app = Flask(__name__)

#database
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///database.db"

api=Api(app) # เตรียมข้อมูลฝั่งเซิฟเวอร์ ให้เป็น api

#ออกแบบ model
class CityModel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    temp=db.Column(db.String(100),nullable=False)
    weather=db.Column(db.String(100),nullable=False)
    people=db.Column(db.String(100),nullable=False)

    #สร้าง เมธอด repr ขึ้นมาเพื่อ mapกับmodel เพราะเราจำเป็นต้องสร้าง object ขึ้นมาเพื่อให้มันไปจับคู่กับตัวแปลในฐานข้อมูล
    def __repr__(self): # repr ใช้ทำวัตถุ แต่ str ใช้กับ string
        return f"City(name={name},temp={temp},weather={weather},people={people})"

db.create_all()# สร้าง model เขียนต่อท้ายเสมอ  เพราะโครงสร้างอยุ่ในโมเดล เราต้องเอาโมเดลที่สร้างมา create
        
city_add_args=reqparse.RequestParser() #import reqparse คือการเช็คข้อมูล
city_add_args.add_argument("name",type=str,required=True,help="กรุณาระบุชื่อจังหวัดด้วยครับ")
city_add_args.add_argument("temp",type=str,required=True,help="กรุณาระบุอุณหภูมิเป็นตัวอักษร")
city_add_args.add_argument("weather",required=True,type=str,help="กรุณาระบุสภาพอากาศเป็นตัวอักษร")
city_add_args.add_argument("people",required=True,type=str,help="กรุณาระบุจำนวนประชากรเป็นตัวอักษร")  

#ก้อนข้อมูล json
# city = {
#             1:{"name": "ชลบุรี" ,"frameworks": "Django","year": 2000},  
#             2:{"name": "กรุงเทพ" ,"frameworks": "Django","year": 2005} ,
#             3:{"name": "ระยอง" ,"frameworks": "Django","year": 2010}    
# }

# def notFoundCity(city_id):
#     if city_id not in city :
#         abort(404,message="ไม่พบข้อมูล")
#     pass

#design
class WeatherCity(Resource): #Resource เป็น object
    # ทำให้อยุ่ในรูปแบบ json
    def get(self,city_id): #ร้องขอข้อมูล
        # return {"data" : "WeatherCity thailand"+name}
        # notFoundCity(city_id) # เช็คว่าใน city มีข้อมูลที่เราเรียกใช้มั้ย ถ้าไม่มี จะไปเรียกใช้ notFoundCity
        return city[city_id]
    def post(self):    #เพิ่มข้อมูลลงไปที่คลัง post คือขอข้อมูลและโยนข้อมูลไปให้ด้วย โดยการโยนข้อมูลไปเพิ่มจะทำผ่านตัว paramiter
        return {"data" : "Weather post"}

# call 
api.add_resource(WeatherCity,"/Weather/<int:city_id>")
if __name__ == "__main__":
    app.run(debug=True)