#!/usr/bin/env python
import yaml
import sys
import uuid
import graphviz
from urllib.parse import urlparse

def get_id(site):
    location = get_netloc(site)
    if location == 'about.me':
        return str(uuid.uuid5(uuid.NAMESPACE_URL, site))
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, get_netloc(site)))

def get_netloc(site):
    return urlparse(site).netloc

def get_dict(files):
    ret = {}
    for i in files:
        with open(i) as f:
            m = yaml.safe_load(f)
            nick = m['nick']
            site = m['site']
            ret[get_netloc(site)] = m
    return ret

def gen_defs(files):
    d = get_dict(files)
    g = graphviz.Digraph('/ Sekai Connection /')
    for k, m in d.items():
        nick = m['nick'] or f
        name = m['name'] or '(?????)'
        links = m['links'] or []
        site = m['site'] or ''
        node_id = get_id(site)
        color = 'pink'
        if 'color' in m:
            color = m['color']
        g.node(node_id, label=f'<<b>{name}</b><br/>{site}>', URL=site, color=color, tooltip=f'{name} - {site}')
        for i in links:
            if get_netloc(i) in d:
                g.edge(node_id, get_id(i))
            else:
                sys.stderr.write(f'// !! WARNING: No node of {i} found. (from {site} of {nick})\n')
    print(g.source)

if __name__ == '__main__':
    gen_defs(sys.argv[1:])
