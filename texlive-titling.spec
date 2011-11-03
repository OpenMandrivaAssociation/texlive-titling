# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/titling
# catalog-date 2009-09-04 12:14:45 +0200
# catalog-license lppl
# catalog-version 2.1d
Name:		texlive-titling
Version:	2.1d
Release:	1
Summary:	Control over the typesetting of the \maketitle command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/titling
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titling.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titling.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titling.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The titling package provides control over the typesetting of
the \maketitle command and \thanks commands, and makes the
\title, \author and \date information permanently available.
Multiple titles are allowed in a single document. New titling
elements can be added and a titlepage title can be centered on
a physical page.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/titling/titling.sty
%doc %{_texmfdistdir}/doc/latex/titling/README
%doc %{_texmfdistdir}/doc/latex/titling/titling.pdf
#- source
%doc %{_texmfdistdir}/source/latex/titling/titling.dtx
%doc %{_texmfdistdir}/source/latex/titling/titling.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
