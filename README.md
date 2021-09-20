# Running instructions

Use the `commander.py` to run the tests.

## Starting a ring

Execute `python commander.py start N` with N being the number of nodes in the ring.

The ring initialize with no leaderm with all nodes binded to `localhost` and base port 12300 + n where n goes from 0 to N.

## Consulting a node status

Execute `python commander.py print HOST PORT` where HOST will be the host (`localhost`, probably) and PORT the port of the node you want to check. 

**Tip**: On startup, nodes log their host and port.

## Killing a node

To see the ring restoring itself by killing a node, run `python commander.py kill HOST PORT` where HOST will be the host (`localhost`, probably) and PORT the port of the node you want to kill.

## Starting elections 

To make the ring elect a leader, run `python commander.py elections HOST PORT` where HOST will be the host (`localhost`, probably) and PORT the port of the node you want to start the elections. Any node might get it done.

## Starting problematic elections

To start elections with the ring broken, run the ring with any number os nodes (let's say, 20) `python commander.py kill HOST1 PORT1 && python commander.py election HOST2 PORT2` where `HOST1`/`PORT1` is some node to kill and `HOST2`/`PORT2` another node to start the elections. The node that communicate with the killed node will loop the election first round message until the node that comes after the killed one asks for restore. The restoring process will run, then the election's first round will finish and the second will starts. the election shoul finish correctly.

If you make a node call for elections and it dies somewhy (don't kill it).