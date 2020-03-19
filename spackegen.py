#!/usr/bin/env python3

import yaml
import json
import sys

def t(d):
    if arch not in d:
        return []
    return d[arch]

def dif(a,b):
    return [x for x in a if x not in b]

def print_usage():
    print("Usage: {} <os> <arch> <compiler>".format(sys.argv[0]))

if len(sys.argv) < 4:
    print_usage()
    sys.exit(1)

opsys, arch, compiler = sys.argv[1], sys.argv[2], sys.argv[3]

dd = yaml.safe_load(open("master-manifest.yaml"))

of = open('new-spack.yaml','w')
nfdd = {"spack":{}}
spack = nfdd["spack"]

# specs
specs = dif(dd['specs'], t(dd['specs-exclude']))
spack['specs'] = ["{s} {compiler} arch=linux-{opsys}-{arch}"
    .format(s=s, compiler=compiler, opsys=opsys, arch=arch) for s in specs]

# package preferences
spack['packages'] = dd['packages']['all']

yaml.dump({"spack":spack}, of, default_flow_style=False)
of.close()
