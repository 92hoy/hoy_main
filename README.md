# hoy_main

Channels 를 이용한 websocket 통신

Redis 는 docker 에 올려서 사용
- > docker run -p 6379:6379 -d redis:2.8
- > pip3 install channels_redis
- >
  settings.py (필요하면 여기서 변경)
  '''
   CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
  }
  '''
