Name:           qtpfsgui
Summary:        A Qt4 graphical user interface that provides a workflow for HDR imaging
Version:        1.8.12
Release:        %mkrel 1
License:        LGPL
Group:          Graphics
Url:	        http://qtpfsgui.sourceforge.net/
Source:         http://jaist.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  qt4-devel
BuildRequires:  libexiv-devel
BuildRequires:  libOpenEXR-devel
BuildRequires:  fftw3-devel
BuildRequires:  tiff-devel
BuildRequires:  desktop-file-utils

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


%post
%update_menus

%postun
%clean_menus

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

%{qt4bin}/qmake PREFIX=%buildroot%_prefix

%make

%install
make DESTDIR=%buildroot install

desktop-file-install --vendor="" \
  --add-category="Qt" \
  --add-category="Graphics" \
  --add-category="Photography" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf %buildroot 

