make:
	python setup.py build
	python setup.py install
	python run.py
	
make tests:
	#sleep 1
	python test/test_request_handler.py
