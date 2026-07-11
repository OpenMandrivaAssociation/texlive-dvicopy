%global tl_name dvicopy
%global tl_revision 77830

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Copy DVI files while expanding VF (virtual font) references
Group:		Publishing
URL:		https://www.ctan.org/pkg/dvicopy
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvicopy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvicopy.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(dvicopy.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
DVIcopy is a utility program that allows one to convert a DVI file that
references composite fonts (VF) into an equivalent DVI file that does
not contain such references. It also serves as a basis for writing DVI
drivers (much like DVItype). The ODVIcopy variant does the same job for
Omega/Aleph's output, modified to support their .ofm font format.

