Summary:	The fvhlib Library
Summary(pl):	Biblioteka fvhlib
Name:		fvhlib
Version:	2.5
Release:	1
License:	distributable
Group:		Libraries
Source0:	http://www.vanheusden.com/fvhlib/%{name}-%{version}.tgz
# Source0-md5:	130d71aef497e9f890f2a67f882acef9
Patch0:		%{name}-linking.patch
URL:		http://www.vanheusden.com/fvhlib/
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fvhlib Library.

%description -l pl
Biblioteka fvhlib.

%package devel
Summary:	Development files for fvhlib library
Summary(pl):	Pliki nag³ówkowe dla biblioteki fvhlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The fvhlib-devel package contains the header files needed to develop
applications with fvhlib.

%description devel -l pl
Pliki nag³ówkowe potrzebne do rozwijania aplikacji korzystaj±cych z
biblioteki fvhlib.

%package static
Summary:	Static development library for fvhlib
Summary(pl):	Biblioteka statyczna fvhlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
The fvhlib-static package contains the static version of fvhlib.

%description static -l pl
Biblioteka statyczna fvhlib.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -Wshadow -Wwrite-strings -Wconversion"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/%{name}}

install libfvh.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install libfvh.a $RPM_BUILD_ROOT%{_libdir}
install *.h $RPM_BUILD_ROOT%{_includedir}/%{name}

ln -sf libfvh.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libfvh.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfvh.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfvh.so
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libfvh.a
