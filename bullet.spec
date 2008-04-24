%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -d -s

Summary:	Professional 3D collision detection library
Name:		bullet
Version:	2.68
Release:	%mkrel 1
License:	Zlib
Group:		System/Libraries
Url:		http://www.continuousphysics.com/Bullet/index.html
Source0:	http://bullet.googlecode.com/files/bullet-%{version}.tgz
Patch1:		%{name}-2.67-shared-libraries.patch
Patch2:		%{name}-2.67-x86_64-fixes.patch
Patch3:		%{name}-2.68-use-system-libxml2.patch
BuildRequires:	doxygen
BuildRequires:	mesa-common-devel
BuildRequires:	ftjam
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
Bullet is a professional open source multi-threaded 
3D Collision Detection and Rigid Body Dynamics Library
for games and animation.

%package -n %{develname}
Summary:	Development headers for bullet
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	libxml2-devel

%description -n %{develname}
Development headers for bullet 3D collision library.

%package -n %{staticname}
Summary:	Static libraries for %{name}
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Provides:	lib%{name}-static-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n %{staticname}
Static libraries for %{name}.

%prep
%setup -q
%patch1 -p1
%patch3 -p1

%ifnarch ix86
%patch2 -p1
%endif

chmod +x configure

pushd mk/autoconf
chmod +x *
popd

# get rid of no newline ... warnings
echo "" >> src/BulletCollision/BroadphaseCollision/btOverlappingPairCallback.h
echo "" >> src/BulletCollision/NarrowPhaseCollision/btRaycastCallback.cpp
echo "" >> src/BulletSoftBody/btSoftBodyRigidBodyCollisionConfiguration.cpp
echo "" >> src/BulletCollision/CollisionShapes/btTriangleMesh.cpp
echo "" >> src/LinearMath/btHashMap.h
echo "" >> Extras/BulletColladaConverter/ColladaConverter.cpp
echo "" >> Demos/AllBulletDemos/../DynamicControlDemo/MotorDemo.cpp
echo "" >> src/LinearMath/btHashMap.h
echo "" >> Demos/Benchmarks/main.cpp
echo "" >> src/LinearMath/btHashMap.h
echo "" >> Demos/BasicDemo/main.cpp
echo "" >> src/LinearMath/btHashMap.h


#(tpg) use system libxml2
rm -rf Extras/LibXML

%build
#(tpg) export USE_ADDR64 only for x86_64, otherwise build fails, use system libxml2
%ifnarch ix86
export CFLAGS="%{optflags} -fno-strict-aliasing -DUSE_ADDR64 -I%{_includedir} -I%{_includedir}/libxml2"
%else
export CFLAGS="%{optflags} -fno-strict-aliasing -I%{_includedir} -I%{_includedir}/libxml2"
%endif
export CXXFLAGS=$CFLAGS
export LDFLAGS="%{optflags} -lxml2"

./autogen.sh

%configure2_5x \
	--with-mesa

# parallel build of demos is broken ...
# ... so build first library
sed -i -e 's|SubInclude TOP Demos ;|#SubInclude TOP Demos ;|g' Jamfile
jam -d2 %{_smp_mflags}

# ... and then demos
sed -i -e 's|#SubInclude TOP Demos ;|SubInclude TOP Demos ;|g' Jamfile
jam -d2

#(tpg) build shared libraries
pushd lib
sed -i -e 's/sover/%{version}/g' Makefile
%make
popd

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

jam -d2 install DESTDIR=%{buildroot} 

install -dm 755 %{buildroot}%{_bindir}

demos=`ls -1 *Demo`
for i in $demos AllBulletDemos ContinuousConvexCollision BulletDino Raytracer UserCollisionAlgorithm; do
    install -m 755 $i %{buildroot}%{_bindir}/bullet-$i
done

#(tpg) install shared libraries
cp -f lib/*.so* %{buildroot}%{_libdir}

#(tpg) add symlinks
pushd %{buildroot}%{_libdir}
for i in libbulletcollision libbulletdynamics libbulletmath; do
ln -s $i.so.%{major}* $i.so
done
popd

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files demo
%defattr(-,root,root)
%{_bindir}/%{name}-*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libbulletcollision.a
%{_libdir}/libbulletdynamics.a
%{_libdir}/libbulletmath.a
%{_libdir}/libbulletsoftbody.a
	 
%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS README LICENSE ChangeLog.txt NEWS VERSION *.pdf
%dir %{_includedir}/%{name}
%{_libdir}/*.so
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/%{name}.pc
