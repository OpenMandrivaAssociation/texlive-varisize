%global tl_name varisize
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Change font size in Plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/varisize
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/varisize.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/varisize.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A series of files, each of which defines a size-change macro. Note that
10point.tex is by convention called by one of the other files, so that
there's always a "way back".

