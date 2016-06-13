NAME=VisIt_workshop

TARGET=$(NAME).pdf
SOURCE=$(NAME).tex

JUNK=.aux .bbl .blg .dvi .log .nav .out .ps .pdf .snm .tex.backup .tex.bak .toc Notes.bib
junk2=.aux .bbl .blg .dvi .log .nav .out .ps .snm .tex.backup .tex.bak .toc Notes.bib

.PHONY: clean

$(TARGET): $(SOURCE) *tex
	@pdflatex $(SOURCE)
	#@bibtex $(NAME)
	@pdflatex $(SOURCE)
	@pdflatex $(SOURCE)

all: $(TARGET)

clean:
	@for ext in $(JUNK); do \
		rm -v $(NAME)$$ext; \
	done

softclean:
	@for ext in $(junk2); do \
		rm -v *$$ext; \
	done

realclean:
	@for ext in $(JUNK); do \
		rm -v *$${ext};	\
	done

upload:
	zip -r -X visit.zip VisIt_workshop.pdf additionalData
	@/bin/mv -f visit.zip ~/Dropbox/Public/visualization
