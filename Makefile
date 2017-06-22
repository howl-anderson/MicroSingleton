PACKAGE_NAME = micro_singleton

all: uninstall_package build_package install_package
	pass

uninstall_package:
	-pip uninstall -y ${PACKAGE_NAME}

build_package:
	python setup.py bdist_wheel --universal

install_package:
	pip install ./dist/*.whl
