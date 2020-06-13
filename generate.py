#!/usr/bin/env python
import yaml
import sys
import uuid
import graphviz
import hashlib
from urllib.parse import urlparse

from conf import GRAPH_EDGE_ATTRS, GRAPH_NODE_ATTRS, GRAPH_GRAPH_ATTRS

def get_id(site):
    location = get_netloc(site)
    if location in {'about.me', 'home.ustc.edu.cn'}:
        return str(uuid.uuid5(uuid.NAMESPACE_URL, site))
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, get_netloc(site)))

def get_netloc(site):
    return urlparse(site).netloc

def get_color(site):
    loc = get_netloc(site)
    h = hashlib.md5(loc.encode('utf-8'))
    return f'#{h.hexdigest()[0:6]}'

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
    g = graphviz.Digraph(
            '/ Sekai Connection /',
            engine='neato',
            node_attr=GRAPH_NODE_ATTRS,
            edge_attr=GRAPH_EDGE_ATTRS,
            graph_attr=GRAPH_GRAPH_ATTRS
            )
    for k, m in d.items():
        nick = m['nick'] or f
        name = m['name'] or '(?????)'
        links = m['links'] or []
        site = m['site'] or ''
        node_id = get_id(site)
        color = get_color(site)
        fontcolor = 'black'
        if 'color' in m:
            color = m['color']
        if 'fontcolor' in m:
            fontcolor = m['fontcolor']
        g.node(node_id, label=f'<<b>{name}</b><br/>{site}>', URL=site, color=color, tooltip=f'{name} - {site}', fontcolor=fontcolor)
        for i in links:
            if get_netloc(i) in d:
                g.edge(node_id, get_id(i), color=color)
            else:
                sys.stderr.write(f'// !! WARNING: No node of {i} found. (from {site} of {nick})\n')
    return g

if __name__ == '__main__':
    fmt = sys.argv[1]
    g = gen_defs(sys.argv[2:])
    g.render(filename='sekai-connection.gv', format=fmt)
