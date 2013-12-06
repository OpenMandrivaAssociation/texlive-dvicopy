# revision 29764
# category TLCore
# catalog-ctan /dviware/dvicopy/dvicopy.web
# catalog-date 2012-04-10 15:00:16 +0200
# catalog-license gpl
# catalog-version 1.5
Name:		texlive-dvicopy
Version:	1.5
Release:	4
Summary:	Copy DVI files, flattening VFs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dvicopy/dvicopy.web
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvicopy.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvicopy.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-dvicopy.bin

%description
DVICOPY is a utility program that allows one to take a DVI file
that references composite fonts (VF) and convert it into a DVI
file that does not contain such references. It also serves as a
basis for writing DVI drivers (much like DVItype).

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/dvicopy.1*
%doc %{_texmfdistdir}/doc/man/man1/dvicopy.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
