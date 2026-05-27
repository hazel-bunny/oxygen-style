%global style oxygen
%global dev   hazel-bunny
%global app_id org.kde.%{style}

# Cursor size
%define _cursorsize_ ""
#_cursorsize_="-big"

# Theme list for cursors
%define _themelist_ "bluecurve brown cherry chrome desert emerald green grey honeycomb hot_orange lilac midnight_meadow navy norway obsidian obsidian-hc olympus olympus-inv orchid oxygen peach purple red red-argentina sea_blue steel terra terra_green violet viorange whitewater wonton"
#_themelist_="${_themelist_} black blue white yellow zion"

%bcond kf5 %[%{undefined rhel} || 0%{?rhel} < 10]
%bcond extra_cursors %[%{undefined rhel} || 0%{?rhel} < 10]

Name:           plasma-%{style}-%{dev}
Version:        6.6.6

%global forgeurl https://github.com/%{dev}/%{style}-style
%global tag %{version}
%global date 20260528
%forgemeta

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Release:        0%{?dist}
Summary:        The Oxygen style for KDE, updated to maintain its former glory, and to add a matching QML style
License:        CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:            %{forgeurl}
Source:         %{forgesource}

# Misc
BuildRequires:  chrpath
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libxcb-devel
BuildRequires:  cmake(Plasma)

%if %{with extra_cursors}
BuildRequires:  inkscape
BuildRequires:  xcursorgen

Suggests:       %{name}-cursor-themes-extra
%endif

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
BuildRequires:  cmake(KF6QQC2DesktopStyle)
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
Requires:       kf6-qqc2-desktop-style

Requires:       %{name}-common
Requires:       %{name}-qt6
Requires:       %{name}-cursor-themes >= %{version}
Requires:       %{style}-sound-theme
# for oxygen look-and-feel
Requires:       %{style}-icon-theme

Recommends:     qqc2-%{style}-style

Suggests:       %{name}-colors
Suggests:       plasma-air-%{dev}

Provides:       plasma-%{style}
Conflicts:      plasma-%{style}

# kwin-oxygen was removed in 5.1.95
Obsoletes:      kwin-%{style} < 5.1.95-1
Conflicts:      plasma-desktop < 5.16.90

%description
%{summary}.

This is a fork of the Oxygen KDE style which was originally implemented for KDE4.

%files
%{_kf6_datadir}/plasma/look-and-feel/%{app_id}/
%{_kf6_datadir}/plasma/look-and-feel/%{app_id}light/
%{_kf6_datadir}/plasma/desktoptheme/%{style}-remix/
%{_kf6_datadir}/plasma/desktoptheme/%{style}/
%{_kf6_datadir}/wallpapers/Horos/

#--------------------------------------------------------------------------------------------------

%package        common
Summary:        Common files for the Oxygen style for KDE
Obsoletes:      plasma-%{style}-common < %{version}

%description    common
%{summary}.

%files common -f %{style}.lang
%license LICENSES/*
%{_kf6_bindir}/%{style}-settings6
%{_kf6_datadir}/applications/kcm_%{style}decoration.desktop
%{_kf6_datadir}/color-schemes/Oxygen.colors
%{_kf6_datadir}/color-schemes/OxygenCold.colors
%{_kf6_datadir}/color-schemes/OxygenDark.colors
%{_kf6_datadir}/icons/hicolor/*/apps/%{style}-settings.*
%{_kf6_datadir}/kstyle/themes/%{style}.themerc
%{_kf6_qtplugindir}/kstyle_config/kstyle_%{style}_config.so
%{_kf6_qtplugindir}/org.kde.kdecoration3.kcm/kcm_%{style}decoration.so
%{_kf6_qtplugindir}/org.kde.kdecoration3/%{app_id}.so

#--------------------------------------------------------------------------------------------------

%package     -n plasma-air-%{dev}
Summary:        The Air style for KDE
Requires:       %{name}-common
Requires:       %{name}-qt6
Requires:       %{name}-cursor-themes >= %{version}
Requires:       %{style}-sound-theme
# for oxygen look-and-feel
Requires:       %{style}-icon-theme
Conflicts:      plasma-air

%description -n plasma-air-%{dev}
%{summary}.

