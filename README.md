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

## ps.py

Like `ps -fHe` on linux, but portable to the extent that `psutil` is. Works on macOS at least.

```
$ ps.py | head
              USER   PID  PPID NIC  %CPU  %MEM   #TH             STARTED COMMAND
              root     0     ?   ?     ?     ?     ? 2023-02-10 07:21:25 kernel_task
              root     1     ?   ?     ?     ?     ? 2023-02-10 07:21:25   launchd
              root   299     1   ?     ?     ?     ? 2023-02-10 07:21:49     logd
              root   301     1   ?     ?     ?     ? 2023-02-10 07:21:49     UserEventAgent
              root   303     1   ?     ?     ?     ? 2023-02-10 07:21:49     uninstalld
              root   304     1   ?     ?     ?     ? 2023-02-10 07:21:49     fseventsd
              root   307     1   ?     ?     ?     ? 2023-02-10 07:21:49     systemstats
              root   748   307   ?     ?     ?     ? 2023-02-10 07:22:05       systemstats
              root   309     1   ?     ?     ?     ? 2023-02-10 07:21:49     configd
Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
BrokenPipeError: [Errno 32] Broken pipe
$ sudo ps.py | head
              USER   PID  PPID NIC  %CPU  %MEM   #TH             STARTED COMMAND
              root     0     ?   ?   0.0   0.0   574 2023-02-10 07:21:25 kernel_task
              root     1     ?   ?   0.0   0.1     6 2023-02-10 07:21:25   /sbin/launchd
              root   299     1   ?   0.0   0.1     4 2023-02-10 07:21:49     /usr/libexec/logd
              root   301     1   ?   0.0   0.0     4 2023-02-10 07:21:49     /usr/libexec/UserEventAgent (System)
              root   303     1   ?   0.0   0.0     2 2023-02-10 07:21:49     /System/Library/PrivateFrameworks/Uninstall.framework/Resources/uninstalld
              root   304     1   ?   0.0   0.0    13 2023-02-10 07:21:49     /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/FSEvents.framework/Versions/A/Support/fseventsd
              root   307     1   ?   0.0   0.1     3 2023-02-10 07:21:49     /usr/sbin/systemstats --daemon
              root   748   307   ?   0.0   0.0     3 2023-02-10 07:22:05       /usr/sbin/systemstats --logger-helper /private/var/db/systemstats
              root   309     1   ?   0.0   0.0     7 2023-02-10 07:21:49     /usr/libexec/configd
Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
BrokenPipeError: [Errno 32] Broken pipe
```