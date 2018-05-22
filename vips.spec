# TODO:
# - split -libs (-n libvips)
# - python package (-n python-vipsCC)
# - gir stuff belongs to what package?
Summary:	A fast image processing library with low memory needs
Summary(pl.UTF-8):	Biblioteka przetwarzania obrazów
Name:		vips
Version:	8.5.9
Release:	3
License:	LGPL
Group:		Libraries
Source0:	https://github.com/jcupitt/libvips/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b8639ec0b05dfa17deca50007895963a
URL:		http://jcupitt.github.io/libvips/
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
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.32
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libvips is a demand-driven, horizontally threaded image processing
library. Compared to similar libraries, libvips runs quickly and uses
little memory.

It has around 300 operations covering arithmetic, histograms,
convolution, morphological operations, frequency filtering, colour,
resampling, statistics and others. It supports a large range of
numeric formats, from 8-bit int to 128-bit complex. Images can have
any number of bands. It supports a good range of image formats,
including JPEG, TIFF, OME-TIFF, PNG, WebP, FITS, Matlab, OpenEXR, PDF,
SVG, HDR, PPM, CSV, GIF, Analyze, DeepZoom, and OpenSlide. It can also
load images via ImageMagick or GraphicsMagick, letting it load formats
like DICOM.

%description -l pl.UTF-8
VIPS jest biblioteką przetwarzania obrazów. Jest dobra dla bardzo
dużych obrazów (to znaczy większych niż ilość RAM w komputerze), oraz
do pracy z kolorami. Zawiera API w C++, kompletne strony pomocy man,
interfejs linii poleceń, automatyczne wątkowanie i bazę danych
operacji. Jest kilka interfejsów użytkownika zbudowanych na podstawie
VIPS, na przykład "nip".

%package devel
Summary:	Header files for vips library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki vips
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for vips library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki vips.

%package static
Summary:	Static vips library
Summary(pl.UTF-8):	Statyczna biblioteka vips
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvips-cpp.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvips.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvipsCC.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/vipsCC/*.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/vipsCC/*.a

rm -r $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/libvips

%py_postclean

%find_lang vips8.5 -o %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS THANKS TODO
%attr(755,root,root) %{_bindir}/batch_crop
%attr(755,root,root) %{_bindir}/batch_image_convert
%attr(755,root,root) %{_bindir}/batch_rubber_sheet
%attr(755,root,root) %{_bindir}/light_correct
%attr(755,root,root) %{_bindir}/shrink_width
%attr(755,root,root) %{_bindir}/vips
%attr(755,root,root) %{_bindir}/vips-8.5
%attr(755,root,root) %{_bindir}/vipsedit
%attr(755,root,root) %{_bindir}/vipsheader
%attr(755,root,root) %{_bindir}/vipsprofile
%attr(755,root,root) %{_bindir}/vipsthumbnail
%attr(755,root,root) %{_libdir}/libvips-cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvips-cpp.so.42
%attr(755,root,root) %{_libdir}/libvips.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvips.so.42
%attr(755,root,root) %{_libdir}/libvipsCC.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvipsCC.so.42
%{_libdir}/girepository-1.0/Vips-8.0.typelib
%{_datadir}/gir-1.0/Vips-8.0.gir
%{_mandir}/man1/batch_crop.1*
%{_mandir}/man1/batch_image_convert.1*
%{_mandir}/man1/batch_rubber_sheet.1*
%{_mandir}/man1/light_correct.1*
%{_mandir}/man1/vips.1*
%{_mandir}/man1/vipsedit.1*
%{_mandir}/man1/vipsheader.1*
%{_mandir}/man1/vipsprofile.1*
%{_mandir}/man1/vipsthumbnail.1*

%dir %{py_sitedir}/vipsCC
%{py_sitedir}/vipsCC/*.py[co]
%attr(755,root,root) %{py_sitedir}/vipsCC/vdisplaymodule.so
%attr(755,root,root) %{py_sitedir}/vipsCC/verrormodule.so
%attr(755,root,root) %{py_sitedir}/vipsCC/vimagemodule.so
%attr(755,root,root) %{py_sitedir}/vipsCC/vmaskmodule.so
%{py_sitedir}/gi/overrides/Vips.py[co]

%files devel
%defattr(644,root,root,755)
%{_libdir}/libvips-cpp.so
%{_libdir}/libvips.so
%{_libdir}/libvipsCC.so
%{_includedir}/vips
%{_pkgconfigdir}/vips-cpp.pc
%{_pkgconfigdir}/vips.pc
%{_pkgconfigdir}/vipsCC.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvips-cpp.a
%{_libdir}/libvips.a
%{_libdir}/libvipsCC.a
