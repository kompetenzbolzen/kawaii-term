

"""
OPENWEATHERというインターネットサービスを利用したものです。
私個人のAPIキーですが、個人で利用したものを利用してアクセスしてください
d5098ce4e32e6d1ffc703cd671d8f985
http://api.openweathermap.org/data/2.5/forecast?id=1850147&APPID={APIKEY}
"""
import os
import json
import time
import sys
from multiprocessing import Process

ok = None

home = os.environ['HOME']
# check the exists of recent prediction
with open('{home}/kawaii-term/async/weather.txt'.format(home=home),'r') as f:
  line = None
  for line in f:
    ...
  last = line.strip()
  if last == '':
    ok = False
    print('please wait serveral seconds...' )
  else:
    #print('last', last )
    lasttime = int( last.split('___').pop(0) )
    if int( time.time() ) - lasttime > 30:
      #print('refresh')
      ok = False
    # 無条件に出力
    print(last.split('___').pop() )

def async_update():
  raw = os.popen('curl -s "http://api.openweathermap.org/data/2.5/weather?q=Tokyo,jp&appid=1e240e732347c23472274dc188cd39d6"').read()
  obj = json.loads( raw )
  desc = obj['weather'][0]['description']
  save = '___'.join( map(str,[int(time.time()), desc] ) )
  os.system('echo {save} >> {home}/kawaii-term/async/weather.txt'.format( save=save, home=home ) )

if ok is not None: 
  p = Process(target=async_update, args=())
  p.start()
  p.join()
