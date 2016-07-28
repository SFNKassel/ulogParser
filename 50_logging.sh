#!/bin/sh
iptables -t nat -I PREROUTING -j NFLOG
