#specfile originally created for Fedora, modified for Moblin Linux
%define _sbindir /sbin
#define _libdir /%{_lib}

Summary: The GNU disk partition manipulation program
Name:    parted
Version: 3.0
Release: 1
License: GPLv3+
Group:   Applications/System
URL:     http://www.gnu.org/software/parted

Source0: ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

BuildRequires: e2fsprogs-devel
BuildRequires: libuuid-devel
BuildRequires: readline-devel
BuildRequires: ncurses-devel
BuildRequires: libtool
BuildRequires: gettext-devel
BuildRequires: texinfo

Requires(post): /sbin/ldconfig
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
Requires(postun): /sbin/ldconfig

%description
The GNU Parted program allows you to create, destroy, resize, move,
and copy hard disk partitions. Parted can be used for creating space
for new operating systems, reorganizing disk usage, and copying data
to new hard disks.

%package devel
Summary:  Files for developing apps which will manipulate disk partitions
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The GNU Parted library is a set of routines for hard disk partition
manipulation. If you want to develop programs that manipulate disk
partitions and filesystems using the routines provided by the GNU
Parted library, you need to install this package.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static --disable-device-mapper --with-readline --with-libdir=%{_libdir} --exec-prefix=/usr
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp COPYING %{buildroot}/usr/share/license/%{name}
%make_install

# Remove components we do not ship
%{__rm} -rf %{buildroot}%{_infodir}/dir
#%{__rm} -rf %{buildroot}%{_bindir}/label
#%{__rm} -rf %{buildroot}%{_bindir}/disk

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%lang_package

%docs_package

%files 
%defattr(-,root,root,-)
%doc COPYING
%{_sbindir}/parted
%{_sbindir}/partprobe
%{_libdir}/libparted*.so.*
/usr/share/license/%{name}

%files devel
%defattr(-,root,root,-)
%{_includedir}/parted
%{_libdir}/libparted.so
%{_libdir}/pkgconfig/libparted.pc