%files -n plasma-air-%{dev}
%{_kf6_datadir}/plasma/look-and-feel/org.kde.air/
%{_kf6_datadir}/plasma/desktoptheme/air/
%{_kf6_datadir}/wallpapers/Air/

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
%{_kf5_bindir}/%{style}-demo5
%{_kf5_libdir}/lib%{style}style5.so.*
%{_kf5_libdir}/lib%{style}styleconfig5.so.*
%{_kf5_qtplugindir}/styles/%{style}5.so
%endif

#--------------------------------------------------------------------------------------------------

%package        qt6
Summary:        Oxygen widget style for Qt 6
Conflicts:      plasma-%{style}-qt6

%description    qt6
%{summary}.

%files qt6
%{_kf6_bindir}/%{style}-demo6
%{_kf6_libdir}/lib%{style}style6.so.*
%{_kf6_libdir}/lib%{style}styleconfig6.so.*
%{_kf6_qtplugindir}/styles/%{style}6.so

#--------------------------------------------------------------------------------------------------

%package        colors
Summary:        Oxygen classic color schemes
BuildArch:      noarch

%description    colors
%{summary}.

%files          colors
%{_kf6_datadir}/color-schemes/BlueDeep.colors
%{_kf6_datadir}/color-schemes/CherryBlossom.colors
%{_kf6_datadir}/color-schemes/Chrome.colors
%{_kf6_datadir}/color-schemes/Desert.colors
%{_kf6_datadir}/color-schemes/EveningLilac.colors
%{_kf6_datadir}/color-schemes/HazelDark.colors
%{_kf6_datadir}/color-schemes/HighlandMist.colors
%{_kf6_datadir}/color-schemes/Honeycomb.colors
%{_kf6_datadir}/color-schemes/MidnightMeadow.colors
%{_kf6_datadir}/color-schemes/Norway.colors
%{_kf6_datadir}/color-schemes/ObsidianCoast.colors
%{_kf6_datadir}/color-schemes/Steel.colors
%{_kf6_datadir}/color-schemes/StoneOrchid.colors
%{_kf6_datadir}/color-schemes/Terra.colors
%{_kf6_datadir}/color-schemes/WhitePeach.colors
%{_kf6_datadir}/color-schemes/Whitewater.colors
%{_kf6_datadir}/color-schemes/WontonSoup.colors
%{_kf6_datadir}/color-schemes/Zion.colors
%{_kf6_datadir}/color-schemes/ZionReversed.colors

#--------------------------------------------------------------------------------------------------

%package        cursor-themes
Summary:        Oxygen cursor themes
BuildArch:      noarch
Conflicts:      %{style}-cursor-themes

%description    cursor-themes
%{summary}.

%files          cursor-themes
%{_kf6_datadir}/icons/KDE_Classic/
%{_kf6_datadir}/icons/Oxygen_Black/
%{_kf6_datadir}/icons/Oxygen_Blue/
%{_kf6_datadir}/icons/Oxygen_White/
%{_kf6_datadir}/icons/Oxygen_Yellow/
%{_kf6_datadir}/icons/Oxygen_Zion/

#--------------------------------------------------------------------------------------------------

%if %{with extra_cursors}
%package        cursor-themes-extra
Summary:        Extra color variants of oxygen cursor themes
BuildArch:      noarch

%description    cursor-themes-extra
%{summary}.

