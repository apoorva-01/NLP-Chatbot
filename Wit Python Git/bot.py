from wit import Wit

client = Wit("W67RFCFTSFZD64KY3LXMA5QI2S33XFGR")
client = Wit(access_token=access_token, logger=custom_logger)
client.message('set an alarm tomorrow at 7am')


resp = client.message('what is the weather in London?')
print('Yay, got Wit.ai response: ' + str(resp))

resp = None
with open('Recording.m4a', 'rb') as f:
  resp = client.speech(f, {'time': 'today'})
print('Yay, got Wit.ai response: ' + str(resp))

