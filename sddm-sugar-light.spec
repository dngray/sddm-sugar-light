%global srcname copr-sddm-sugar-light
%global commit 19bac00e7bd99e0388d289bdde41bf6644b88772
%global commitdate 20190202
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: sddm-sugar-light
Version: 1.0^%{commitdate}.%{shortcommit}
Release: 0%{?dist}
License: GPLv3
Summary: The sweetest light theme around for SDDM, the Simple Desktop Display Manager.
URL: https://github.com/MarianArlt/%{name}
Source0: %{URL}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch: noarch

Requires: qt5-qtgraphicaleffects
Requires: qt5-qtquickcontrols2
Requires: qt5-qtsvg
Requires: sddm

%description
Sugar is extremely customizable and so sweet it will probably cause you
diabetes just from looking at it. Sweeten the login experience for your users,
your family and yourself. Sugar is cross platform and all about user experience
and functionality.

With those principles in mind Sugar was written completely from scratch making
it clean and simple not only by looks but by design too.

All controls use the latest Qt Quick Controls 2 for increased performance on
low end or even embedded systems.

%prep
%setup -n %{name}-%{commit}

%install
mkdir -p %{buildroot}%{_datadir}/sddm/themes/sugar-light
cp -ar {Assets,Components,Background.jpg,Illustration.svg,Main.qml,metadata.desktop} \
        %{buildroot}%{_datadir}/sddm/themes/sugar-light
cp theme.conf %{buildroot}%{_datadir}/sddm/themes/sugar-light/theme.conf

%files
%license COPYING
%doc AUTHORS
%doc CREDITS
%doc README.md
%{_datadir}/sddm/themes/sugar-light

%changelog
