
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	autotools.rawConfigure("--prefix=/usr")
					
def build():
	autotools.make()
	
def install():
	autotools.install()
	pisitools.domove("/usr/lib/libz*.so*", "/lib/")
	pisitools.dosym("/lib/libz.so.1.2.7", "/usr/lib/libz.so")
	pisitools.dodoc("ChangeLog", "README")
