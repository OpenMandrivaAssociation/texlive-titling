%global tl_name titling
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1d
Release:	%{tl_revision}.1
Summary:	Control over the typesetting of the \maketitle command
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/titling
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/titling.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/titling.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/titling.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The titling package provides control over the typesetting of the
\maketitle command and \thanks commands, and makes the \title, \author
and \date information permanently available. Multiple titles are allowed
in a single document. New titling elements can be added and a titlepage
title can be centered on a physical page.

