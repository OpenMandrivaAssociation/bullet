Summary:	Professional 3D collision detection library
Name:		bullet
Version:	2.53
Release:	%mkrel 1
License:	ZLIB
Group:		System/Libraries
Url:		http://www.continuousphysics.com/Bullet/index.html
Source0:	http://downloads.sourceforge.net/bullet/%{name}-%{version}.tar.bz2
#BuildRequires:
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Bullet is a professional open source multi-threaded 
3D Collision Detection and Rigid Body Dynamics Library
for games and animation.

%prep
%setup -q

%build
%configure2_5x \
	--with-x \
	--with-mesa

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%post
%{update_menus}
%if %mdkversion >= 200700
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%postun
%{clean_menus}
%if %mdkversion >= 200700
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc
%attr(755,root,root)