%files          cursor-themes-extra
%{_kf5_datadir}/icons/oxy-bluecurve
%{_kf5_datadir}/icons/oxy-brown
%{_kf5_datadir}/icons/oxy-cherry
%{_kf5_datadir}/icons/oxy-chrome
%{_kf5_datadir}/icons/oxy-desert
%{_kf5_datadir}/icons/oxy-emerald
%{_kf5_datadir}/icons/oxy-green
%{_kf5_datadir}/icons/oxy-grey
%{_kf5_datadir}/icons/oxy-honeycomb
%{_kf5_datadir}/icons/oxy-hot_orange
%{_kf5_datadir}/icons/oxy-lilac
%{_kf5_datadir}/icons/oxy-midnight_meadow
%{_kf5_datadir}/icons/oxy-navy
%{_kf5_datadir}/icons/oxy-norway
%{_kf5_datadir}/icons/oxy-obsidian
%{_kf5_datadir}/icons/oxy-obsidian-hc
%{_kf5_datadir}/icons/oxy-olympus
%{_kf5_datadir}/icons/oxy-olympus-inv
%{_kf5_datadir}/icons/oxy-orchid
%{_kf5_datadir}/icons/oxy-oxygen
%{_kf5_datadir}/icons/oxy-peach
%{_kf5_datadir}/icons/oxy-purple
%{_kf5_datadir}/icons/oxy-red
%{_kf5_datadir}/icons/oxy-red-argentina
%{_kf5_datadir}/icons/oxy-sea_blue
%{_kf5_datadir}/icons/oxy-steel
%{_kf5_datadir}/icons/oxy-terra
%{_kf5_datadir}/icons/oxy-terra_green
%{_kf5_datadir}/icons/oxy-violet
%{_kf5_datadir}/icons/oxy-viorange
%{_kf5_datadir}/icons/oxy-whitewater
%{_kf5_datadir}/icons/oxy-wonton
%endif

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

%if %{with extra_cursors}
# Prepend necessary variables
pushd cursors/src
sed -i '1s/^/project(oxygen)\n/' CMakeLists.txt
sed -i '1s/^/cmake_minimum_required(VERSION 3.25)\n/' CMakeLists.txt
popd
%endif

%build
mkdir qt6build qt5build
pushd qt6build
%cmake_kf6 -S .. -DBUILD_QT6=ON -DBUILD_QT5=OFF
%cmake_build
popd

%if %{with kf5}
pushd qt5build
%cmake_kf5 -S .. -DBUILD_QT6=OFF -DBUILD_QT5=ON
%cmake_build
popd
%endif

%if %{with extra_cursors}
pushd cursors/src
cmake .

for theme in bluecurve brown cherry chrome desert emerald green grey honeycomb hot_orange lilac midnight_meadow navy norway obsidian obsidian-hc olympus olympus-inv orchid oxygen peach purple red red-argentina sea_blue steel terra terra_green violet viorange whitewater wonton; do
    make -j1 theme-${theme}%{_cursorsize_}
done

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

%if %{with extra_cursors}
pushd cursors/src
for theme in bluecurve brown cherry chrome desert emerald green grey honeycomb hot_orange lilac midnight_meadow navy norway obsidian obsidian-hc olympus olympus-inv orchid oxygen peach purple red red-argentina sea_blue steel terra terra_green violet viorange whitewater wonton; do
    cp -r --parents "oxy-${theme}%{_cursorsize_}/cursors" %{buildroot}%{_datadir}/icons/
    cp "theme-${theme}/index.theme" %{buildroot}%{_datadir}/icons/oxy-${theme}%{_cursorsize_}/
done
popd
%endif

install -Dm644 -t %{buildroot}%{_sysconfdir}/skel/.config/plasma-workspace/env/ qtquickcontrols/configure-%{style}.sh

chrpath --delete %{buildroot}%{_libdir}/qt6/plugins/kf6/kirigami/platform/org.kde.oxygen.so

%find_lang %{style} --with-qt --all-name

#---------------------------------------------------------------------------------------------------

%changelog
* Thu May 28 2026 Hazel Bunny <hazel_bunny@disroot.org> - 6.6.6-0
- Update to 6.6.6

* Mon May 18 2026 Hazel Bunny <hazel_bunny@disroot.org> - 6.6.5-0
- Update to 6.6.5

* Sat Apr 4 2026 Hazel Bunny <hazel_bunny@disroot.org> - 6.6.4-0
- Update to 6.6.4

* Sat Mar 14 2026 Hazel Bunny <hazel_bunny@disroot.org> - 6.6.3-0
- Update to 6.6.3

* Sat Mar 7 2026 Hazel Bunny <hazel_bunny@disroot.org> - 6.6.2-0
- Update to 6.6.2

* Thu Feb 26 2026 Hazel Bunny <hazel_bunny@disroot.org> - 6.6.1-0
- Update to 6.6.1

* Mon Feb 9 2026 Hazel Bunny <hazel_bunny@disroot.org> - 6.6.0-0
- Update to 6.6.0

* Fri Sep 5 2025 Hazel Bunny <hazel_bunny@disroot.org> - 0-1.20250829gitece2e521
- Intial snapshot
