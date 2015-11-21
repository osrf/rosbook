DIAGRAMS=arm_2d_cartesian
DIAGRAM_SRCS=$(DIAGRAMS:%=%.tex)
DIAGRAM_PNGS=$(DIAGRAMS:%=%.png)
DIAGRAM_DEBRIS=$(DIAGRAMS:%=%.aux) $(DIAGRAMS:%=%.log) $(DIAGRAMS:%=%.pdf)

default: $(DIAGRAM_PNGS)

%.png: %.tex
	pdflatex -shell-escape $<

.PHONY: clean
clean:
	-rm $(DIAGRAM_PNGS) $(DIAGRAM_DEBRIS)
