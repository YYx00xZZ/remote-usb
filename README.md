# remote-usb

Aim to provide way for using iot serial usb devices remotely.
Lets assume we have rpi with 1 or more elecrow pump shield/s connected to usb. Alse we have zerotier-one setup.
what we want to accomplsh:
 - bidirectional comm
 - define command pattern for control fro RPi->serial device

For now on by server i mean rpi and by client you should understand any of the connected usb device
One way of achieving this is with `socat` tool
```bash
sudo socat PTY,raw,mode=666,echo=0,link=/dev/ttyVUSB0 tcp:10.147.17.10:7777
```


