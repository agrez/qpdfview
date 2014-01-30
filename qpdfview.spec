Name:		qpdfview
Version:	0.4.8
Release:	1%{?dist}
License:	GPLv2+
Summary:	Tabbed PDF Viewer
Url:		https://launchpad.net/qpdfview
Source0:	https://launchpad.net/qpdfview/trunk/0.4.5/+download/%{name}-%{version}.tar.gz
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
lrelease-qt4 qpdfview.pro
qmake-qt4 \
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
%find_lang %{name} --with-qt --without-mo
# unknown language
rm -f %{buildroot}/%{_datadir}/%{name}/%{name}_ast.qm

%post	-p /sbin/ldconfig

%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%doc CHANGES CONTRIBUTORS COPYING README TODO
%{_bindir}/%{name}
%{_libdir}/%{name}/
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help*.html
%{_datadir}/%{name}/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man?/*

%changelog
* Thu Jan 30 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.8-1
- Version bump

* Sun Dec 08 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.7-1
- Version bump

* Sun Oct 13 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.6-1
- Version bump

* Fri Sep 06 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.5-1
- Version bump

* Tue Jul 30 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.4-1
- Version bump

* Sun May 26 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.3-1
- Version bump
- Translations added
- post/postun ldconfig added

* Mon Mar 25 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.1-1
- New version
- License changed to GPLv2+

* Sat Mar 23 2013 TI_Eugene <ti.eugene@gmail.com> 0.4-1
- initial packaging for Fedora
