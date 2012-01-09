%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Professional 3D collision detection library
Name:		bullet
Version:	2.79
Release:	%mkrel 1
License:	Zlib
Group:		System/Libraries
URL:		http://www.bulletphysics.com
Source0:	http://bullet.googlecode.com/files/%{name}-%{version}-rev2440.tgz
Patch0:		bullet-2.77-extras-version.patch
BuildRequires:	doxygen
BuildRequires:	GL-devel
BuildRequires:	mesaglut-devel
BuildRequires:	cmake
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	graphviz
BuildRequires:	perl-Template-Toolkit
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Requires:	libxml2-devel

%description -n %{develname}
Development headers for bullet 3D collision library.

%prep
%setup -q
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

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files demo
%defattr(-,root,root)
%{_bindir}/%{name}-*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS README COPYING ChangeLog NEWS VERSION *.pdf
%dir %{_includedir}/%{name}
%{_libdir}/*.so
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/%{name}.pc
