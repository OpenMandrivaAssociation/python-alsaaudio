%define fname		pyalsaaudio

Summary:	ALSA wrapper for Python
Name:		python-alsaaudio
Version:	0.11.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/p/pyalsaaudio/pyalsaaudio-%{version}.tar.gz
License:	Python
URL:		https://sourceforge.net/projects/pyalsaaudio/
Group:		Development/Python
BuildRequires:	python-devel
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	pkgconfig(alsa)

%description
The goal of this project is to provide a functionality complete Python
wrapper for ALSA. Currently PCM playback and capture, as well as the
mixer API is supported.

%prep
%autosetup -p1 -n %{fname}-%{version}

%build
%py_build

%install
%py_install

%files
%defattr(-,root,root)
%doc LICENSE TODO
%{py_platsitedir}/alsaaudio*.so
%{py_platsitedir}/%{fname}-%{version}-py%{pyver}.egg-info
