#!/usr/bin/env python3
# Python CLI for parsing shitlist and generating various
# firewall rules based on the list

import click
import os

BASEDIR = os.path.dirname(__file__)

def list_file(protocol, name):
    fname = '{protocol}-{name}.txt'.format(protocol=protocol, name=name)
    return os.path.join(BASEDIR, protocol, fname)

def parse_cidr_list(file_name):
    with open(file_name, 'r', encoding="UTF-8") as fp:
        for line in fp:
            # Strip comments
            content, __, comment = line.partition("#")
            cidr = content.strip()
            if cidr:
                yield cidr


@click.group()
def cli():
    pass

@cli.command()
def list():
    """Pretty print shitlist"""
    for proto in ['ipv4', 'ipv6']:
        click.echo("---------------------------------------------")
        click.echo("Listing bad {proto} prefixes".format(proto=proto))
        click.echo("")
        for reason, description in (
                ('not-forwardable', 'Not forwardable addresses:'),
                ('not-valid-destination', 'Not valid as destination:'),
                ('not-valid-source', 'Not valid as source')):
            click.echo()
            click.echo(description)
            for cidr in parse_cidr_list(list_file(proto, reason)):
                click.echo("- {cidr}".format(cidr=cidr))

# TODO: Implement iptables output
# TODO: Implement pf output

if __name__ == '__main__':
    cli()
