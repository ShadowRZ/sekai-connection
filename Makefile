# -*- Makefile -*-

# Layouter.
LAYOUTER = neato

# Arguments to layouter.
GVFLAGS = -Nshape=doublecircle -Ncolor=yellow -Goverlap=false

svg: output.svg

output.gv: $(wildcard data/*.yml)
	@{ printf 'digraph {\n'; python3 ./generate.py $^; printf '}'; } > $@

output.svg: output.gv
	@echo ' NEATO	output.svg'
	@$(LAYOUTER) $(GVFLAGS) $< -Tsvg > $@


.PHONY: svg
