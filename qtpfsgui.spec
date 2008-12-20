Name:		qtpfsgui
Summary:	A Qt4 graphical user interface that provides a workflow for HDR imaging
Version:	1.9.2
Release:	%mkrel 2
License:	LGPL2+
Group:		Graphics
URL:		http://qtpfsgui.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		qtpfsgui-1.8.12-fix-desktop.patch
Patch1:		qtpfsgui-1.9.2-fix-str-fmt.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	qt4-devel
BuildRequires:	libexiv-devel
BuildRequires:	libOpenEXR-devel
BuildRequires:	fftw3-devel
BuildRequires:	tiff-devel

%description
Qtpfsgui is a Qt4 graphical user interface that aims to provide a 
workflow for HDR imaging.

    * Create an HDR file from a set of images (formats: JPEG, TIFF 8bit 
and 16bit, RAW) of the same scene taken at different exposure setting.
    * Save and load HDR images.
    * Rotate and resize HDR images.
    * Tonemap HDR images.
    * Copy exif data between sets of images.
    * Supports internationalization.


%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
sed -i -e 's,QMAKE_CXXFLAGS,#QMAKE_CXXFLAGS,g' project.pro
%qmake_qt4 PREFIX=%{buildroot}%{_prefix}
%make

%install
rm -fr %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS Changelog README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/%{name}

