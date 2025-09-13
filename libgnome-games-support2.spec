%define major		4
%define api		2
%define libname		%mklibname gnome-games-support2
%define develname	%mklibname gnome-games-support2 -d

%define url_ver	%(echo %{version}|cut -d. -f1,2)

%global optflags %{optflags} -Wno-error -Wno-implicit-function-declaration
%global optflags %{optflags} -Wno-incompatible-function-pointer-types

%define oname libgnome-games-support

Name:		libgnome-games-support2
Version:	2.0.2
Release:	1
Summary:	Support library for GNOME games
Group:		Development/GNOME and GTK+
License:	LGPLv3+
URL:		https://git.gnome.org/browse/%{name}/
Source0:	https://download.gnome.org/sources/%{oname}/%{url_ver}/%{oname}-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0) >= 2.40
BuildRequires:	pkgconfig(gio-2.0) >= 2.40
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:	intltool
BuildRequires:  meson

%description
libgnome-games-support is a small library intended for internal use by GNOME Games,
but it may be used by others. The API will only break with the major version
number. The ABI is unstable.

#------------------------------------

%package	i18n
Summary:	Support library for GNOME games - translations
Group:		System/Internationalization
BuildArch:	noarch

%description	i18n
libgnome-games-support is a small library intended for internal use by GNOME Games,
but it may be used by others. The API will only break with the major version
number. The ABI is unstable.

This package contains translations used by %{name}.

#------------------------------------

%package -n	%{libname}
Summary:	Library for %{name}
Group:		System/Libraries
Requires:	%{name}-i18n = %{version}-%{release}


%description -n %{libname}
libgnome-games-support is a small library intended for internal use by GNOME Games,
but it may be used by others. The API will only break with the major version
number. The ABI is unstable.

#------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
The %{develname} package contains libraries and header files for
developing applications that use %{name}.

#------------------------------------

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -delete

%find_lang %{name}

%files i18n -f %{name}.lang

%files -n %{libname}
%doc README
%license COPYING.LESSER
%{_libdir}/%{oname}-%{api}.so.%{major}{,.*}

%files -n %{develname}
%doc README
%license COPYING.LESSER
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi
%{_includedir}/gnome-games-support-%{api}/
%{_libdir}/%{oname}-%{api}.so
%{_libdir}//pkgconfig/libgnome-games-support-2.pc
