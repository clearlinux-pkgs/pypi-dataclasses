#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-dataclasses
Version  : 0.8
Release  : 22
URL      : https://files.pythonhosted.org/packages/1f/12/7919c5d8b9c497f9180db15ea8ead6499812ea8264a6ae18766d93c59fe5/dataclasses-0.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/1f/12/7919c5d8b9c497f9180db15ea8ead6499812ea8264a6ae18766d93c59fe5/dataclasses-0.8.tar.gz
Summary  : A backport of the dataclasses module for Python 3.6
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-dataclasses-license = %{version}-%{release}
Requires: pypi-dataclasses-python = %{version}-%{release}
Requires: pypi-dataclasses-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: https://img.shields.io/pypi/v/dataclasses.svg
:target: https://pypi.org/project/dataclasses/

%package license
Summary: license components for the pypi-dataclasses package.
Group: Default

%description license
license components for the pypi-dataclasses package.


%package python
Summary: python components for the pypi-dataclasses package.
Group: Default
Requires: pypi-dataclasses-python3 = %{version}-%{release}

%description python
python components for the pypi-dataclasses package.


%package python3
Summary: python3 components for the pypi-dataclasses package.
Group: Default
Requires: python3-core
Provides: pypi(dataclasses)

%description python3
python3 components for the pypi-dataclasses package.


%prep
%setup -q -n dataclasses-0.8
cd %{_builddir}/dataclasses-0.8
pushd ..
cp -a dataclasses-0.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656408621
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-dataclasses
cp %{_builddir}/dataclasses-0.8/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-dataclasses/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-dataclasses/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
