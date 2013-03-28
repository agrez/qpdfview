Name:		qpdfview
Version:	0.4.1
Release:	1%{?dist}
License:	GPLv2+
Summary:	Tabbed PDF Viewer
Url:		https://launchpad.net/qpdfview
Source0:	https://launchpad.net/qpdfview/trunk/0.4.1/+download/%{name}-%{version}.tar.gz
Patch0:		%{name}-0.4-desktop.patch
BuildRequires:	desktop-file-utils file-devel cups-devel hicolor-icon-theme pkgconfig(poppler-qt4) pkgconfig(libspectre) pkgconfig(QtGui) pkgconfig(QtSql) pkgconfig(QtDBus) pkgconfig(zlib)
%if 0%{?centos_version}
Requires:	qt-sqlite
%else
BuildRequires:	pkgconfig(ddjvuapi)
%endif

%description
qpdfview is a tabbed PDF viewer.
It uses the Poppler library for rendering and CUPS for printing.
It provides a clear and simple graphical user interface using the Qt framework.

%prep
%setup -q
%patch0

%build
`pkg-config --variable=exec_prefix QtCore`/bin/qmake \
    QMAKE_CFLAGS+="%{optflags}" \
    QMAKE_CXXFLAGS+="%{optflags}" \
    QMAKE_STRIP="" \
    PLUGIN_INSTALL_PATH="%{_libdir}/%{name}" \
    DATA_INSTALLPATH="%{_datadir}/%{name}" \
%if 0%{?centos_version}
    CONFIG+=without_djvu \
%endif
    qpdfview.pro
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
install -Dm 0644 icons/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc CHANGES CONTRIBUTORS COPYING README TODO
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man?/*

%changelog
* Thu Mar 25 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.1-1
- New version
- License changed to GPLv2+

* Thu Mar 23 2013 TI_Eugene <ti.eugene@gmail.com> 0.4-1
- initial packaging for Fedora
