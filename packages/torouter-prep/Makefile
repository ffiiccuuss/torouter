default: build

build:
	echo "nothing to build"

install:
	install -o root -g root -m 750 src/torouter_config.sh $(DESTDIR)/usr/bin
	install -o root -g root -m 750 src/torouter_takeover.sh $(DESTDIR)/usr/bin

clean:
	echo "nothing to clean"

deb:
	dpkg-buildpackage -us -uc
