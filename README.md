# / Sekai Connection /

An experiment of conencting blogrolls.

## Building

Type `make`. this will generate `output.svg` which you can open in the browser.

## Writing YAML

Place a YAML file like this:

```
# 你的显示名
name:
# 你的用户名（ASCII Only 时）
nick: user
# 你的网站或博客（网站优先）
site:
# 你的博客友链，是个列表，列表里面是友链对象的 ASCII Only Nick
links:
  # 像这样一行一项
  - another_user
```

and it will be used for generating graphs.
