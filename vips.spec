Summary:	An image processing library
Summary(pl):	Biblioteka przetwarzania obrazów
Name:		vips
Version:	7.10.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.vips.ecs.soton.ac.uk/%{name}-7.10/%{name}-%{version}.tar.gz
# Source0-md5:	6c0bd95710096686b57878167c483298
URL:		http://www.vips.ecs.soton.ac.uk/
BuildRequires:	ImageMagick-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	expat-devel
BuildRequires:	fftw3-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	glib2-devel
BuildRequires:	imlib-devel
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pango-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VIPS is an image processing library. It is good for very large images
(ie. larger than the amount of RAM in your machine), and for working
with colour. It includes a C++ API, complete man pages, a command-line
interface, automatic threading and an operation database. There are
several user interfaces built on top of VIPS: for example "nip".

%description -l pl
VIPS jest bibliotek± przetwarzania obrazów. Jest dobra dla bardzo
du¿ych obrazów(to znaczy wiêkszych ni¿ ilo¶æ RAM w komputerze), oraz
do pracy z kolorami. Zawiera API w C++, kompletne strony pomocy man,
interfejs lini poleceñ, automatyczne w±tkowanie i bazê danych
operacji. Jest kilka interfejsów u¿ytkownika zbudowanych na podstawie
VIPS, na przyk³ad "nip".

%package devel
Summary:	Header files for vips library
Summary(pl):	Pliki nag³ówkowe biblioteki vips
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for vips library.

%description devel -l pl
Pliki nag³ówkowe biblioteki vips.

%package static
Summary:	Static vips library
Summary(pl):	Statyczna biblioteka vips
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static vips library.

%description static -l pl
Statyczna biblioteka vips.

%prep
%setup -q

%build
# if ac/am/lt/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/lib*.so
%doc doc/html/cppguide doc/html/libguide
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
