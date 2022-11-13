Name:		texlive-titling
Version:	15878
Release:	1
Summary:	Control over the typesetting of the \maketitle command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/titling
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titling.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titling.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titling.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The titling package provides control over the typesetting of
the \maketitle command and \thanks commands, and makes the
\title, \author and \date information permanently available.
Multiple titles are allowed in a single document. New titling
elements can be added and a titlepage title can be centered on
a physical page.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/titling/titling.sty
%doc %{_texmfdistdir}/doc/latex/titling/README
%doc %{_texmfdistdir}/doc/latex/titling/titling.pdf
#- source
%doc %{_texmfdistdir}/source/latex/titling/titling.dtx
%doc %{_texmfdistdir}/source/latex/titling/titling.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
