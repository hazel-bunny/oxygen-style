%global toolchain clang
%define _lto_cflags %{nil}

%global style oxygen
%global dev   hazel-bunny
%global app_id org.kde.%{style}

%if 0%{?rhel} && 0%{?rhel} >= 10
%bcond_with kf5
%else
%bcond_without kf5
%endif

Name:           plasma-%{style}-%{dev}
Version:        6.6.0

%global forgeurl https://github.com/%{dev}/%{style}-style
%global tag %{version}
%global date 20260209
%forgemeta

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Release:        0%{?dist}
Summary:        The Oxygen style for KDE, updated to maintain its former glory, and to add a matching QML style
License:        CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:            %{forgeurl}
Source:         %{forgesource}
# Patch:          window_buttons_workaround.patch

# Misc
BuildRequires:  chrpath
BuildRequires:  clang
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  libxcb-devel
BuildRequires:  cmake(Plasma)

%if %{with kf5}
# Qt5
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)

BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)

Requires:       (%{name}-qt5 if qt5-qtbase-gui)
%endif

# Qt6
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6FrameworkIntegration)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel

%if 0%{?rhel} >= 10 || 0%{?fedora} >= 42
BuildRequires:  cmake(Qt6GuiPrivate)
%endif

Requires:       kf6-filesystem

Requires:       %{name}-qt6
Requires:       %{name}-cursor-themes >= %{version}
Requires:       qqc2-%{style}-style
Requires:       %{style}-sound-theme
# for oxygen look-and-feel
Requires:       %{style}-icon-theme

Provides:       plasma-%{style}
Conflicts:      plasma-%{style}

# kwin-oxygen was removed in 5.1.95
Obsoletes:      kwin-%{style} < 5.1.95-1
Conflicts:      plasma-desktop < 5.16.90

%description
%{summary}.

This is a fork of the Oxygen KDE style which was originally implemented for KDE4.

%files -f %{style}.lang
%license LICENSES/*
%{_bindir}/%{style}-settings6
%{_kf6_datadir}/applications/kcm_%{style}decoration.desktop
%{_kf6_datadir}/color-schemes/Oxygen.colors
%{_kf6_datadir}/color-schemes/OxygenCold.colors
%{_kf6_datadir}/icons/hicolor/*/apps/%{style}-settings.*
%{_kf6_datadir}/kstyle/themes/%{style}.themerc
%{_kf6_datadir}/plasma/look-and-feel/%{app_id}/
%{_kf6_datadir}/plasma/desktoptheme/%{style}/
# %%{_kf6_metainfodir}/%{app_id}.appdata.xml
%{_kf6_qtplugindir}/kstyle_config/kstyle_%{style}_config.so
%{_kf6_qtplugindir}/org.kde.kdecoration3.kcm/kcm_%{style}decoration.so
%{_kf6_qtplugindir}/org.kde.kdecoration3/%{app_id}.so

#--------------------------------------------------------------------------------------------------

%if %{with kf5}
%package        qt5
Summary:        Oxygen widget style for Qt 5
Obsoletes:      qt5-style-%{style} < %{version}-%{release}
Provides:       qt5-style-%{style} = %{version}-%{release}
Conflicts:      plasma-%{style}-qt5

%description    qt5
%{summary}.

%files qt5
%{_bindir}/%{style}-demo5
%{_libdir}/lib%{style}style5.so.*
%{_libdir}/lib%{style}styleconfig5.so.*
%{_kf5_qtplugindir}/styles/%{style}5.so
%endif

#--------------------------------------------------------------------------------------------------

%package        qt6
Summary:        Oxygen widget style for Qt 6
Conflicts:      plasma-%{style}-qt6

%description    qt6
%{summary}.

%files qt6
%{_bindir}/%{style}-demo6
%{_libdir}/lib%{style}style6.so.*
%{_libdir}/lib%{style}styleconfig6.so.*
%{_kf6_qtplugindir}/styles/%{style}6.so

#--------------------------------------------------------------------------------------------------

%package        cursor-themes
Summary:        Oxygen cursor themes
BuildArch:      noarch
Conflicts:      %{style}-cursor-themes
Obsoletes:      plasma-%{style}-common < 5.1.1-2

%description    cursor-themes
%{summary}.

%files          cursor-themes
%{_datadir}/icons/KDE_Classic/
%{_datadir}/icons/Oxygen_Black/
%{_datadir}/icons/Oxygen_Blue/
%{_datadir}/icons/Oxygen_White/
%{_datadir}/icons/Oxygen_Yellow/
%{_datadir}/icons/Oxygen_Zion/

#---------------------------------------------------------------------------------------------------

%package -n     qqc2-%{style}-style
Summary:        Oxygen style for QQC2 apps
Requires:       kf6-qqc2-desktop-style

%description -n qqc2-%{style}-style
%{summary}.

%files -n       qqc2-%{style}-style
%{_sysconfdir}/skel/.config/plasma-workspace/env/configure-%{style}.sh
%{_qt6_qmldir}/org/kde/%{style}/
%{_qt6_qmldir}/org/kde/qqc2%{style}style/
%{_kf6_plugindir}/kirigami/platform/org.kde.%{style}.so

#---------------------------------------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
mkdir qt6build qt5build
pushd qt6build
%cmake_kf6 -S .. -DBUILD_QT6=ON -DBUILD_QT5=OFF
# -DCMAKE_BUILD_WITH_INSTALL_RPATH=OFF -DCMAKE_SKIP_INSTALL_RPATH=ON
%cmake_build
popd

%if %{with kf5}
pushd qt5build
%cmake_kf5 -S .. -DBUILD_QT6=OFF -DBUILD_QT5=ON
%cmake_build
popd
%endif

%install
pushd qt6build
%cmake_install
popd

%if %{with kf5}
pushd qt5build
%cmake_install
popd
%endif

install -Dm644 -t %{buildroot}%{_sysconfdir}/skel/.config/plasma-workspace/env/ qtquickcontrols/configure-%{style}.sh

chrpath --delete %{buildroot}%{_libdir}/qt6/plugins/kf6/kirigami/platform/org.kde.oxygen.so
#patchelf --remove-rpath %{buildroot}%{_libdir}/qt6/plugins/kf6/kirigami/platform/org.kde.oxygen.so

%find_lang %{style} --with-qt --all-name

#---------------------------------------------------------------------------------------------------

%changelog
* Mon Feb 9 2026 Hazel Bunny <hazel_bunny@disroot.org> - 6.6.0-0
- Update to 6.6.0

* Fri Sep 5 2025 Hazel Bunny <hazel_bunny@disroot.org> - 0-1.20250829gitece2e521
- Intial snapshot
