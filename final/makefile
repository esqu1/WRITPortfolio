all: Portfolio.tex
	pdftk coverletter.pdf brandonlinresume.pdf cat output output.pdf
	pdflatex Portfolio.tex
	pdflatex Portfolio.tex
	python toc.py
	pdftk A=Portfolio.pdf B=output.pdf cat A1-3 B A4-end output Final.pdf

clean:
	rm *.out *.log *.aux
	rm *~ > /dev/null 2>&1 || echo ""
