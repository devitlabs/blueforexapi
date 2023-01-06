from flask import Flask
import datetime
from flask_restful import Resource, Api
import gspread

app = Flask(__name__)
api = Api(app)
sa = gspread.service_account()

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Weeks(Resource):
    def get(self):
        json = {
            "total":0,
            "weeks":[]
        }
        try:
            sh_weeks = sa.open("WeeksSheet")
            wks_weeks = sh_weeks.sheet1
            end = wks_weeks.acell("K1").value
            print(end)
            weeks = wks_weeks.get(f"A2:I{end}")
            list_week = []
            for week in weeks :
                week_json = {}
                week_json["id"] = int(week[0])
                week_json["week_id"] = week[1]
                week_json["start"] = week[2]
                week_json["end"] = week[3]
                week_json["week"] = int(week[4])
                week_json["month"] = int(week[5])
                week_json["number"] = int(week[6])
                week_json["year"] = int(week[7])
                week_json["valide"] = week[8] == "TRUE"
                list_week.append(week_json)
            json["total"] = len(list_week)
            json["weeks"] = list_week

            return  json

        except :
            return  json

class LiveSignals(Resource):
    def get(self):
        date = datetime.datetime.now()
        return {
            "total":20,
            "weeks":[
                {
                    "week_id":"week_2022_10_1",
                    "signals":[
                        {
                            "number":3,
                            "asset":"CADJPY",
                            "direction":"BUY",
                            "open_price":1.0350,
                            "asset_type":2,
                            "stop_loss":1.0300,
                            "take_profit":1.0400,
                            "status":"LIVE",
                            "open_time":int(date.strftime("%Y%m%d%H%M")),
                            "current_price":1.0360,
                            "result_view": "url"
                        },
                        {
                            "number": 4,
                            "asset": "EURUSD",
                            "direction": "BUY",
                            "open_price": 1.0350,
                            "asset_type": 2,
                            "stop_loss": 1.0300,
                            "take_profit": 1.0400,
                            "status": "LIVE",
                            "open_time": int(date.strftime("%Y%m%d%H%M")),
                            "current_price": 1.0360,
                            "result_view": "url"
                        },
                    ]
                },
                {
                    "week_id": "week_2022_10_3",
                    "signals": [
                        {
                            "number": 3,
                            "asset": "CADJPY",
                            "direction": "BUY",
                            "open_price": 1.0350,
                            "asset_type": 2,
                            "stop_loss": 1.0300,
                            "take_profit": 1.0400,
                            "status": "LIVE",
                            "open_time": int(date.strftime("%Y%m%d%H%M")),
                            "current_price": 1.0360,
                            "result_view": "url"
                        },
                        {
                            "number": 4,
                            "asset": "EURUSD",
                            "direction": "BUY",
                            "open_price": 1.0350,
                            "asset_type": 2,
                            "stop_loss": 1.0300,
                            "take_profit": 1.0400,
                            "status": "LIVE",
                            "open_time": int(date.strftime("%Y%m%d%H%M")),
                            "current_price": 1.0360,
                            "result_view": "url"
                        },
                    ]
                },
                {
                    "week_id": "week_2022_10_",
                    "signals": [
                        {
                            "number": 3,
                            "asset": "CADJPY",
                            "direction": "BUY",
                            "open_price": 1.0350,
                            "asset_type": 2,
                            "stop_loss": 1.0300,
                            "take_profit": 1.0400,
                            "status": "LIVE",
                            "open_time": int(date.strftime("%Y%m%d%H%M")),
                            "current_price": 1.0360,
                            "result_view": "url"
                        },
                        {
                            "number": 4,
                            "asset": "EURUSD",
                            "direction": "BUY",
                            "open_price": 1.0350,
                            "asset_type": 2,
                            "stop_loss": round(1.0300,4),
                            "take_profit": 1.0400,
                            "status": "LIVE",
                            "open_time": int(date.strftime("%Y%m%d%H%M")),
                            "current_price": 1.0360,
                            "result_view": "url"
                        },
                    ]
                },
            ]
        }

