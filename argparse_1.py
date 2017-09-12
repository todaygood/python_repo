import argparse
parser=argparse.ArgumentParser("tcp connect target:")
parser.add_argument("server_ip");
args = parser.parse_args()
print args.echo

