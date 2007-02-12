Summary:	An image processing library
Summary(pl.UTF-8):   Biblioteka przetwarzania obrazów
Name:		vips
Version:	7.10.10
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://www.vips.ecs.soton.ac.uk/%{name}-7.10/%{name}-%{version}.tar.gz
# Source0-md5:	5fa724406ff4e9ca9839d5f51bd391ad
URL:		http://www.vips.ecs.soton.ac.uk/
BuildRequires:	ImageMagick-devel >= 1:6.2.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	fftw3-devel >= 3.0.0
BuildRequires:	glib2-devel >= 2.4.0
BuildRequires:	imlib-devel
BuildRequires:	intltool
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VIPS is an image processing library. It is good for very large images
(ie. larger than the amount of RAM in your machine), and for working
with colour. It includes a C++ API, complete man pages, a command-line
interface, automatic threading and an operation database. There are
several user interfaces built on top of VIPS: for example "nip".

%description -l pl.UTF-8
VIPS jest biblioteką przetwarzania obrazów. Jest dobra dla bardzo
dużych obrazów (to znaczy większych niż ilość RAM w komputerze), oraz
do pracy z kolorami. Zawiera API w C++, kompletne strony pomocy man,
interfejs linii poleceń, automatyczne wątkowanie i bazę danych
operacji. Jest kilka interfejsów użytkownika zbudowanych na podstawie
VIPS, na przykład "nip".

%package devel
Summary:	Header files for vips library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki vips
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for vips library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki vips.

%package static
Summary:	Static vips library
Summary(pl.UTF-8):   Statyczna biblioteka vips
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static vips library.

%description static -l pl.UTF-8
Statyczna biblioteka vips.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc doc/html/refguide doc/html/appguide
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc doc/html/cppguide doc/html/libguide
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
