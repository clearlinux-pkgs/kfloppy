#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3A6A4DB839EAA6D7 (aacid@kde.org)
#
Name     : kfloppy
Version  : 22.12.1
Release  : 48
URL      : https://download.kde.org/stable/release-service/22.12.1/src/kfloppy-22.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.1/src/kfloppy-22.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.1/src/kfloppy-22.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0
Requires: kfloppy-bin = %{version}-%{release}
Requires: kfloppy-data = %{version}-%{release}
Requires: kfloppy-license = %{version}-%{release}
Requires: kfloppy-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcrash-dev
BuildRequires : kdoctools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KFloppy 2.1
===========
KFloppy was "done and feature complete and bug free", for systems
running Linux. Other KDE platforms had an app that put up a warning
box and was then totally inert. I've restructured the whole thing,
cleaned up the code somewhat, and modularized it.

%package bin
Summary: bin components for the kfloppy package.
Group: Binaries
Requires: kfloppy-data = %{version}-%{release}
Requires: kfloppy-license = %{version}-%{release}

%description bin
bin components for the kfloppy package.


%package data
Summary: data components for the kfloppy package.
Group: Data

%description data
data components for the kfloppy package.


%package doc
Summary: doc components for the kfloppy package.
Group: Documentation

%description doc
doc components for the kfloppy package.


%package license
Summary: license components for the kfloppy package.
Group: Default

%description license
license components for the kfloppy package.


%package locales
Summary: locales components for the kfloppy package.
Group: Default

%description locales
locales components for the kfloppy package.


%prep
%setup -q -n kfloppy-22.12.1
cd %{_builddir}/kfloppy-22.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673307929
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1673307929
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kfloppy
cp %{_builddir}/kfloppy-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kfloppy/7c203dee3a03037da436df03c4b25b659c073976 || :
cp %{_builddir}/kfloppy-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kfloppy/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
pushd clr-build
%make_install
popd
%find_lang kfloppy

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kfloppy

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kfloppy.desktop
/usr/share/icons/hicolor/128x128/apps/kfloppy.png
/usr/share/icons/hicolor/16x16/apps/kfloppy.png
/usr/share/icons/hicolor/22x22/apps/kfloppy.png
/usr/share/icons/hicolor/32x32/apps/kfloppy.png
/usr/share/icons/hicolor/48x48/apps/kfloppy.png
/usr/share/icons/hicolor/64x64/apps/kfloppy.png
/usr/share/metainfo/org.kde.kfloppy.appdata.xml
/usr/share/qlogging-categories5/kfloppy.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kfloppy/index.cache.bz2
/usr/share/doc/HTML/ca/kfloppy/index.docbook
/usr/share/doc/HTML/de/kfloppy/index.cache.bz2
/usr/share/doc/HTML/de/kfloppy/index.docbook
/usr/share/doc/HTML/en/kfloppy/index.cache.bz2
/usr/share/doc/HTML/en/kfloppy/index.docbook
/usr/share/doc/HTML/es/kfloppy/index.cache.bz2
/usr/share/doc/HTML/es/kfloppy/index.docbook
/usr/share/doc/HTML/et/kfloppy/index.cache.bz2
/usr/share/doc/HTML/et/kfloppy/index.docbook
/usr/share/doc/HTML/fr/kfloppy/index.cache.bz2
/usr/share/doc/HTML/fr/kfloppy/index.docbook
/usr/share/doc/HTML/gl/kfloppy/index.cache.bz2
/usr/share/doc/HTML/gl/kfloppy/index.docbook
/usr/share/doc/HTML/it/kfloppy/index.cache.bz2
/usr/share/doc/HTML/it/kfloppy/index.docbook
/usr/share/doc/HTML/nl/kfloppy/index.cache.bz2
/usr/share/doc/HTML/nl/kfloppy/index.docbook
/usr/share/doc/HTML/pt/kfloppy/index.cache.bz2
/usr/share/doc/HTML/pt/kfloppy/index.docbook
/usr/share/doc/HTML/pt_BR/kfloppy/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kfloppy/index.docbook
/usr/share/doc/HTML/ru/kfloppy/index.cache.bz2
/usr/share/doc/HTML/ru/kfloppy/index.docbook
/usr/share/doc/HTML/sr/kfloppy/index.cache.bz2
/usr/share/doc/HTML/sr/kfloppy/index.docbook
/usr/share/doc/HTML/sr@latin/kfloppy/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kfloppy/index.docbook
/usr/share/doc/HTML/sv/kfloppy/index.cache.bz2
/usr/share/doc/HTML/sv/kfloppy/index.docbook
/usr/share/doc/HTML/uk/kfloppy/index.cache.bz2
/usr/share/doc/HTML/uk/kfloppy/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kfloppy/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/kfloppy/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files locales -f kfloppy.lang
%defattr(-,root,root,-)

