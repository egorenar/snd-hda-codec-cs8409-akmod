
====================
Install dependencies
====================

.. code-block:: bash

		sudo dnf install akmods
		sudo dnf install fedora-packager rpmdevtools gcc
		sudo dnf install buildsys-build-rpmfusion-kerneldevpkgs-current

===============
Set up rpmbuild
===============

.. code-block:: bash

		rpmdev-setuptree
		cp snd-hda-codec-cs8409-akmod/*.spec ~/rpmbuild/SPECS/
		spectool -gR ~/rpmbuild/SPECS/snd-hda-codec-cs8409-kmod.spec

==========
Build RPMs
==========

.. code-block:: bash

		rm -f ~/rpmbuild/RPMS/x86_64/*.rpm
		rpmbuild -ba ~/rpmbuild/SPECS/snd-hda-codec-cs8409-kmod*.spec

============
Install RPMs
============

.. code-block:: bash

		sudo dnf install ~/rpmbuild/RPMS/x86_64/*.rpm

==============
Trigger akmods
==============

.. code-block:: bash

		sudo akmods --rebuild

==========
References
==========

- https://developer.fedoraproject.org/deployment/rpm/about.html
- https://github.com/HikariKnight/looking-glass-kvmfr-akmod
- https://github.com/neatbasis/sunhme2g
- https://github.com/gladion136/tuxedo-drivers-kmod
