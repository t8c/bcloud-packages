# bcloud.spec
# Used to build rpm for bcloud on Fedora 20
# Released by wangjiezhe <wangjiezhe@gmail.com>
# This spec file is published under the GPLv3 license

# Template is originally generated by "rpmdev-newspec -t python"

%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python3_lib; print(get_python3_lib())")}

Name:           bcloud
Version:        2.1.4
Release:        1%{?dist}
Summary:        Baidu Pan client for Linux Desktop users

License:        GPLv3
URL:            https://github.com/LiuLang/bcloud
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:  python3-gobject
Requires:  python3-urllib3
Requires:  gnome-icon-theme-symbolic

%description


%prep
%setup -q


%build
%{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc LICENSE README.md HISTORY
%{python3_sitelib}/*
%{_datadir}/icons/*
# %{_datadir}/bcloud/*
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
# generated by python3
%exclude %{python3_sitelib}/bcloud/__pycache__

%post
for file in /usr/lib/python3.3/site-packages/bcloud*
do
	if [ -f $file ] && [ $file != "bcloud-%{version}-py3.3.egg-info" ]
	then
		rm $file
	fi
done

