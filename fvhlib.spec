
# conditional build:
# _without_dist_kernel    without kernel from distribution

Summary:	The fvhlib Library
Summary(pl):	Biblioteka fvhlib
Name:		fvhlib
Version:	2.4
Release:	1
License:	distributable
Group:		Libraries
Source0:	http://www.vanheusden.com/fvhlib/%{name}-%{version}.tgz
Patch0:		%{name}-linking.patch
URL:		http://www.vanheusden.com/fvhlib/
BuildRequires:	openssl-devel
%{!?_without_dist_kernel:BuildRequires: kernel-headers}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fvhlib Library.

%description -l pl
Biblioteka fvhlib.

%package devel
Summary:	Development files for fvhlib library
Summary(pl):	Pliki nagłówkowe dla biblioteki fvhlib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The fvhlib-devel package contains the header files needed to develop
applications with fvhlib.

%description devel -l pl
Pliki nagłówkowe potrzebne do rozwijania aplikacji korzystających z
biblioteki fvhlib.

%package static
Summary:	Static development library for fvhlib
Summary(pl):	Biblioteka statyczna fvhlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
The fvhlib-static package contains the static libraries of fvhlib.

%description static -l pl
Biblioteka statyczna fvhlib.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/%{name}}

install libfvh.so.2.4 $RPM_BUILD_ROOT%{_libdir}
install libfvh.a $RPM_BUILD_ROOT%{_libdir}
install *.h $RPM_BUILD_ROOT%{_includedir}/%{name}

ln -s libfvh.so.2.4 $RPM_BUILD_ROOT%{_libdir}/libfvh.so

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
