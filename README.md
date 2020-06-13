# / Sekai Connection /

An experiment of connecting blogrolls.

## Dependency

- [Python 3](https://www.python.org): Python is used for generating DOT file.
- [PyYAML](https://pyyaml.org): Read YAML files under `data/`.
- [Graphviz](https://graphviz.org): For drawing graph.
- [Python Graphviz binding](https://graphviz.readthedocs.io): Generate DOT file.

## Building

Type `make`. this will generate `sekai-connection.gv.svg` which you can open in the browser.

## Writing YAML

Place a YAML file in `data/` like this:

```
# 你的显示名
name:
# 你的用户名（ASCII Only 时）
nick: user
# 你的网站或博客
site:
# 你的博客友链，是个列表，列表里面是友链对象的网站
links:
  # 像这样一行一项
  - https://example.com
```

and it will be used for generating graphs.

## Chat

`#archlinux-cn-offtopic` @ Freenode
