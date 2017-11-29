%global prerelease beta1

Name:		qpdfview
Version:	0.4.17
Release:	0.5.%{?prerelease}%{?dist}
License:	GPLv2+
Summary:	Tabbed PDF Viewer
Url:		https://launchpad.net/qpdfview
Source0:	https://launchpad.net/qpdfview/trunk/%{version}%{?prerelease}/+download/%{name}-%{version}%{?prerelease}.tar.gz
BuildRequires:  qt5-qttools
BuildRequires:	cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  file-devel
BuildRequires:  cups-devel
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	djvulibre-devel

%description
qpdfview is a tabbed PDF viewer.
It uses the Poppler library for rendering and CUPS for printing.
It provides a clear and simple graphical user interface using the Qt framework.


%prep
%setup -n %{name}-%{version}%{?prerelease}

%build
%{_qt5_bindir}/lrelease qpdfview.pro
%{qmake_qt5} \
    PLUGIN_INSTALL_PATH="%{_libdir}/%{name}" \
    DATA_INSTALLPATH="%{_datadir}/%{name}" \
    qpdfview.pro
make %{?_smp_mflags}


%install
make INSTALL_ROOT=%{buildroot} install
install -Dm 0644 icons/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt --without-mo
# unknown language
rm -f %{buildroot}/%{_datadir}/%{name}/%{name}_ast.qm


%post
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
/usr/bin/update-desktop-database &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


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
* Thu Sep 08 2016 Vaughan <devel at agrez dot net> - 0.4.16-4
- Build against Qt5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

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
