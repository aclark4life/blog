deploy:
	aws s3 rm --recursive s3://blog.aclark.net
	aws s3 cp --recursive _build/html/ s3://blog.aclark.net
	aws cloudfront create-invalidation --distribution-id ER61U0W7M90OK --paths "/*" | cat

build:
	$(MAKE) sphinx-build

clean:
	rm -rvf _build/
	aws s3 rm --recursive s3://blog.aclark.net/
