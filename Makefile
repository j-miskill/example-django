make:
	python3 setup.py build
	python3 setup.py install
	
make tests:
	#sleep 1
	python3 test/test_request_handler.py