# Custom Makefile
# Add your custom makefile commands here
#
PROJECT_NAME := blog
all:
	python -m venv .; source bin/activate; $(MAKE) install; $(MAKE) build deploy

build:
	rm -rvf _build/html/
	$(MAKE) sphinx-build

deploy:
	aws s3 rm --recursive s3://blog.aclark.net/
	aws s3 cp --recursive _build/html/ s3://blog.aclark.net
	aws cloudfront create-invalidation --distribution-id ER61U0W7M90OK --paths "/*" | cat

edit:
	vi index.rst
