debs: webdeb prepdeb mvdebs

webdeb:
	# By default we will but not sign for now
	#cd torouter-web && debuild --no-tgz-check -us -uc

prepdeb:
	# By default we will but not sign for now
	cd torouter-prep && debuild --no-tgz-check -us -uc

mvdebs:
	mv *.deb *.build *.changes *.dsc *.tar.gz packages-for-upload/

updatearchive:
	scp packages-for-upload/* vescum.torproject.org:/srv/torrouter.torproject.org/ftp-archive/archive/pool/torrouter/
	ssh vescum.torproject.org make -C /srv/torrouter.torproject.org/ftp-archive

