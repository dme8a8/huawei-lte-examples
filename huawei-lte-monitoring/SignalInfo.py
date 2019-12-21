def get_int(value):
	if value == None:
	  return int(0)
	else:
	  return int(value.split('d')[0])

class SignalInfo():
    def __init__(self, client):
        self.signal_info = client.device.signal()

    def get_rsrq(self):
        return get_int(self.signal_info['rsrq'])

    def get_rsrp(self):
        return get_int(self.signal_info['rsrp'])

    def get_sinr(self):
        return get_int(self.signal_info['sinr'])

    def get_rssi(self):
        return get_int(self.signal_info['rssi'])
        
    def get_ecio(self):
        return get_int(self.signal_info['ecio'])
        
    def get_rscp(self):
        return get_int(self.signal_info['rscp'])
