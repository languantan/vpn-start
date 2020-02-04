# vpn-start

easy python script that talks to Keychain to connect to Tunnelblick profiles that requires Open MFA standards.

# Requirements

- Python 3
- `pip install pyotp keyring`
- Tunnelblick

# Configure

Update `VPN_SERVERS` array to match profile names in Tunnelblick

# How-to use

- When logging in for the first time to the OpenVPN server, save the 2FA base key. It should look something like: BZBODYDFSG0AW5Y3
- **IMPT NOTE: base key is only shown on the first login**
- Run `python totp.py`
- On first run, it will prompt for 2FA base key. After keying in, the key will be stored in your system keychain
- It will then generate and copy the 2FA OTP to your clipboard
- When the tunnelblick dialog appears, paste it in
- CONNECTED!
