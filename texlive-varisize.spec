Name:		texlive-varisize
Version:	15878
Release:	1
Summary:	Change font size in Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/varisize
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/varisize.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/varisize.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A series of files, each of which defines a size-change macro.
Note that 10point.tex is by convention called by one of the
other files, so that there's always a "way back".

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/varisize/10point.tex
%{_texmfdistdir}/tex/plain/varisize/10pointss.tex
%{_texmfdistdir}/tex/plain/varisize/11point.tex
%{_texmfdistdir}/tex/plain/varisize/12point.tex
%{_texmfdistdir}/tex/plain/varisize/14point.tex
%{_texmfdistdir}/tex/plain/varisize/17point.tex
%{_texmfdistdir}/tex/plain/varisize/20point.tex
%{_texmfdistdir}/tex/plain/varisize/7point.tex
%{_texmfdistdir}/tex/plain/varisize/8point.tex
%{_texmfdistdir}/tex/plain/varisize/9point.tex
%doc %{_texmfdistdir}/doc/plain/varisize/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
