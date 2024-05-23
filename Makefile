.PHONY: package_layer_zip logic_layer_zip

package_layer_zip:
	rm -rf package package.zip || true
	mkdir -p ./package/python
	pip install --target ./package/python -r requirements.txt
	(cd package && zip -r ../package.zip .)
	rm -rf package

logic_layer_zip:
	rm ./logic_code.zip || true
	zip ./logic_code.zip src/*.py