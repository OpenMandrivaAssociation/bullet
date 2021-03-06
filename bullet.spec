%define major 2.89
#define	_disable_lto %{nil}
#define _disable_ld_no_undefined 1

Summary:	Professional 3D collision detection library
Name:		bullet
Version:	2.89
Release:	1
License:	Zlib
Group:		System/Libraries
URL:		http://www.bulletphysics.com
Source0:	https://github.com/bulletphysics/bullet3/archive/%{version}/%{name}3-%{version}.tar.gz
#Patch0:		do-not-build-with-embedded-tinyxml-library.patch
# https://github.com/bulletphysics/bullet3/issues/626
Patch0:         bullet-2.89-fix-bullet.pc.patch
# https://github.com/bulletphysics/bullet3/issues/1489
Patch1:         bullet-2.87-disable-underlinked-bulletrobotics.patch
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
%define libBulletCommon %mklibname BulletCommon %{major}

%package -n %{libBulletCommon}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4
Obsoletes:	%{_lib}bullet2 < 2.80-4

%description -n %{libBulletCommon}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libBulletCommon}
%{_libdir}/libBullet3Common.so.%{major}

#----------------------------------------------------------------------------

%define libBulletCollision %mklibname BulletCollision %{major}

%package -n %{libBulletCollision}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4
Obsoletes:	%{_lib}bullet2 < 2.80-4

%description -n %{libBulletCollision}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libBulletCollision}
%{_libdir}/libBulletCollision.so.%{major}
%{_libdir}/libBullet3Collision.so.%{major}

#----------------------------------------------------------------------------

%define libBulletDynamics %mklibname BulletDynamics %{major}

%package -n %{libBulletDynamics}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4

%description -n %{libBulletDynamics}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libBulletDynamics}
%{_libdir}/libBulletDynamics.so.%{major}
%{_libdir}/libBullet3Dynamics.so.%{major}

#----------------------------------------------------------------------------

%define libBulletFileLoader %mklibname BulletFileLoader %{major}

%package -n %{libBulletFileLoader}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4

%description -n %{libBulletFileLoader}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libBulletFileLoader}
%{_libdir}/libBulletFileLoader.so.%{major}
%{_libdir}/libBullet2FileLoader.so.%{major}

#----------------------------------------------------------------------------

%define libBulletSoftBody %mklibname BulletSoftBody %{major}

%package -n %{libBulletSoftBody}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4

%description -n %{libBulletSoftBody}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libBulletSoftBody}
%{_libdir}/libBulletSoftBody.so.%{major}

#----------------------------------------------------------------------------

%define libBulletWorldImporter %mklibname BulletWorldImporter %{major}

%package -n %{libBulletWorldImporter}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4

%description -n %{libBulletWorldImporter}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libBulletWorldImporter}
%{_libdir}/libBulletWorldImporter.so.%{major}

#----------------------------------------------------------------------------

%define libConvexDecomposition %mklibname ConvexDecomposition %{major}

%package -n %{libConvexDecomposition}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4

%description -n %{libConvexDecomposition}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libConvexDecomposition}
%{_libdir}/libConvexDecomposition.so.%{major}

#----------------------------------------------------------------------------

%define libGeometry %mklibname Geometry %{major}

%package -n %{libGeometry}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4

%description -n %{libGeometry}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libGeometry}
%{_libdir}/libBullet3Geometry.so.%{major}

#----------------------------------------------------------------------------

%define libGIMPACTUtils %mklibname GIMPACTUtils %{major}

%package -n %{libGIMPACTUtils}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4

%description -n %{libGIMPACTUtils}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libGIMPACTUtils}
%{_libdir}/libGIMPACTUtils.so.%{major}

#----------------------------------------------------------------------------

%define libOpenCL %mklibname OpenCL %{major}

%package -n %{libOpenCL}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4

%description -n %{libOpenCL}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libOpenCL}
%{_libdir}/libBullet3OpenCL_clew.so.%{major}


#----------------------------------------------------------------------------

%define libInverseDynamics %mklibname InverseDynamics %{major}

%package -n %{libInverseDynamics}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4

%description -n %{libInverseDynamics}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libInverseDynamics}
%{_libdir}/libBulletInverseDynamics.so.%{major}

#----------------------------------------------------------------------------

%define libInverseDynamicsUtils %mklibname InverseDynamicsUtils %{major}

%package -n %{libInverseDynamicsUtils}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4

%description -n %{libInverseDynamicsUtils}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libInverseDynamicsUtils}
%{_libdir}/libBulletInverseDynamicsUtils.so.%{major}

#----------------------------------------------------------------------------

%define libHACD %mklibname HACD %{major}

%package -n %{libHACD}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4

%description -n %{libHACD}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libHACD}
%{_libdir}/libHACD.so.%{major}

#----------------------------------------------------------------------------

%define libLinearMath %mklibname LinearMath %{major}

%package -n %{libLinearMath}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4

%description -n %{libLinearMath}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libLinearMath}
%{_libdir}/libLinearMath.so.%{major}

#----------------------------------------------------------------------------
%define libBulletXmlWorldImporter %mklibname BulletXmlWorldImporter %{major}

%package -n %{libBulletXmlWorldImporter}
Summary:	Professional 3D game multiphysics library
Group:		System/Libraries
Conflicts:	%{_lib}bullet2 < 2.80-4

%description -n %{libBulletXmlWorldImporter}
Bullet is a professional open source multi-threaded 3D Collision Detection
and Rigid Body Dynamics Library for games and animation.

This package provides one of Bullet shared libraries.

%files -n %{libBulletXmlWorldImporter}
%{_libdir}/libBulletXmlWorldImporter.so.%{major}

%define devname %mklibname %{name} -d

%package -n %{devname}
Summary:	Development headers for Bullet
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libBulletCollision} = %{EVRD}
Requires:	%{libBulletCommon} = %{EVRD}
Requires:	%{libGeometry} = %{EVRD}
Requires:	%{libOpenCL} = %{EVRD}
Requires:	%{libInverseDynamics} = %{EVRD}
Requires:	%{libInverseDynamicsUtils} = %{EVRD}
Requires:	%{libBulletDynamics} = %{EVRD}
Requires:	%{libBulletFileLoader} = %{EVRD}
Requires:	%{libBulletSoftBody} = %{EVRD}
Requires:	%{libBulletWorldImporter} = %{EVRD}
Requires:	%{libBulletXmlWorldImporter} = %{EVRD}
Requires:	%{libConvexDecomposition} = %{EVRD}
Requires:	%{libGIMPACTUtils} = %{EVRD}
Requires:	%{libHACD} = %{EVRD}
Requires:	%{libLinearMath} = %{EVRD}
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
    -DBUILD_EXTRAS=ON \
    -DBUILD_OPENGL3_DEMOS=OFF \
    -DBUILD_UNIT_TESTS=OFF \
    -DINSTALL_EXTRA_LIBS=ON \
    -DINCLUDE_INSTALL_DIR=%{_includedir}/%{name}
%make_build

%install
%make_install -C build

# install libs from Extras
pushd Extras
find . -name '*.so*' -exec cp -a {} %{buildroot}%{_libdir} \;
popd
