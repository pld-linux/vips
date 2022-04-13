# TODO:
# - pdfium as an alternative for poppler?
#
# Conditional build:
%bcond_with	libspng		# libspng for reading instead of libpng

Summary:	A fast image processing library with low memory needs
Summary(pl.UTF-8):	Szybka, mająca małe wymagania pamięciowe biblioteka przetwarzania obrazów
Name:		vips
Version:	8.11.2
Release:	3
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/jcupitt/libvips/tags
Source0:	https://github.com/jcupitt/libvips/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	79ceea4d685b1b9dc3cb1e253c81793c
URL:		http://jcupitt.github.io/libvips/
BuildRequires:	ImageMagick-devel >= 1:7.0
BuildRequires:	OpenEXR-devel >= 1.2.2
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1.6
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel >= 1.2
BuildRequires:	cfitsio-devel
BuildRequires:	expat-devel >= 1.95
BuildRequires:	fftw3-devel >= 3.0.0
BuildRequires:	fontconfig-devel
BuildRequires:	gettext-tools
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 1:2.62
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libexif-devel >= 0.6
BuildRequires:	libgsf-devel >= 1.14.31
BuildRequires:	libheif-devel >= 1.7.0
BuildRequires:	libimagequant-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libjxl-devel >= 0.3.7
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel >= 2:1.2.9
BuildRequires:	librsvg-devel >= 2.40.3
%{?with_libspng:BuildRequires:	libspng >= 0.6}
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libtool
BuildRequires:	libwebp-devel >= 0.6
BuildRequires:	libxml2-devel
BuildRequires:	matio-devel
BuildRequires:	nifticlib-devel
BuildRequires:	openjpeg2-devel >= 2.4
BuildRequires:	openslide-devel >= 3.4.0
BuildRequires:	orc-devel >= 0.4.31
BuildRequires:	pango-devel >= 1:1.8
BuildRequires:	poppler-glib-devel >= 0.16.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(find_lang) >= 1.32
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	zlib-devel >= 0.4
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

This package contains utilities based on libvips library.

%description -l pl.UTF-8
VIPS jest wielowątkową biblioteką przetwarzania obrazów. W porównaniu
do innych, działa szybko i zużywa niewiele pamięci.

Ma około 300 operacji obejmujących arytmetykę, histogramy, sploty,
operacje morfologiczne, filtry częstotliwościowe, kolory, resampling,
statystyki i inne. Obsługuje wiele formatów liczbowych, od 8-bitowych
do zespolonych 128-bitowych. Obrazy mogą mieć dowolną liczbę zakresów.
Obsługiwane jest szeroki zakres formatów, w tym JPEG, TIFF, OME-TIFF,
PNG, WebP, FITS, Matlab, OpenEXR, PDF, SVG, HDR, PPM, CSV, GIF,
Analyze, DeepZoom i OpenSlide. Biblioteka potrafi także wczytywać
obrazy poprzez ImageMagick lub GraphicsMagick, dzięki czemu obsługuje
formaty takie jak DICOM.

Ten pakiet zawiera narzędzia oparte na bibliotece libvips.

%package -n libvips
Summary:	VIPS image processing library
Summary(pl.UTF-8):	Biblioteka przetwarzania obrazów VIPS
Group:		Libraries
Requires:	ImageMagick-libs >= 1:7.0
Requires:	OpenEXR >= 1.2.2
Requires:	cairo >= 1.2
Requires:	glib2 >= 1:2.62
Requires:	libexif >= 0.6
Requires:	libgsf >= 1.14.31
Requires:	libheif >= 1.7.0
Requires:	libjxl >= 0.3.7
Requires:	libpng >= 2:1.2.9
Requires:	librsvg >= 2.40.3
%{?with_libspng:Requires:	libspng >= 0.6}
Requires:	libtiff >= 4
Requires:	libwebp >= 0.6
Requires:	openjpeg2 >= 2.4
Requires:	openslide >= 3.4.0
Requires:	orc >= 0.4.31
Requires:	poppler-glib >= 0.16.0
Requires:	zlib >= 0.4

%description -n libvips
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

%description -n libvips -l pl.UTF-8
VIPS jest wielowątkową biblioteką przetwarzania obrazów. W porównaniu
do innych, działa szybko i zużywa niewiele pamięci.

Ma około 300 operacji obejmujących arytmetykę, histogramy, sploty,
operacje morfologiczne, filtry częstotliwościowe, kolory, resampling,
statystyki i inne. Obsługuje wiele formatów liczbowych, od 8-bitowych
do zespolonych 128-bitowych. Obrazy mogą mieć dowolną liczbę zakresów.
Obsługiwane jest szeroki zakres formatów, w tym JPEG, TIFF, OME-TIFF,
PNG, WebP, FITS, Matlab, OpenEXR, PDF, SVG, HDR, PPM, CSV, GIF,
Analyze, DeepZoom i OpenSlide. Biblioteka potrafi także wczytywać
obrazy poprzez ImageMagick lub GraphicsMagick, dzięki czemu obsługuje
formaty takie jak DICOM.

