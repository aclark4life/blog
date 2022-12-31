eb-deploy:
	aws s3 cp --recursive _build/html/ s3://blog.aclark.net
	aws cloudfront create-invalidation --distribution-id ER61U0W7M90OK --paths "/*"

readme-build:
	$(MAKE) sphinx-build

readme-edit:
	$(MAKE) sphinx-edit

readme-open:
	open http://0.0.0.0:8000

sphinx-edit:
	vi index.rst

django-serve:
	$(MAKE) sphinx-serve
