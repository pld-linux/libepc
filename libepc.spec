Summary:	Easy Publish and Consume library
Name:		libepc
Version:	0.4.0
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libepc/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	c7fde118546d09d747af7b08cb52bfad
URL:		http://live.gnome.org/libepc
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10.3
BuildRequires:	avahi-glib-devel
BuildRequires:	avahi-ui-gtk3-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnutls-devel
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	intltool >= 0.36.0
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libuuid-devel >= 1.36
BuildRequires:	pkgconfig >= 1:0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Easy Publish and Consume library provides an easy method to:
- publish data using HTTPS
- announce that information via DNS-SD
- find that information
- and finally consume it

This library can be used as key/value store published to the network,
using encryption, authentication and service discovery.

%package devel
Summary:	Header files for libepc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libepc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	avahi-glib-devel
Requires:	libsoup-devel >= 2.4.0

%description devel
Header files for libepc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libepc.

%package static
Summary:	Static libepc library
Summary(pl.UTF-8):	Statyczna biblioteka libepc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libepc library.

%description static -l pl.UTF-8
Statyczna biblioteka libepc.

%package ui
Summary:	Widgets for libepc
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description ui
Widgets for use with libepc.

%package ui-devel
Summary:	Header files for libepc-ui library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libepc-ui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ui = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.12.8

%description ui-devel
Header files for libepc-ui library.

%description ui-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libepc-ui.

%package ui-static
Summary:	Static libepc-ui library
Summary(pl.UTF-8):	Statyczna biblioteka libepc-ui
Group:		X11/Development/Libraries
Requires:	%{name}-ui-devel = %{version}-%{release}

%description ui-static
Static libepc-ui library.

%description ui-static -l pl.UTF-8
Statyczna biblioteka libepc-ui.

%package apidocs
Summary:	libepc library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libepc
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libepc library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libepc.

%package examples
Summary:	libepc - example programs
Summary(pl.UTF-8):	libepc - przykładowe programy
License:	Public Domain
Group:		Development/Libraries

%description examples
libepc - example programs.

%description examples -l pl.UTF-8
libepc - przykładowe programy.

%prep
%setup -q

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libepc-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libepc-1.0.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepc-1.0.so
%{_includedir}/libepc-1.0
%{_pkgconfigdir}/libepc-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libepc-1.0.a

%files ui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepc-ui-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libepc-ui-1.0.so.3

%files ui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libepc-ui-1.0.so
%{_includedir}/libepc-ui-1.0
%{_pkgconfigdir}/libepc-ui-1.0.pc

%files ui-static
%defattr(644,root,root,755)
%{_libdir}/libepc-ui-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libepc-1.0

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