%package -n libvips-devel
Summary:	Header files for VIPS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki VIPS
Group:		Development/Libraries
Requires:	ImageMagick-devel >= 1:7.0
Requires:	OpenEXR-devel >= 1.2.2
Requires:	cairo-devel >= 1.2
Requires:	cfitsio-devel
Requires:	expat-devel >= 1.95
Requires:	fftw3-devel >= 3.0.0
Requires:	fontconfig-devel
Requires:	glib2-devel >= 1:2.62
Requires:	lcms2-devel >= 2
Requires:	libexif-devel >= 0.6
Requires:	libgsf-devel >= 1.14.31
Requires:	libheif-devel >= 1.7.0
Requires:	libimagequant-devel
Requires:	libjpeg-devel
Requires:	libjxl-devel >= 0.3.7
Requires:	libpng-devel >= 2:1.2.9
Requires:	librsvg-devel >= 2.40.3
%{?with_libspng:Requires:	libspng-devel >= 0.6}
Requires:	libtiff-devel >= 4
Requires:	libwebp-devel >= 0.6
Requires:	matio-devel
Requires:	openjpeg2-devel >= 2.4
Requires:	openslide-devel >= 3.4.0
Requires:	orc-devel >= 0.4.31
Requires:	pango-devel >= 1:1.8
Requires:	poppler-glib-devel >= 0.16.0
Requires:	zlib-devel >= 0.4
Obsoletes:	vips-devel < 8.7

%description -n libvips-devel
Header files for VIPS library.

%description -n libvips-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki VIPS.

%package -n libvips-static
Summary:	Static VIPS library
Summary(pl.UTF-8):	Statyczna biblioteka VIPS
Group:		Development/Libraries
Obsoletes:	vips-static < 8.7

%description -n libvips-static
Static VIPS library.

%description -n libvips-static -l pl.UTF-8
Statyczna biblioteka VIPS.

%package -n libvips-apidocs
Summary:	API documentation for VIPS library
Summary(pl.UTF-8):	Dokumentacja API biblioteki VIPS
Group:		Documentation
BuildArch:	noarch

%description -n libvips-apidocs
API documentation for VIPS library, together with some general VIPS
documentation.

%description -n libvips-apidocs -l pl.UTF-8
Dokumentacja API biblioteki VIPS. Zawiera także trochę ogólnej
dokumentacji projektu VIPS.

%package -n libvips-cpp8
Summary:	C++ API for VIPS 8 image processing library
Summary(pl.UTF-8):	API C++ do biblioteki przetwarzania obrazów VIPS 8
Group:		Libraries
Requires:	libvips = %{version}-%{release}

%description -n libvips-cpp8
C++ API for VIPS 8 image processing library.

%description -n libvips-cpp8 -l pl.UTF-8
API C++ do biblioteki przetwarzania obrazów VIPS 8.

%package -n libvips-cpp8-devel
Summary:	C++ API for VIPS 8 image processing library - header files
Summary(pl.UTF-8):	API C++ do biblioteki przetwarzania obrazów VIPS 8 - pliki nagłówkowe
Group:		Development/Libraries
Requires:	libvips-cpp8 = %{version}-%{release}
Requires:	libvips-devel = %{version}-%{release}

%description -n libvips-cpp8-devel
C++ API for VIPS 8 image processing library - header files.

%description -n libvips-cpp8-devel -l pl.UTF-8
API C++ do biblioteki przetwarzania obrazów VIPS 8 - pliki nagłówkowe.

%package -n libvips-cpp8-static
Summary:	C++ API for VIPS 8 image processing library - static library
Summary(pl.UTF-8):	API C++ do biblioteki przetwarzania obrazów VIPS 8 - biblioteka statyczna
Group:		Development/Libraries
Requires:	libvips-cpp8-devel = %{version}-%{release}

%description -n libvips-cpp8-static
C++ API for VIPS 8 image processing library - static library.

%description -n libvips-cpp8-static -l pl.UTF-8
API C++ do biblioteki przetwarzania obrazów VIPS 8 - biblioteka
statyczna.

%package -n libvips-cpp8-apidocs
Summary:	C++ API documentation for VIPS 8 library
Summary(pl.UTF-8):	Dokumentacja API C++ biblioteki VIPS 8
Group:		Documentation
BuildArch:	noarch

%description -n libvips-cpp8-apidocs
C++ API documentation for VIPS 8 library.

%description -n libvips-cpp8-apidocs -l pl.UTF-8
Dokumentacja API C++ biblioteki VIPS 8.

%prep
%setup -q -n libvips-%{version}

