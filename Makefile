# -*- Makefile -*-

# Python.
PYTHON3 = python3

svg: sekai-connection.svg
png: sekai-connection.png
jpeg: sekai-connection.jpeg
pdf: sekai-connection.pdf

sekai-connection.svg: $(wildcard data/*.yml)
	@echo '  GENERATE.PY	sekai-connection.gv.svg'
	@$(PYTHON3) generate.py svg $^

sekai-connection.png: $(wildcard data/*.yml)
	@echo '  GENERATE.PY	sekai-connection.gv.png'
	@$(PYTHON3) generate.py png $^

sekai-connection.jpeg: $(wildcard data/*.yml)
	@echo '  GENERATE.PY	sekai-connection.gv.jpeg'
	@$(PYTHON3) generate.py jpeg $^

sekai-connection.pdf: $(wildcard data/*.yml)
	@echo '  GENERATE.PY	sekai-connection.gv.pdf'
	@$(PYTHON3) generate.py pdf $^

.PHONY: svg png jpeg pdf
