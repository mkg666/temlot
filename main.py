# coding=utf-8
from flask import Flask
import tsdb_sample
import time
import mysqldb
import datetime

app = Flask(__name__)


@app.after_request
def after_request(response):
    # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    # # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


# @app.route('/')
# def hello():
#     tsdbs = tsdb_sample.select()
#     for tsdb in tsdbs:
#         # print studb.stuselect(tsdb[1])
#
#     return jsonify(tsdbs)


@app.route('/tsdball')
def selectall():
    # 全部数据查询

    tsdb = tsdb_sample.select(
        "select  Identity ,Temperature, Number_02,  String_01 from metric order by "
        "Number_02 desc")
    count = tsdb_sample.select("select  count(*) from metric")[0][0]
    for b in tsdb:
        timeStamp = int(b[2])
        dateArray = datetime.datetime.fromtimestamp(timeStamp)
        b[2] = dateArray.strftime("%Y--%m--%d %H:%M:%S")

        # 时序数据库查询与时间格式转换
    for sqlfor in tsdb:
        stuinfo = mysqldb.select(
            "SELECT stu.name, stu.xingbie, stu.zuanye, stu.xueyuan, stu.area FROM stu WHERE stu.xuhao = %d" % (
                int(sqlfor[0])))
        name = stuinfo[0]
        sex = stuinfo[1]
        zuanye = stuinfo[2]
        xueyuan = stuinfo[3]
        area = stuinfo[4]

        sqlfor.insert(1, name)
        sqlfor.insert(4, sex)
        sqlfor.insert(5, xueyuan)
        sqlfor.insert(6, zuanye)
        sqlfor.insert(7, area)

    returndate = {
        "code": 0,
        "msg": "",
        "count": count,
        "data": tsdb
    }
    return returndate


@app.route('/tsdbtoday')
def select():
    # 获取0点时间戳

    today = datetime.date.today()
    today_time = int(time.mktime(today.timetuple()))

    tsdb = tsdb_sample.select(
        "select Identity ,Temperature, Number_02,  String_01 from metric where Number_02 > %d order by Number_02 desc" % (
            today_time))
    for b in tsdb:
        timeStamp = int(b[2])
        dateArray = datetime.datetime.fromtimestamp(timeStamp)
        b[2] = dateArray.strftime("%Y--%m--%d %H:%M:%S")

        # 时序数据库查询与时间格式转换
    for sqlfor in tsdb:
        stuinfo = mysqldb.select(
            "SELECT stu.name, stu.xingbie, stu.zuanye, stu.xueyuan, stu.area FROM stu WHERE stu.xuhao = %d" % (
                int(sqlfor[0])))
        name = stuinfo[0]
        sex = stuinfo[1]
        zuanye = stuinfo[2]
        xueyuan = stuinfo[3]
        area = stuinfo[4]

        sqlfor.insert(1, name)
        sqlfor.insert(4, sex)
        sqlfor.insert(5, xueyuan)
        sqlfor.insert(6, zuanye)
        sqlfor.insert(7, area)

    returndate = {
        "code": 0,
        "msg": "",
        "count": 1000,
        "data": tsdb
    }
    return returndate


@app.route('/tsdbmonth')
def selectmonth():
    today_time = int(time.mktime(datetime.date(datetime.date.today().year, datetime.date.today().month, 1).timetuple()))

    tsdb = tsdb_sample.select(
        "select Identity ,Temperature, Number_02,  String_01 from metric where Number_02 > %d order by Number_02 desc" % (
            today_time))
    count = tsdb_sample.select("select count(*) from metric where Number_02 > %d " % (
            today_time))
    for b in tsdb:
        timeStamp = int(b[2])
        dateArray = datetime.datetime.fromtimestamp(timeStamp)
        b[2] = dateArray.strftime("%Y--%m--%d %H:%M:%S")

        # 时序数据库查询与时间格式转换
    for sqlfor in tsdb:
        stuinfo = mysqldb.select(
            "SELECT stu.name, stu.xingbie, stu.zuanye, stu.xueyuan, stu.area FROM stu WHERE stu.xuhao = %d" % (
                int(sqlfor[0])))
        name = stuinfo[0]
        sex = stuinfo[1]
        zuanye = stuinfo[2]
        xueyuan = stuinfo[3]
        area = stuinfo[4]

        sqlfor.insert(1, name)
        sqlfor.insert(4, sex)
        sqlfor.insert(5, xueyuan)
        sqlfor.insert(6, zuanye)
        sqlfor.insert(7, area)

    returndate = {
        "code": 0,
        "msg": "",
        "count": int(count[0][0]),
        "data": tsdb
    }
    return returndate


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)

