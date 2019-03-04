'''
File: totp.py
Author: yanfly
Email: languantan@gmail.com
Github: https://github.com/languantan
Description: main file to talk to tunnelblick
'''

from subprocess import Popen, PIPE
import pyotp 
import keyring

VPN_SERVERS = ['profile1', 'profile2']


def main():
    """TODO: Docstring for main.
    :returns: TODO
    """
    print(' '.join([f'{i}) {x}' for i, x in enumerate(VPN_SERVERS)]))

    vpn_selection = int(input('Select VPN server: '))

    vpn_server = VPN_SERVERS[vpn_selection]

    vpn_key = keyring.get_password('totp-cli', vpn_server)
    if not vpn_key:
        print('No keyring found')
        vpn_key = input('Enter VPN OTP key:')
        keyring.set_password('totp-cli', vpn_server, vpn_key)

    try:
        totp = pyotp.TOTP(vpn_key)
        clipboard = Popen('pbcopy', stdin=PIPE)
        clipboard.communicate(totp.now().encode())
        print(totp.now() + ' copied to clipboard')
    except Exception as e:
        print(e)
        print('Invalid totp key, please delete from keychain totp-cli:' + vpn_server)
        return

    connect_script = f'''
    tell application "Tunnelblick"
        disconnect all
        connect "{vpn_server}"
        get state of first configuration where name = "{vpn_server}"
        repeat until result = "CONNECTED" or result = "EXITING"
            delay 1
            get state of first configuration where name = "{vpn_server}"
        end repeat
    end tell'''

    applescript = Popen(['osascript'], stdin=PIPE)
    applescript.communicate(connect_script.encode())

    print('')
    print('give thanks to yanfly,broly')


if __name__ == "__main__":
    m
