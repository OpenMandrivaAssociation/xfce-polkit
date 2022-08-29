Name:           xfce-polkit
Version:        0.3
Release:        1
Summary:        Simple PolicyKit authentication agent for Xfce

License:        GPLv2+
URL:            https://github.com/ncopa/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: automake
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(libxfce4ui-2)
BuildRequires: desktop-file-utils

Provides: PolicyKit-authentication-agent

Requires: polkit >= 0.97

%description
%{summary}.


%prep
%autosetup
autoreconf -fi

%build
%configure
%make_build

%install
%make_install
desktop-file-edit --remove-key=NotShowIn --add-only-show-in=XFCE \
%{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop

%files
%license LICENSE
%doc AUTHORS README.md
# do not distribute empty documentation files
#doc ChangeLog NEWS
%{_sysconfdir}/xdg/autostart/xfce-polkit.desktop
%{_libexecdir}/%{name}
