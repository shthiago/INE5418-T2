import argparse
import json
import sys
import socket

from node import Node


class Commander:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Send commands to running rings',
        )

        parser.add_argument('command', help='Subcommand to trigger')

        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Command not found')
            parser.print_help()
            sys.exit(1)

        getattr(self, args.command)()

    def start(self):
        parser = argparse.ArgumentParser(
            description='Start a node ring'
        )
        parser.add_argument('num_nodes', help='Number of nodes', type=int)

        args = parser.parse_args(sys.argv[2:])

        base_port = 12300
        for i in range(args.num_nodes):
            if i == args.num_nodes - 1:
                next_port = base_port

            else:
                next_port = base_port + i + 1

            Node(identifier=i,
                 host='localhost',
                 port=base_port + i,
                 next_host='localhost',
                 next_port=next_port)

    def kill(self):
        parser = argparse.ArgumentParser(
            description='Kill a node'
        )
        parser.add_argument('host', help='Host of the target node', type=str)
        parser.add_argument('port', help='Port of the target node', type=int)

        args = parser.parse_args(sys.argv[2:])

        sock = socket.socket(family=socket.AF_INET,
                             type=socket.SOCK_STREAM)
        sock.connect((args.host, args.port))
        msg = {'type': 'abort', 'dest': 'any'}
        sock.send(json.dumps(msg).encode())

    def elections(self):
        parser = argparse.ArgumentParser(
            description='Kill a node'
        )
        parser.add_argument('host', help='Host of the target node', type=str)
        parser.add_argument('port', help='Port of the target node', type=int)

        args = parser.parse_args(sys.argv[2:])

        sock = socket.socket(family=socket.AF_INET,
                             type=socket.SOCK_STREAM)
        sock.connect((args.host, args.port))
        msg = {'type': 'start_election', 'dest': 'any'}
        sock.send(json.dumps(msg).encode())

    def print(self):
        parser = argparse.ArgumentParser(
            description='Kill a node'
        )
        parser.add_argument('host', help='Host of the target node', type=str)
        parser.add_argument('port', help='Port of the target node', type=int)

        args = parser.parse_args(sys.argv[2:])

        sock = socket.socket(family=socket.AF_INET,
                             type=socket.SOCK_STREAM)
        sock.connect((args.host, args.port))
        msg = {'type': 'print', 'dest': 'any'}
        sock.send(json.dumps(msg).encode())


if __name__ == '__main__':
    Commander()
