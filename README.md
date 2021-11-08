# rebooter
rebooter
Reboot PR21 once a day

1 - Transfer the snap to PR21: sudo scp rebooter_0.1_amd64.snap boschrexroth@192.168.1.1:/home/boschrexroth/

2 - SSH into PR21: ssh boschrexroth@192.168.1.1

3 - install snap sudo snap install rebooter_0.1_amd64.snap --devmode

4 - test to see if snap is ok sudo snap run rebooter

You should see the actual time printed. It will reboot once time is 00:00:00.

Obs.: Everything is hardcoded! To modify and snap your modification: 1 - clone this repo 2 - modify 3 - call snapcraft snapcraft (if using a ubuntu machine) snapcraft --use-lxd (if using a vm)
