#!/usr/bin/python3

from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.exceptions import ResponseErrorLoginCsfrException
import time
from reprint import output
from GraphicTrafficInfo import Graphic_Traffic_Info
from GraphicSignalInfo import Graphic_Signal_Info
from login import *


def print_traffic(client, output_lines):
    graphic_traffic_info = Graphic_Traffic_Info(client)
    graphic_download = graphic_traffic_info.get_dwn_string()
    graphic_upload = graphic_traffic_info.get_up_string()
    output_lines['Rate download'] = graphic_download
    output_lines['Rate upload'] = graphic_upload

def print_signal(client, output_lines):
    graphic_signal_info = Graphic_Signal_Info(client)
    graphic_rssi = graphic_signal_info.get_rssi_string()
    graphic_ecio = graphic_signal_info.get_ecio_string()
    graphic_rscp = graphic_signal_info.get_rscp_string()
    output_lines['rssi'] = graphic_rssi
    output_lines['ecio'] = graphic_ecio
    output_lines['rscp'] = graphic_rscp

def main():
    connection = AuthorizedConnection(f'http://{ip}/', login, password)
    with output(output_type='dict') as output_lines:
        while True:
            try:
                client = Client(connection)
                print_signal(client, output_lines)
                print_traffic(client, output_lines)
                time.sleep(1)
            except ResponseErrorLoginCsfrException:
                connection = AuthorizedConnection(f'http://{ip}/', login, password)
    client.user.logout()

main()