class ClosedSignals(Resource):
    def get(self):
        date = datetime.datetime.now()
        return {
            "total": 20,
            "weeks": [
                {
                    "week_id": "week_2022_10_1",
                    "signals": [
                        {
                            "number": 3,
                            "asset": "CADJPY",
                            "direction": "BUY",
                            "open_price": 1.0350,
                            "asset_type": 2,
                            "stop_loss": 1.0300,
                            "take_profit": 1.0400,
                            "status": "CLOSED",
                            "open_time": int(date.strftime("%Y%m%d%H%M")),
                            "closed_time": int(date.strftime("%Y%m%d%H%M")),
                            "closed_price":1.0400,
                            "current_price": 1.0360,
                            "result":"TP",
                            "result_pips":50,
                            "result_view":"url"
                        },
                        {
                            "number": 3,
                            "asset": "CADJPY",
                            "direction": "BUY",
                            "open_price": 1.0350,
                            "asset_type": 2,
                            "stop_loss": 1.0300,
                            "take_profit": 1.0400,
                            "status": "CLOSED",
                            "open_time": int(date.strftime("%Y%m%d%H%M")),
                            "closed_time": int(date.strftime("%Y%m%d%H%M")),
                            "closed_price":1.0400,
                            "current_price": 1.0360,
                            "result":"TP",
                            "result_pips":50,
                            "result_view":"url"
                        },
                    ]
                },
                {
                    "week_id": "week_2022_10_3",
                    "signals": [
                        {
                            "number": 3,
                            "asset": "CADJPY",
                            "direction": "BUY",
                            "open_price": 1.0350,
                            "asset_type": 2,
                            "stop_loss": 1.0300,
                            "take_profit": 1.0400,
                            "status": "CLOSED",
                            "open_time": int(date.strftime("%Y%m%d%H%M")),
                            "closed_time": int(date.strftime("%Y%m%d%H%M")),
                            "closed_price": 1.0400,
                            "current_price": 1.0360,
                            "result": "TP",
                            "result_pips": 50,
                            "result_view": "url"
                        },
                        {
                            "number": 3,
                            "asset": "CADJPY",
                            "direction": "BUY",
                            "open_price": 1.0350,
                            "asset_type": 2,
                            "stop_loss": 1.0300,
                            "take_profit": 1.0400,
                            "status": "CLOSED",
                            "open_time": int(date.strftime("%Y%m%d%H%M")),
                            "closed_time": int(date.strftime("%Y%m%d%H%M")),
                            "closed_price":1.0400,
                            "current_price": 1.0360,
                            "result":"TP",
                            "result_pips":50,
                            "result_view":"url"
                        },
                    ]
                },
                {
                    "week_id": "week_2022_10_",
                    "signals": [
                        {
                            "number": 3,
                            "asset": "CADJPY",
                            "direction": "BUY",
                            "open_price": 1.0350,
                            "asset_type": 2,
                            "stop_loss": 1.0300,
                            "take_profit": 1.0400,
                            "status": "CLOSED",
                            "open_time": int(date.strftime("%Y%m%d%H%M")),
                            "closed_time": int(date.strftime("%Y%m%d%H%M")),
                            "closed_price":1.0400,
                            "current_price": 1.0360,
                            "result":"TP",
                            "result_pips":50,
                            "result_view":"url"
                        },
                        {
                            "number": 3,
                            "asset": "CADJPY",
                            "direction": "BUY",
                            "open_price": 1.0350,
                            "asset_type": 2,
                            "stop_loss": 1.0300,
                            "take_profit": 1.0400,
                            "status": "CLOSED",
                            "open_time": int(date.strftime("%Y%m%d%H%M")),
                            "closed_time": int(date.strftime("%Y%m%d%H%M")),
                            "closed_price":1.0400,
                            "current_price": 1.0360,
                            "result":"TP",
                            "result_pips":50,
                            "result_view":"url"
                        },
                    ]
                },
            ]
        }

class MontlyResult(Resource):
    def get(self):
        return {
            "month":10,
            "year":2022,
            "week":[
                {
                    "week":1,
                    "profit_loss":150,
                },
                {
                    "week": 1,
                    "profit_loss": -50,
                }
            ],
            "profit_loss":{
                "profit":150,
                "loss":50,
                "result":100,
            },
            "signals":{
                "total":10,
                "profit":8,
                "loss":2
            }
        }

class ForexQuote(Resource):
    def get(self):
        return {
            "base_currency":"USD",
            "pip_factor":{
                "EURUSD":1.0,
                "GBPUSD":1.0,
                "USDCAD":0.75,
                "GBPCAD":0.78,
                "EURJPY":0.85,
            }
        }

class AssetCalcutor(Resource):
    def get(self):
        return {
            "time_frame":"5M",
            "asset":"EURUSD",
            "end_date":"",
            "candle":[
                {
                    "open":"",
                    "high":"",
                    "low":"",
                    "close":"",
                    "time":""
                },
                {
                    "open": "",
                    "high": "",
                    "low": "",
                    "close": "",
                    "time": ""
                },
                {
                    "open": "",
                    "high": "",
                    "low": "",
                    "close": "",
                    "time": ""
                },
                {
                    "open": "",
                    "high": "",
                    "low": "",
                    "close": "",
                    "time": ""
                },
                {
                    "open":"",
                    "high":"",
                    "low":"",
                    "close":"",
                    "time":""
                },
                {
                    "open":"",
                    "high":"",
                    "low":"",
                    "close":"",
                    "time":""
                },
                {
                    "open":"",
                    "high":"",
                    "low":"",
                    "close":"",
                    "time":""
                },
                {
                    "open":"",
                    "high":"",
                    "low":"",
                    "close":"",
                    "time":""
                },
                {
                    "open":"",
                    "high":"",
                    "low":"",
                    "close":"",
                    "time":""
                },
                {
                    "open":"",
                    "high":"",
                    "low":"",
                    "close":"",
                    "time":""
                },
                {
                    "open":"",
                    "high":"",
                    "low":"",
                    "close":"",
                    "time":""
                }
            ]
        }



api.add_resource(HelloWorld, '/')
api.add_resource(LiveSignals, '/live_signals')
api.add_resource(Weeks, '/weeks')

if __name__ == '__main__':
    app.run(debug=True)
