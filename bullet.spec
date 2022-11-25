%define major 3.17
#define	_disable_lto %{nil}
#define _disable_ld_no_undefined 1

Summary:	Professional 3D collision detection library
Name:		bullet
Version:	3.24
Release:	2
License:	Zlib
Group:		System/Libraries
URL:		http://www.bulletphysics.com
Source0:	https://github.com/bulletphysics/bullet3/archive/%{version}/%{name}3-%{version}.tar.gz
#Patch0:		do-not-build-with-embedded-tinyxml-library.patch
# https://github.com/bulletphysics/bullet3/issues/626
Patch0:         bullet-2.89-fix-bullet.pc.patch
# https://github.com/bulletphysics/bullet3/issues/1489
#Patch1:         bullet-2.87-disable-underlinked-bulletrobotics.patch
Patch2:         use-system-libs.patch

BuildRequires:	cmake
BuildRequires:	libtool
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	perl-Template-Toolkit
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
BuildRequires:  pkgconfig(freeglut)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(tinyxml2)

%description
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


#----------------------------------------------------------------------------
%define libname %mklibname %{name} %{major}

%package -n %{libname}
Summary:        Professional 3D collision detection library
Group:          System/Libraries
Provides:       %{_lib}bullet2 = %{version}-%{release}

%description -n %{libname}
Bullet is a professional open source multi-threaded
3D Collision Detection and Rigid Body Dynamics Library
for games and animation.

%files -n %{libname}
%{_libdir}/lib*.so.%{version}

#----------------------------------------------------------------------------
%define devname %mklibname %{name} -d

%package -n %{devname}
Summary:	Development headers for Bullet
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	pkgconfig(libxml-2.0)

%description -n %{devname}
Development headers for Bullet, a 3D collision library.

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/cmake/%{name}
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}3-%{version}
%autopatch -p1
rm -rf build3/*.{bat,exe}
rm -rf build3/xcode*
rm -rf build3/*osx*
rm -rf build3/premake*
rm -rf data
rm -rf examples/

# Set these files to right permission
#chmod 644 src/LinearMath/btPoolAllocator.h
#chmod 644 src/BulletDynamics/ConstraintSolver/btSliderConstraint.cpp
#chmod 644 src/BulletDynamics/ConstraintSolver/btSliderConstraint.h
sed -i 's|-I@CMAKE_INSTALL_PREFIX@/@INCLUDE_INSTALL_DIR@|-I@INCLUDE_INSTALL_DIR@|' bullet.pc.cmake

sed -i 's|BulletRobotics||' Extras/CMakeLists.txt
sed -i 's|obj2sdf||' Extras/CMakeLists.txt

%build
%cmake \
    -DBUILD_BULLET2_DEMOS=OFF \
    -DBUILD_CPU_DEMOS=OFF \
    -DBUILD_EXTRAS=OFF \
    -DBUILD_OPENGL3_DEMOS=OFF \
    -DBUILD_UNIT_TESTS=OFF \
    -DINSTALL_EXTRA_LIBS=ON \
    -DOpenGL_GL_PREFERENCE=GLVND \
    -DBUILD_EXTRAS=ON \
    -DBUILD_INVERSE_DYNAMIC_EXTRA=OFF \
    -DBUILD_BULLET_ROBOTICS_GUI_EXTRA=OFF \
    -DBUILD_BULLET_ROBOTICS_EXTRA=OFF \
    -DBUILD_OBJ2SDF_EXTRA=OFF \
    -DBUILD_SERIALIZE_EXTRA=ON \
    -DBUILD_CONVEX_DECOMPOSITION_EXTRA=OFF \
    -DBUILD_HACD_EXTRA=OFF \
    -DBUILD_GIMPACTUTILS_EXTRA=OFF \
    -DINCLUDE_INSTALL_DIR=%{_includedir}/%{name}
%make_build

%install
%make_install -C build

# install libs from Extras
pushd Extras
find . -name '*.so*' -exec cp -a {} %{buildroot}%{_libdir} \;
popd
