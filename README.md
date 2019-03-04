# vpn-start
easy python script that talks to Keychain to connect to Tunnelblick profiles that requires Open MFA standards.

# Requirements
- Python 3
- `pip install pyotp`
- Tunnelblick

# Configure
Update `VPN_SERVERS` array to match profile names in Tunnelblick

# How-to use
- Run python `totp.py`.
- On first run, it will prompt for 2FA base key. After keying in, the key will be stored in your system keychain
- It will then generate and copy the 2FA OTP to your clipboard.
- When the tunnelblick dialog appears, paste it in.
- CONNECTED!
