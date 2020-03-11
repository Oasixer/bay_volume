ZIPNAME = lambda

PYTHON_FILES  = lambda_function.py

.PHONY: all
all:
	-rm $(ZIPNAME).zip
	zip $(ZIPNAME) $(PYTHON_FILES)
