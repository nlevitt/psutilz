# psutilz

Utilities built on the psutil library

## pslisten

Prints information about processes listening on ports (TCP and UDP, IPv4 and IPv6).

```
$ sudo pslisten
PROTO                        HOST  PORT           USER   PID  PPID NIC  %CPU  %MEM   #TH              STARTED COMMAND
 UDP4                     0.0.0.0   137       _netbios 60612     1  20   0.0   0.0     2  2022-12-08 03:03:43 /usr/sbin/netbiosd
 UDP4                     0.0.0.0   137           root     1     0   0   0.0   0.0     3  2022-12-01 00:00:50 /sbin/launchd
 UDP4                     0.0.0.0   138       _netbios 60612     1  20   0.0   0.0     2  2022-12-08 03:03:43 /usr/sbin/netbiosd
 UDP4                     0.0.0.0   138           root     1     0   0   0.0   0.0     3  2022-12-01 00:00:50 /sbin/launchd
 TCP4                   127.0.0.1   631           root 70386     1   0   0.0   0.0     3  2022-12-07 10:20:28 /usr/sbin/cupsd -l
 TCP6                         ::1   631           root 70386     1   0   0.0   0.0     3  2022-12-07 10:20:28 /usr/sbin/cupsd -l
 UDP4                     0.0.0.0  5353 _mdnsresponder   300     1   0   0.0   0.0     3  2022-12-01 00:00:55 /usr/sbin/mDNSResponder
 UDP6                          ::  5353 _mdnsresponder   300     1   0   0.0   0.0     3  2022-12-01 00:00:55 /usr/sbin/mDNSResponder
```

## dstat

A fork of https://github.com/dstat-real/dstat

![dstat](https://user-images.githubusercontent.com/423176/206405331-2914119b-29a8-40dd-a025-ad255257a4d2.gif)
