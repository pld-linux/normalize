Summary:	A WAV and MP3 file volume adjuster
Summary(pl):	Korektor poziomu g³o¶no¶ci w plikach WAV i MP3
Name:		normalize
Version:	0.7.6
Release:	3
License:	GPL
Group:		Applications/Sound
Source0:	http://www.cs.columbia.edu/~cvaill/normalize/%{name}-%{version}.tar.bz2
# Source0-md5: 7476f028304791595e91610bb0cd4e97
BuildRequires:	gettext-devel
BuildRequires:	mad-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
URL:		http://www.cs.columbia.edu/~cvaill/normalize/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{xmms_effect_plugindir}

%description
Normalize is an overly complicated tool for adjusting the volume of
wave files to a standard level.  This is useful for things like
creating mixed CD's and mp3 collections, where different recording
levels on different albums can cause the volume to vary greatly from
song to song.
You can also adjust the volume of mp3 files without reencoding, but it
requires player with support for RVA2 (Relative Volume Adjustment)
ID3v2 frame. Plugin for xmms is available.

%description -l pl
Normalize jest narzêdziem do ustawiania poziomu g³o¶no¶ci w plikach
WAV przez dostosowanie go do standardowej warto¶ci. Jest to przydatne
w sytuacjach takich jak tworzenie sk³adankowych p³yt CD oraz zbiorów
MP3, gdzie ró¿ne poziomy nagrywania na ró¿nych albumach mog±
spowodowaæ, ¿e poziom g³o¶no¶ci ró¿ni siê do¶æ istotnie pomiêdzy
poszczególnymi utworami.
Jesli masz odtwarzacz mp3 korzystaj±cy z ramek RVA2 w tagach ID3v2, to
mo¿esz równie¿ normalizowaæ pliki mp3 bez konieczno¶ci ponownego
skompresowania pliku.

%package -n xmms-effect-rva
Summary:	RVA2 (Relative Volume Adjustment) ID3v2 frame support
Summary(pl):	Obs³uga ramek RVA2 tagów ID3v2
Group:		X11/Applications/Sound
Requires:	xmms

%description -n xmms-effect-rva
Plugin for xmms that supports volume adjustment frames (RVA2 ID3v2
frames).

%description -n xmms-effect-rva -l pl
Wtyczka dla xmms-a zapewniaj±ca obs³ugê zawartych w pliku mp3
informacji o dostrojeniu g³o¶no¶ci (ramki RVA2 w tagach ID3v2).

%prep
%setup  -q

%build
%configure \
	--with-mad \
	--enable-xmms \
	--with-xmms-prefix=%{xmms_prefix} \
	--without-audiofile \
	--disable-audiofiletest

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/normalize-mp3 .

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS TODO normalize-mp3
%attr(755,root,root) %{_bindir}/normalize
%{_mandir}/man1/*

%files -n xmms-effect-rva
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