# it seems to support both python2/python3, prefer the latter
%{__sed} -i -e '1s,/usr/bin/python$,%{__python3},' \
      tools/vipsprofile

%build
%{__gtkdocize} --docdir doc
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_libspng:--without-libspng}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvips-cpp.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvips.la

# packaged as %doc in libvips-cpp8-apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/vips/html

%find_lang vips8.11 -o %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libvips -p /sbin/ldconfig
%postun	-n libvips -p /sbin/ldconfig

%post	-n libvips-cpp8 -p /sbin/ldconfig
%postun	-n libvips-cpp8 -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/batch_crop
%attr(755,root,root) %{_bindir}/batch_image_convert
%attr(755,root,root) %{_bindir}/batch_rubber_sheet
%attr(755,root,root) %{_bindir}/light_correct
%attr(755,root,root) %{_bindir}/shrink_width
%attr(755,root,root) %{_bindir}/vips
%attr(755,root,root) %{_bindir}/vips-8.11
%attr(755,root,root) %{_bindir}/vipsedit
%attr(755,root,root) %{_bindir}/vipsheader
%attr(755,root,root) %{_bindir}/vipsprofile
%attr(755,root,root) %{_bindir}/vipsthumbnail
%{_mandir}/man1/batch_crop.1*
%{_mandir}/man1/batch_image_convert.1*
%{_mandir}/man1/batch_rubber_sheet.1*
%{_mandir}/man1/light_correct.1*
%{_mandir}/man1/vips.1*
%{_mandir}/man1/vipsedit.1*
%{_mandir}/man1/vipsheader.1*
%{_mandir}/man1/vipsprofile.1*
%{_mandir}/man1/vipsthumbnail.1*

%files -n libvips
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md THANKS
%attr(755,root,root) %{_libdir}/libvips.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvips.so.42
%{_libdir}/girepository-1.0/Vips-8.0.typelib

%files -n libvips-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvips.so
%dir %{_includedir}/vips
%{_includedir}/vips/almostdeprecated.h
%{_includedir}/vips/arithmetic.h
%{_includedir}/vips/basic.h
%{_includedir}/vips/buf.h
%{_includedir}/vips/colour.h
%{_includedir}/vips/connection.h
%{_includedir}/vips/conversion.h
%{_includedir}/vips/convolution.h
%{_includedir}/vips/create.h
%{_includedir}/vips/dbuf.h
%{_includedir}/vips/debug.h
%{_includedir}/vips/deprecated.h
%{_includedir}/vips/dispatch.h
%{_includedir}/vips/draw.h
%{_includedir}/vips/enumtypes.h
%{_includedir}/vips/error.h
%{_includedir}/vips/foreign.h
%{_includedir}/vips/format.h
%{_includedir}/vips/freqfilt.h
%{_includedir}/vips/gate.h
%{_includedir}/vips/generate.h
%{_includedir}/vips/header.h
%{_includedir}/vips/histogram.h
%{_includedir}/vips/image.h
%{_includedir}/vips/interpolate.h
%{_includedir}/vips/intl.h
%{_includedir}/vips/mask.h
%{_includedir}/vips/memory.h
%{_includedir}/vips/morphology.h
%{_includedir}/vips/mosaicing.h
%{_includedir}/vips/object.h
%{_includedir}/vips/operation.h
%{_includedir}/vips/private.h
%{_includedir}/vips/rect.h
%{_includedir}/vips/region.h
%{_includedir}/vips/resample.h
%{_includedir}/vips/sbuf.h
%{_includedir}/vips/semaphore.h
%{_includedir}/vips/soname.h
%{_includedir}/vips/thread.h
%{_includedir}/vips/threadpool.h
%{_includedir}/vips/transform.h
%{_includedir}/vips/type.h
%{_includedir}/vips/util.h
%{_includedir}/vips/VConnection8.h
%{_includedir}/vips/vector.h
%{_includedir}/vips/version.h
%{_includedir}/vips/video.h
%{_includedir}/vips/vips7compat.h
%{_includedir}/vips/vips.h
%{_datadir}/gir-1.0/Vips-8.0.gir
%{_pkgconfigdir}/vips.pc

%files -n libvips-static
%defattr(644,root,root,755)
%{_libdir}/libvips.a

%files -n libvips-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libvips

%files -n libvips-cpp8
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvips-cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvips-cpp.so.42

%files -n libvips-cpp8-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvips-cpp.so
%{_includedir}/vips/VError8.h
%{_includedir}/vips/VImage8.h
%{_includedir}/vips/VInterpolate8.h
%{_includedir}/vips/vips8
%{_pkgconfigdir}/vips-cpp.pc

%files -n libvips-cpp8-static
%defattr(644,root,root,755)
%{_libdir}/libvips-cpp.a

%files -n libvips-cpp8-apidocs
%defattr(644,root,root,755)
%doc cplusplus/html/{search,*.css,*.html,*.js,*.png}
