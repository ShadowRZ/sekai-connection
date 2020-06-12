# -*- Makefile -*-

# Layouter.
LAYOUTER = neato

# Arguments to layouter.
GVFLAGS = -Nshape=doublecircle -Ncolor=yellow -Goverlap=false

svg: output.svg

output.gv: $(wildcard data/*.yml)
	@echo '  GENERATE.PY	output.gv'
	@python3 ./generate.py $^ > $@

output.svg: output.gv
	@echo '  NEATO	output.svg'
	@$(LAYOUTER) $(GVFLAGS) $< -Tsvg > $@

.PHONY: svg
