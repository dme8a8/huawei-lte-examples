import SignalInfo

lte_quality_signal_dict = {
                   'rsrp': (-80, -90, -100),
                   'rsrq': (-10, -15, -20),
                   'sinr': (20, 13, 0),
                   'rssi': (-70, -86, -100),
                   'ecio': (0, -6, -11),
                   'rscp': (-60, -85, -95),
                  }

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

conditions_list = ['excellent',  'good',  'mid cell', 'cell edge']
colors_list = [bcolors.OKBLUE, bcolors.OKGREEN, bcolors.WARNING, bcolors.FAIL]

stop_color = bcolors.ENDC


def get_quality_signal(value, signal):
    for index, threshold in enumerate(lte_quality_signal_dict[signal]):
        if value >= threshold:
            return conditions_list[index]
    return conditions_list[3]

def get_color_signal(value, signal):
    for index, threshold in enumerate(lte_quality_signal_dict[signal]):
        if value >= threshold:
            return colors_list[index]
    return colors_list[3]

class Graphic_Signal_Info():
    def __init__(self, client):
        signal_info = SignalInfo.SignalInfo(client)
        self.rsrq = signal_info.get_rsrq()
        self.rsrp = signal_info.get_rsrp()
        self.sinr = signal_info.get_sinr()
        self.rssi = signal_info.get_rssi()
        self.ecio = signal_info.get_ecio()
        self.rscp = signal_info.get_rscp()

    def get_quality_rsrq(self):
        return get_quality_signal(self.rsrq, 'rsrq')

    def get_quality_rsrp(self):
        return get_quality_signal(self.rsrp, 'rsrp')

    def get_quality_sinr(self):
        return get_quality_signal(self.sinr, 'sinr')
        
    def get_quality_rssi(self):
        return get_quality_signal(self.rssi, 'rssi')

    def get_quality_ecio(self):
        return get_quality_signal(self.ecio, 'ecio')

    def get_quality_rscp(self):
        return get_quality_signal(self.rscp, 'rscp')       
        
    def get_color_rsrq(self):
        return get_color_signal(self.rsrq, 'rsrq')

    def get_color_rsrp(self):
        return get_color_signal(self.rsrp, 'rsrp')

    def get_color_sinr(self):
        return get_color_signal(self.sinr, 'sinr')
        
    def get_color_rssi(self):
        return get_color_signal(self.rssi, 'rssi')

    def get_color_ecio(self):
        return get_color_signal(self.ecio, 'ecio')

    def get_color_rscp(self):
        return get_color_signal(self.rscp, 'rscp')

    def get_rsrq_string(self):
        rsrq = self.rsrq
        rsrq_cdt = self.get_quality_rsrq() 
        rsrq_color = self.get_color_rsrq() 
        return f'{rsrq_color}{rsrq}dB{stop_color} ({rsrq_color}{rsrq_cdt}{stop_color}, best should be {bcolors.OKBLUE}> -10dB{stop_color})'

    def get_rsrp_string(self):
        rsrp = self.rsrp
        rsrp_cdt = self.get_quality_rsrp() 
        rsrp_color = self.get_color_rsrp() 
        return f'{rsrp_color}{rsrp}dBm{stop_color} ({rsrp_color}{rsrp_cdt}{stop_color}, best should be {bcolors.OKBLUE}> -80dBm{stop_color})'

    def get_sinr_string(self):
        sinr = self.sinr
        sinr_cdt = self.get_quality_sinr() 
        sinr_color = self.get_color_sinr() 
        return f'{sinr_color}{sinr}dB{stop_color} ({sinr_color}{sinr_cdt}{stop_color}, best should be {bcolors.OKBLUE}> 20dB{stop_color})'

    def get_rssi_string(self):
        rssi = self.rssi
        rssi_cdt = self.get_quality_rssi() 
        rssi_color = self.get_color_rssi() 
        return f'{rssi_color}{rssi}dB{stop_color} ({rssi_color}{rssi_cdt}{stop_color}, best should be {bcolors.OKBLUE}> -70dB{stop_color})'
  
    def get_ecio_string(self):
        ecio = self.ecio
        ecio_cdt = self.get_quality_ecio() 
        ecio_color = self.get_color_ecio() 
        return f'{ecio_color}{ecio}dB{stop_color} ({ecio_color}{ecio_cdt}{stop_color}, best should be {bcolors.OKBLUE}> -6dB{stop_color})'

    def get_rscp_string(self):
        rscp = self.rscp
        rscp_cdt = self.get_quality_rscp() 
        rscp_color = self.get_color_rscp() 
        return f'{rscp_color}{rscp}dB{stop_color} ({rscp_color}{rscp_cdt}{stop_color}, best should be {bcolors.OKBLUE}> -60dB{stop_color})'
