from flask import Flask
import datetime
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Weeks(Resource):
    def get(self):
        return {
            "total":10,
            "weeks":[
                {
                    "week_id":"week_2022_10_1",
                    "start":2000,
                    "end":200,
                    "month":10,
                    "week":42,
                    "order":1,
                    "year":2022,
                    "number":35
                },
                {
                    "week_id": "week_2022_10_1",
                    "start": 2000,
                    "end": 200,
                    "month": 10,
                    "week": 42,
                    "order": 1,
                    "year": 2022,
                    "number": 35
                },
                {
                    "week_id": "week_2022_10_1",
                    "start": 2000,
                    "end": 200,
                    "month": 10,
                    "week": 42,
                    "order": 1,
                    "year": 2022,
                    "number": 35
                },
            ]
        }

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
    app.run(host="0.0.0.0")