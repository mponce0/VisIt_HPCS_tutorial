NAME=VisIt_workshop

TARGET=$(NAME).pdf
SOURCE=$(NAME).tex

JUNK=.aux .bbl .blg .dvi .log .nav .out .ps .pdf .snm .tex.backup .tex.bak .toc Notes.bib

.PHONY: clean

$(TARGET): $(SOURCE)
	@pdflatex $(SOURCE)
	#@bibtex $(NAME)
	@pdflatex $(SOURCE)
	@pdflatex $(SOURCE)

all: $(TARGET)

clean:
	@for ext in $(JUNK); do \
		rm -v $(NAME)$$ext; \
	done

realclean:
	@for ext in $(JUNK); do \
		rm -v *$${ext};	\
	done
