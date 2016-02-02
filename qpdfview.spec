Name:		qpdfview
Version:	0.4.16
Release:	2%{?dist}
License:	GPLv2+
Summary:	Tabbed PDF Viewer
Url:		https://launchpad.net/qpdfview
Source0:	https://launchpad.net/qpdfview/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:	desktop-file-utils file-devel cups-devel hicolor-icon-theme pkgconfig(poppler-qt4) pkgconfig(libspectre) pkgconfig(QtGui) pkgconfig(QtDBus) pkgconfig(zlib)
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
%setup0 -q


%build
lrelease-qt4 qpdfview.pro
%{qmake_qt4} \
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
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man?/*

%changelog
* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.4.16-2
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jan 07 2016 TI_Eugene <ti.eugene@gmail.com> 0.4.16-1
- Version bump

* Fri Oct 09 2015 TI_Eugene <ti.eugene@gmail.com> 0.4.15-1
- Version bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.13-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Nov 18 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.13-1
- Version bump

* Mon Oct 06 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.12-1
- Version bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.11-1
- Version bump

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.10-1
- Version bump

* Sun Mar 23 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.9-1
- Version bump

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
