%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -d -s

Summary:	Professional 3D collision detection library
Name:		bullet
Version:	2.63
Release:	%mkrel 1
License:	Zlib
Group:		System/Libraries
Url:		http://www.continuousphysics.com/Bullet/index.html
Source0:	http://downloads.sourceforge.net/bullet/%{name}-%{version}.tar.bz2
BuildRequires:	doxygen
BuildRequires:	mesa-common-devel
BuildRequires:	ftjam
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Bullet is a professional open source multi-threaded 
3D Collision Detection and Rigid Body Dynamics Library
for games and animation.

%package -n %{staticname}
Summary:	Professional 3D collision detection library
Group:		Development/C

%description -n %{staticname}
Bullet is a professional open source multi-threaded 
3D Collision Detection and Rigid Body Dynamics Library
for games and animation.

%package -n %{develname}
Summary:	Development headers for bullet
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{staticname} = %{version}-%{release}

%description -n %{develname}
Development headers for bullet.

%prep
%setup -q

%ifarch x86_64
sed -i -e 's|(unsigned)|(unsigned long)|g' src/BulletCollision/CollisionShapes/btOptimizedBvh.cpp
%endif

%build
%configure2_5x \
	--with-mesa

jam -d2

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

DESTDIR=%{buildroot} jam -d2 install

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libbulletcollision.a
%{_libdir}/libbulletdynamics.a
%{_libdir}/libbulletmath.a
	 
%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS README LICENSE ChangeLog.txt NEWS VERSION *.pdf
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/%{name}.pc
