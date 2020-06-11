#!/usr/bin/env python
import yaml
import sys
import uuid

def get_id(string):
    return uuid.uuid5(uuid.NAMESPACE_URL, string)

def get_dict(files):
    ret = {}
    for i in files:
        with open(i) as f:
            m = yaml.safe_load(f)
            nick = m['nick']
            ret[nick.capitalize()] = m
    return ret

def gen_defs(files):
    d = get_dict(files)
    for k, m in d.items():
        nick = m['nick'] or f
        name = m['name'] or '(?????)'
        links = m['links'] or []
        site = m['site'] or ''
        color = 'pink'
        if 'color' in m:
            color = m['color']
        print(f'''\
{k} [label=<<b>{name}</b><br/>@{nick}> URL="{site}" color={color}];
''')
        for i in links:
            if i.capitalize() in d:
                print(f'{k} -> {i.capitalize()}')
            else:
                sys.stderr.write(f'// !! WARNING: No node of {i} found. (from {nick})\n')

if __name__ == '__main__':
    gen_defs(sys.argv[1:])
