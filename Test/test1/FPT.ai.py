import requests

url = 'https://api.fpt.ai/hmi/tts/v5'

payload = 'Mình là Phạm Nhật linh, 19 tuổi và có nhiều bạn trên facebook. ' \
          'Mình không bao giờ chấp nhận kết bạn “tào lao”, mình đâu có ngu để bị “dụ”. ' \
          'Mong được làm quen với các bạn nữ.'

headers = {
    'api-key': 'zzZq77FGWvx6LorGDkj9gp1MkJoP5rP2',
    'speed': '',
    'voice': 'banmai'
}

response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)

print(response.text)
