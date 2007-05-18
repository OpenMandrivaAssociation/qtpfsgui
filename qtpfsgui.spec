Name:           qtpfsgui
Summary:        A Qt4 graphical user interface that provides a workflow for HDR imaging
Version:        1.8.8
Release:        %mkrel 3
License:        LGPL
Group:          Graphics
Url:	        http://qtpfsgui.sourceforge.net/
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  qt4-devel
BuildRequires:  libexiv2-devel
BuildRequires:  libOpenEXR4-devel
BuildRequires:  fftw3-devel
BuildRequires:  tiff-devel

%description

Qtpfsgui is a Qt4 graphical user interface that aims to provide a 
workflow for HDR imaging.
Supported HDR formats:

    * OpenEXR (extension: exr, linux and Mac OS X only)
    * Radiance RGBE (extension: hdr)
    * Tiff formats: 16bit, 32bit (float) and LogLuv (extension: tiff)
    * Raw image formats (extension: various)
    * PFS native format (extension: pfs)

Supported LDR formats:

    * JPEG, PNG, PPM, PBM, TIFF(8 bit)

Supported features:

    * Create an HDR file from a set of images (formats: JPEG, TIFF 8bit 
and 16bit, RAW) of the same scene taken at different exposure setting.
    * Save and load HDR images.
    * Rotate and resize HDR images.
    * Tonemap HDR images.
    * Copy exif data between sets of images.
    * Supports internationalization.

%files
%defattr(-,root,root)
%{_bindir}/qtpfsgui
%{_datadir}/applications/qtpfsgui.desktop
%{_datadir}/icons/hicolor/48x48/apps/qtpfsgui.png
%{_datadir}/qtpfsgui/html/faq.html
%{_datadir}/qtpfsgui/html/hints.html
%{_datadir}/qtpfsgui/html/images/copy_exif.jpeg
%{_datadir}/qtpfsgui/html/images/mainwin.jpeg
%{_datadir}/qtpfsgui/html/images/resize.jpeg
%{_datadir}/qtpfsgui/html/images/snap-qt4_3.jpeg
%{_datadir}/qtpfsgui/html/images/snap-qt4_4.jpeg
%{_datadir}/qtpfsgui/html/images/snap-qt4_5.jpeg
%{_datadir}/qtpfsgui/html/images/snap-qt4_6.jpeg
%{_datadir}/qtpfsgui/html/images/tonemapdialog.jpeg
%{_datadir}/qtpfsgui/html/index.html
%{_datadir}/qtpfsgui/html/manual.html

#--------------------------------------------------------------------

%prep
%setup -q

%build
export QTDIR=/usr/lib/qt4/

/usr/lib/qt4/bin/qmake PREFIX=%buildroot%_prefix

%make

%install
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot 

