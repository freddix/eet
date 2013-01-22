Summary:	Enlightenment Foundation Library
Name:		eet
Version:	1.7.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	4a7b4ec5473570cec8cd3b81ce1a68f1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	eina-devel
BuildRequires:	gnutls-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a tiny library designed to write an arbitrary set of chunks of
data to a file and optionally compress each chunk (very much like
a zip file) and allow fast random-access reading of the file later on.
It does not do zip as a zip itself has more complexity than is needed,
and it was much simpler to implement this once here.

%package devel
Summary:	Header files for eet library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for eet library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-install-examples	\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/eet
%attr(755,root,root) %ghost %{_libdir}/libeet.so.1
%attr(755,root,root) %{_libdir}/libeet.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeet.so
%{_includedir}/eet-1
%{_pkgconfigdir}/eet.pc

