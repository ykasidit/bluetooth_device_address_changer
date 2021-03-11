Bluetooth device address changer
-------------------------------

For changing bluetooth device address of USB Bluetooth dongles that came with same bluetooth device addresses, on Ubuntu GNU/Linux.

This uses the `bdaddr` binary compiled from from BlueZ. If the binary doesn't work on your platform, please re-compile and replace with new binary.

How to use
----------

- Plug in your USB Bluetooth dongle.
- Run `change.sh`

How to change the address used
------------------------------

- Edit 'last_bd_addr.txt' - this script runs bdaddr numbers from there.

LICENSE
-------

This project is released under the same license as 'BlueZ' - GNU GPL - Please see the LICENSE file.

AUTHORS
-------

Kasidit Yusuf
