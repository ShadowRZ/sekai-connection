# -*- Makefile -*-

# Python.
PYTHON3 = python3

# Graph layouter.
LAYOUTER = neato

svg: sekai-connection.gv.svg
png: sekai-connection.gv.png
jpeg: sekai-connection.gv.jpeg
pdf: sekai-connection.gv.pdf

sekai-connection.gv: $(wildcard data/*.yml)
	@echo '  GENERATE.PY	sekai-connection.gv'
	@$(PYTHON3) generate.py $^

sekai-connection.gv.svg: sekai-connection.gv
	@echo '  DOT	sekai-connection.gv.svg'
	@dot -K$(LAYOUTER) -Tsvg $< -o$@

sekai-connection.gv.png: sekai-connection.gv
	@echo '  DOT	sekai-connection.gv.png'
	@dot -K$(LAYOUTER) -Tpng $< -o$@

sekai-connection.gv.jpeg: sekai-connection.gv
	@echo '  DOT	sekai-connection.gv.jpeg'
	@dot -K$(LAYOUTER) -Tjpg $< -o$@

sekai-connection.gv.pdf: sekai-connection.gv
	@echo '  DOT	sekai-connection.gv.pdf'
	@dot -K$(LAYOUTER) -Tpdf $< -o$@

# Preview
x11-preview: sekai-connection.gv
	@dot -K$(LAYOUTER) -Tx11 $<

missing:
	@$(PYTHON3) -c 'import generate; generate.find_missing()'

.PHONY: svg png jpeg pdf x11-preview missing
