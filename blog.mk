deploy:
	aws s3 cp --recursive _build/html/ s3://blog.aclark.net
	aws cloudfront create-invalidation --distribution-id ER61U0W7M90OK --paths "/*"

deploy-clean:
	aws s3 rm --recursive s3://blog.aclark.net/

build:
	$(MAKE) sphinx-build
