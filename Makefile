ZIPNAME = lambda
FILES = $(wildcard *.py)

.PHONY: all
all:
	rm -f $(ZIPNAME).zip~
	zip $(ZIPNAME) $(FILES)
