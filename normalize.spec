Summary:	A WAV file volume adjuster
Summary(pl):	Korektor poziomu g�o�no�ci w plikach WAV
Name:		normalize
Version:	0.5.1
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Source0:	http://www.cs.columbia.edu/~cvaill/normalize/%{name}-%{version}.tar.gz
BuildRequires:	gettext-devel
URL:		http://www.cs.columbia.edu/~cvaill/normalize/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Normalize is a tool for adjusting the volume of WAV files to a
standard volume level. This is useful for things like creating mix CDs
and MP3 databases, where different recording levels on different
albums can cause the volume to vary greatly from song to song.

%description -l pl
Normalize jest narz�dziem do ustawiania poziomu g�o�no�ci w plikach
WAV przez dostosowanie go do standardowej warto�ci. Jest to przydatne
w sytuacjach takich jak tworzenie sk�adankowych p�yt CD oraz zbior�w
MP3, gdzie r�ne poziomy nagrywania na r�nych albumach mog�
spowodowa�, �e poziom g�o�no�ci r�ni si� do�� istotnie pomi�dzy
poszczeg�lnymi utworami.

%prep
%setup  -q

%build
gettextize --copy --force
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

mv -f $RPM_BUILD_ROOT%{_bindir}/normalize-mp3 .

gzip -9nf README ChangeLog NEWS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz normalize-mp3
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
