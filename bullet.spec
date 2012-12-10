%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Professional 3D collision detection library
Name:		bullet
Version:	2.80
Release:	1
License:	Zlib
Group:		System/Libraries
URL:		http://www.bulletphysics.com
Source0:	http://bullet.googlecode.com/files/%{name}-%{version}-rev2531.tgz
Patch0:		bullet-2.80-extras-version.patch
BuildRequires:	doxygen
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glut)
BuildRequires:	cmake
BuildRequires:	libtool
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	graphviz
BuildRequires:	perl-Template-Toolkit

%description
Bullet is a professional open source multi-threaded 
3D Collision Detection and Rigid Body Dynamics Library
for games and animation.

%package demo
Summary:	A demo programs using bullet library
Group:		Graphics
Requires:	%{libname} = %{version}-%{release}

%description demo
A demo programs using bullet library.

%package -n %{libname}
Summary:	Professional 3D collision detection library
Group:		System/Libraries

%description -n %{libname}
Bullet 3D Game Multiphysics Library provides state of the art 
collision detection, soft body and rigid body dynamics.

* Used by many game companies in AAA titles on Playstation 3, 
  XBox 360, Nintendo Wii and PC
* Modular extendible C++ design with hot-swap of most components
* Optimized back-ends with multi-threaded support for Playstation 3 
  Cell SPU and other platforms
* Discrete and continuous collision detection (CCD)
* Swept collision queries
* Ray casting with custom collision filtering
* Generic convex support (using GJK), capsule, cylinder, cone, sphere, 
  box and non-convex triangle meshes. 
* Rigid body dynamics including constraint solvers, generic 
  constraints, ragdolls, hinge, ball-socket
* Support for constraint limits and motors
* Soft body support including cloth, rope and deformable
* Bullet is integrated into Blender 3D and provides a Maya Plugin
* Supports import and export into COLLADA 1.4 Physics format
* Support for dynamic deformation of non-convex triangle meshes, by 
  refitting the acceleration structures 

The Library is free for commercial use and open source 
under the ZLib License.

%package -n %{develname}
Summary:	Development headers for bullet
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	pkgconfig(libxml-2.0)

%description -n %{develname}
Development headers for bullet 3D collision library.

%prep
%setup -qn %{name}-%{version}-rev2531
%patch0 -p1
rm -f src/BulletMultiThreaded/GpuSoftBodySolvers/OpenCL/CMakeLists.txt Demos/OpenCLClothDemo/CMakeLists.txt

%build
%cmake \
	-DBUILD_EXTRAS=ON -DINCLUDE_INSTALL_DIR=%{_includedir}/bullet
%make

%install
cd build
%makeinstall_std

#install demos
mkdir -p %{buildroot}%{_bindir}
for i in `find -type f -name *Demo`; do
    install -m 755 $i %{buildroot}%{_bindir}/bullet-`basename $i`
done

# install libs from Extras
pushd Extras
find . -name '*.so*' -exec cp -a {} %{buildroot}%{_libdir} \;
popd
# install libs from Demos
pushd Demos
find . -name '*.so*' -exec cp -a {} %{buildroot}%{_libdir} \;
popd

pushd %{buildroot}%{_libdir}
for f in lib*.so.*.*
do
  ln -sf $f ${f%\.*}
done
popd

%files demo
%{_bindir}/%{name}-*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS README COPYING ChangeLog NEWS VERSION *.pdf
%dir %{_includedir}/%{name}
%{_libdir}/*.so
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Mon Jan 09 2012 Andrey Bondrov <abondrov@mandriva.org> 2.79-1mdv2012.0
+ Revision: 758789
- Update BuildRequires
- New version 2.79, spec cleanup

* Tue Jun 14 2011 Funda Wang <fwang@mandriva.org> 2.78-1
+ Revision: 685133
- br cmake
- sync with fedora 2.78

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.75-3mdv2011.0
+ Revision: 610085
- rebuild

* Sun May 09 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 2.75-2mdv2010.1
+ Revision: 544274
- rebuild

* Sun Sep 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.75-1mdv2010.0
+ Revision: 449892
- Patch0: fix undefinied symbols
- update to new version 2.75

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Mar 29 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.74-2mdv2009.1
+ Revision: 362177
- fix symlinks creation (mdvbz #49283)

* Tue Mar 17 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.74-1mdv2009.1
+ Revision: 356989
- update to new version 2.74

* Sun Jan 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.73-1mdv2009.1
+ Revision: 328422
- update to new version 2.73
- drop patch 2
- rediff patch 3
- use %%define Werror_cflags %%nil and %%define _disable_ld_no_udefined 1 too much work
- provide all libraries as a shared objects

* Sun Oct 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.72-1mdv2009.1
+ Revision: 293033
- update to new version 2.72

* Mon Sep 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.71-1mdv2009.0
+ Revision: 282548
- update to new version 2.71
- better description

* Sun Aug 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.70-2mdv2009.0
+ Revision: 275516
- Patch2: rediff against latest bullet version
- update to new version 2.70

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 01 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.69-1mdv2009.0
+ Revision: 213860
- update to new version 2.69

* Fri Apr 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.68-2mdv2009.0
+ Revision: 197348
- Patch1: create one more share library
- fix url

* Thu Apr 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.68-1mdv2009.0
+ Revision: 197220
- Patch3: rediff
- add missing buildrequires on graphviz and perl-Template-Toolkit
- get rid of missing newlines in source files
- fix file list
- new version

* Thu Mar 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.67-4mdv2008.1
+ Revision: 187554
- add more explicit provides for static library package

* Wed Mar 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.67-3mdv2008.1
+ Revision: 187135
- fix symlinks creation (#38749)

* Sun Mar 09 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.67-2mdv2008.1
+ Revision: 183143
- add scriplets
- new version
- drop patch 0
- Patch1: build shared libraries !
- Patch2: fixes against 64 bit architecture
- Patch3: use system libxml2
- strict-aliasting breaks building, so disable it
- get ride of few no-newline warnings
- create package demo, which include all demo programs using bullet library
- fix typo in a header (p0)
- regenerate scripts
- fix building of demos, since parallel build is broken
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.63-1mdv2008.1
+ Revision: 100537
- new version
- use ftjam
- new upstream version
- add provides

* Tue Jun 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.53-1mdv2008.0
+ Revision: 44271
- make it compiliant with mandriva's library policy
- drop %%post and %%postun
- fix file list
- spec file clean
- Import bullet

