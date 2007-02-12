Summary:	A GTK+ tool to configure window decorations in compiz
Summary(pl.UTF-8):   Narzędzie GTK+ do konfiguracji dekoracji okien w compizie
Name:		gcompizthemer
Version:	0.7
Release:	1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://distfiles.xgl-coffee.org/gcompizthemer/%{name}-%{version}.tar.gz
# Source0-md5:	281b81c13568d1860ed61e6c91066c9e
URL:		http://compiz.net
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	pkgconfig
Requires:	compiz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK+ tool to configure window decorations in compiz.

%description -l pl.UTF-8
Narzędzie GTK+ do konfiguracji dekoracji okien w compizie.

%prep
%setup -q -n %{name}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man*/*
%{_datadir}/compiz/themes
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}-icon.png
