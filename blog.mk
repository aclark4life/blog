eb-deploy:
	rm -rvf _build/
	$(make) sphinx-build
	aws s3 cp --recursive _build/html/ s3://blog.aclark.net
	aws cloudfront create-invalidation --distribution-id ER61U0W7M90OK --paths "/*"
