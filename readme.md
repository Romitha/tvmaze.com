# tvmaze API Intergration

### Installation
First Extract the zip file name tvmaze.com
Then create virtual envirioment to run it.
Below steps are for the linux environment
```sh
$ cd tvmaze.com
$ virtualenv tvmaze
$ source tvmaze/bin/activate
$ pip install -r requirement.txt
$ python manage.py run 
```
Then server will start, you can use postman for to trigger api
curl --location --request GET 'http://127.0.0.1:5000/timers/diff/2020-1/2020-2/list'

The project structure according to MVC pattern
__init__.py in app/ directory initiate the router path 

In timer_controller is mange the request from tvmaze website

```sh
from flask import request, jsonify
from flask_restplus import Resource
from flask_cors import cross_origin
from ..util.dto import TimerDto
from ..service.timer_service import save_timer
import requests
from datetime import timedelta, datetime

api = TimerDto.api
_timer = TimerDto.timer

@api.route('/diff/<month1>/<month2>/list')
@api.response(404, 'timer not found.')
class GetTimerList(Resource):
    @api.doc('get tv episode')
    @cross_origin() # this is for accesign this api from different web site
    def get(self, month1, month2):
        """List all Episode details"""
        print('List all Timer details')
        get_month = []
        get_month.append(month1)
        get_month.append(month2)
        dates = []
        finalized_list = []
        # initiate the vriables

        for month_ in get_month: #get month iput fromquery parameters

            month, year = int(month_.split('-')[1]), int(month_.split('-')[0])
            print(month, year)
            day = timedelta(days=1)
            date1 = datetime(year, month, 1)
            d = date1
            # generate month days list
            while d.month == month:
                dates.append(d.strftime('%Y-%m-%d'))
                print(d.strftime('%Y-%m-%d'))
                d += day
                response = requests.get('http://api.tvmaze.com/schedule/web?date={}'.format(d.strftime('%Y-%m-%d')))
                get_data = response.json()
                for data in get_data:
                    finalized_list.append({
                        "name": data['name'],
                        "season": data['season'],
                        "series_name": data['_embedded']['show']['name'],
                        "language": data['_embedded']['show']['language'],
                    })

        print(datetime.utcnow())
        data = {
            "api_name" : "diff/{}/{}/list".format(month1,month2),
            "description": "http://api.tvmaze.com/schedule/web?date=",
            "created_at": str(datetime.utcnow())
        }
        result = save_timer(data=data)
        # send result as json format
        response = jsonify({
            'list': finalized_list,
            'result': result
        })
        response.status_code = 201
        return response

```
