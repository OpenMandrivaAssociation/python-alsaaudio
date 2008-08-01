%define fname		pyalsaaudio

Summary:	ALSA wrapper for Python
Name:		python-alsaaudio
Version:	0.3
Release:	%mkrel 4
Source0:	http://mesh.dl.sourceforge.net/sourceforge/%{fname}/%{fname}-%{version}.tar.gz
License:	Python
URL:		http://sourceforge.net/projects/pyalsaaudio/
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	python-devel
BuildRequires:	alsa-lib-devel

%description
The goal of this project is to provide a functionality complete Python
wrapper for ALSA. Currently PCM playback and capture, as well as the
mixer API is supported.

%prep
%setup -q -n %{fname}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE CHANGES README TODO
%{py_platsitedir}/alsaaudio.so
%{py_platsitedir}/%{fname}-%{version}-py%{pyver}.egg-info
