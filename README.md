# hoy_main

### Development Environment
```
python 3.7.x
Django==2.2.3
mysql==0.0.2
mysqlclient==1.4.2.post1
requests==2.22.0
channels==2.2.0
channels-redis==2.4.0
```

### BootStrap Theme(Custom)
### Mysql
### Channels 를 이용한 websocket 통신
### Redis 는 docker 에 올려서 사용
```
$ docker run -p 6379:6379 -d redis:2.8
$ pip3 install channels_redis
```

- >
  settings.py (필요하면 여기서 변경)
  ```
   CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
  }
  ```
