debs: webdeb prepdeb wirelessdeb

webdeb:
	# By default we will but not sign for now
	cd torouter-web && debuild --no-tgz-check -us -uc

prepdeb:
	# By default we will but not sign for now
	cd torouter-prep && debuild --no-tgz-check -us -uc

wirelessdeb:
	# By default we will but not sign for now
	cd dreamplug-uaputl && debuild --no-tgz-check -us -uc
