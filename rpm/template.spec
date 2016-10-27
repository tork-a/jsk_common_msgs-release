Name:           ros-indigo-jsk-common-msgs
Version:        4.1.0
Release:        0%{?dist}
Summary:        ROS jsk_common_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_common_msgs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-jsk-footstep-msgs
Requires:       ros-indigo-jsk-gui-msgs
Requires:       ros-indigo-jsk-hark-msgs
Requires:       ros-indigo-posedetection-msgs
Requires:       ros-indigo-speech-recognition-msgs
BuildRequires:  ros-indigo-catkin

%description
Metapackage that contains commonly used messages for jsk-ros-pkg

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Oct 27 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 4.1.0-0
- Autogenerated by Bloom

* Wed Sep 21 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 4.0.0-0
- Autogenerated by Bloom

* Sat Jun 18 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.0.0-0
- Autogenerated by Bloom

* Sun Jan 24 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.0-0
- Autogenerated by Bloom

