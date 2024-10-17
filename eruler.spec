%define git	20150506

Epoch:	1
Summary: 	Enlightened ruler
Name: 		eruler
Version:	0.1.0
Release:	1.%{git}.1
License:	BSD
Group:		Video
URL:		https://www.enlightenment.org/
Source0:	%{name}-%{git}.tar.xz

BuildRequires:	edje
BuildRequires:	evas
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(elementary)

%description
ERuler is a piece of software that allows on-screen virtual rule and
measurement of areas.

This is a WORK IN PROGRESS - it is NOT COMPLETE. do not expect everything to
work and do what you want.

%prep
%setup -qn %{name}-%{git}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS README 
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_iconsdir}/%name.png
