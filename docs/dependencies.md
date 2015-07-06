libtasn1-4.5-----------------------------------------------------------------------------------3-DEPS-----*
     bison                              bison-2.4.1-5.8.amzn1.x86_64                           AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     valgrind                           valgrind-3.9.0-6.13.amzn1.x86_64                       AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libtasn1.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libtasn1.spec
     ------------------------------------------------------------------------------------------------
     Install in next step


p11-kit-0.23.1---------------------------------------------------------------------------------4-DEPS-----*
     libtasn1-devel                     libtasn1-devel-2.3-6.6.amzn1.x86_64                    AMAZON
     nss-softokn-freebl                 nss-softokn-freebl-3.16.2.3-1.13.amzn1.x86_64          AMAZON
     libffi-devel                       libffi-devel-3.0.13-11.4.amzn1.x86_64                  AMAZON
     gtk-doc                            gtk-doc-1.19-2.11.amzn1.noarch                         AMAZON
     ------------------------------------------------------------------------------------------------
     Requires libtasn1 to be force installed in order to build, pre-built rpms provided
     ------------------------------------------------------------------------------------------------
     Install pre-built rpms together with libtasn1 to overcome AWS p11 dependency
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libtasn1-4.5-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libtasn1-devel-4.5-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/p11-kit-0.23.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/p11-kit-devel-0.23.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/p11-kit-trust-0.23.1-1.amzn1.x86_64.rpm


fontconfig-2.11.94-----------------------------------------------------------------------------3-DEPS-----*
     expat-devel                        expat-devel-2.1.0-8.18.amzn1.x86_64                    AMAZON
     freetype-devel                     freetype-devel-2.3.11-15.14.amzn1.x86_64               AMAZON
     fontpackages-devel                 fontpackages-devel-1.41-1.1.2.amzn1.noarch             AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/fontconfig.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/fontconfig.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/fontconfig-2.11.94-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/fontconfig-devel-2.11.94-1.amzn1.x86_64.rpm


libdrm-2.4.61----------------------------------------------------------------------------------13DEPS-----*
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     kernel-headers                     kernel-headers-3.14.42-31.38.amzn1.x86_64              AMAZON
     libxcb-devel                       libxcb-devel-1.8.1-1.18.amzn1.x86_64                   AMAZON
     libudev-devel                      libudev-devel-173-4.13.amzn1.x86_64                    AMAZON
     libatomic_ops-devel                libatomic_ops-devel-1.2-8.gc.1.6.amzn1.x86_64          AMAZON
     libpciaccess-devel                 libpciaccess-devel-0.13.1-4.1.11.amzn1.x86_64          AMAZON
     libxslt                            libxslt-1.1.28-5.12.amzn1.x86_64                       AMAZON
     docbook-style-xsl                  docbook-style-xsl-1.78.1-3.9.amzn1.noarch              AMAZON
     valgrind-devel                     valgrind-devel-3.9.0-6.13.amzn1.x86_64                 AMAZON
     xorg-x11-util-macros               xorg-x11-util-macros-1.17-2.6.amzn1.noarch             AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libdrm.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libdrm.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libdrm-2.4.61-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libdrm-devel-2.4.61-1.amzn1.x86_64.rpm


gl-manpages-1.1.1------------------------------------------------------------------------------2-DEPS-----*
     libxslt                            libxslt-1.1.28-5.12.amzn1.x86_64                       AMAZON
     docbook-style-xsl                  docbook-style-xsl-1.78.1-3.9.amzn1.noarch              AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/gl-manpages.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/gl-manpages.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/noarch/gl-manpages-1.1-1.amzn1.noarch.rpm


libxshmfence-1.2-------------------------------------------------------------------------------5-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     xorg-x11-proto-devel               xorg-x11-proto-devel-7.7-9.10.amzn1.noarch             AMAZON
     xorg-x11-util-macros               xorg-x11-util-macros-1.17-2.6.amzn1.noarch             AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libxshmfence.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libxshmfence.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libxshmfence-devel-1.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libxshmfence-1.2-1.amzn1.x86_64.rpm


opencl-headers-1.2-----------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/opencl-headers.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/opencl-headers.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/noarch/opencl-headers-1.2-1.amzn1.noarch.rpm


opencl-filesystem-1.0--------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/opencl-filesystem.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/opencl-filesystem.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/noarch/opencl-filesystem-1.0-1.amzn1.noarch.rpm


libclc-0.0.1-----------------------------------------------------------------------------------6-DEPS-----*
     clang-devel                        clang-devel-3.5.1-1.7.amzn1.x86_64                     AMAZON
     libedit-devel                      libedit-devel-2.11-4.20080712cvs.1.6.amzn1.x86_64      AMAZON
     llvm-devel                         llvm-devel-3.5.1-1.7.amzn1.x86_64                      AMAZON
     llvm-static                        llvm-static-3.5.1-1.7.amzn1.x86_64                     AMAZON
     python27                           python27-2.7.9-4.115.amzn1.x86_64                      AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libclc.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libclc.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libclc-0.0.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libclc-devel-0.0.1-1.amzn1.x86_64.rpm


mesa-10.6.0------------------------------------------------------------------------------------28DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     bison                              bison-2.4.1-5.8.amzn1.x86_64                           AMAZON
     elfutils                           elfutils-0.158-3.16.amzn1.x86_64                       AMAZON
     elfutils-libelf-devel              elfutils-libelf-devel-0.158-3.16.amzn1.x86_64          AMAZON
     expat-devel                        expat-devel-2.1.0-8.18.amzn1.x86_64                    AMAZON
     flex                               flex-2.5.36-1.8.amzn1.x86_64                           AMAZON
     gettext                            gettext-0.18.1.1-9.1.11.amzn1.x86_64                   AMAZON
     git                                git-2.1.0-1.38.amzn1.x86_64                            AMAZON
     libdrm-devel                       libdrm-devel-2.4.61-3.amzn1.x86_64.rpm                 LBUILD
     libselinux-devel                   libselinux-devel-2.1.10-3.22.amzn1.x86_64              AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     libudev-devel                      libudev-devel-173-4.13.amzn1.x86_64                    AMAZON
     libXdamage-devel                   libXdamage-devel-1.1.3-4.7.amzn1.x86_64                AMAZON
     libXext-devel                      libXext-devel-1.3.2-2.1.10.amzn1.x86_64                AMAZON
     libXfixes-devel                    libXfixes-devel-5.0.1-2.1.8.amzn1.x86_64               AMAZON
     libXi-devel                        libXi-devel-1.7.2-2.2.9.amzn1.x86_64                   AMAZON
     libxml2-python27                   libxml2-python27-2.9.1-3.1.35.amzn1.x86_64             AMAZON
     libXmu-devel                       libXmu-devel-1.1.1-2.8.amzn1.x86_64                    AMAZON
     libxshmfence-devel                 libxshmfence-devel-1.2-1.amzn1.x86_64.rpm              LBUILD
     libXxf86vm-devel                   libXxf86vm-devel-1.1.3-2.1.9.amzn1.x86_64              AMAZON
     imake                              imake-1.0.2-11.7.amzn1.x86_64                          AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     python27                           python27-2.7.9-4.115.amzn1.x86_64                      AMAZON
     python27-mako                      python27-mako-0.8.1-2.8.amzn1.noarch                   AMAZON
     xorg-x11-proto-devel               xorg-x11-proto-devel-7.7-9.10.amzn1.noarch             AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     gl-manpages                        gl-manpages-1.1-9.20140424.amzn1.noarch.rpm            LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/mesa.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/mesa.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mesa-libGL-10.6.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mesa-dri-drivers-10.6.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mesa-filesystem-10.6.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mesa-libglapi-10.6.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mesa-libGL-devel-10.6.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mesa-libEGL-10.6.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mesa-libEGL-devel-10.6.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mesa-libgbm-10.6.0-1.amzn1.x86_64.rpm


mesa-libGLU-10.6.0-----------------------------------------------------------------------------4-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     mesa-libGL-devel                   mesa-libGL-devel-10.6.0-1.amzn1.x86_64.rpm             LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/mesa-libGLU.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/mesa-libGLU.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mesa-libGLU-10.6.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mesa-libGLU-devel-10.6.0-1.amzn1.x86_64.rpm


glew-1.10.0------------------------------------------------------------------------------------1-DEPS-----*
     mesa-libGLU-devel                  mesa-libGLU-devel-10.6.0-1.amzn1.x86_64.rpm            LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/glew.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/glew.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/glew-1.10.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/glew-devel-1.10.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libGLEW-1.10.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libGLEWmx-1.10.0-1.amzn1.x86_64.rpm


mesa-demos-10.6.0------------------------------------------------------------------------------8-DEPS-----*
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     freeglut-devel                     freeglut-devel-2.6.0-1.8.amzn1.x86_64                  AMAZON
     mesa-libGL-devel                   mesa-libGL-devel-10.6.0-1.amzn1.x86_64.rpm             LBUILD
     mesa-libGLU-devel                  mesa-libGLU-devel-9.0.0-1.amzn1.x86_64.rpm             LBUILD
     glew-devel                         glew-devel-1.10.0-1.amzn1.x86_64.rpm                   LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/mesa-demos.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/mesa-demos.spec
     ------------------------------------------------------------------------------------------------
     ***** Building for consistency, does not require installation
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mesa-demos-10.6.0-1.amzn1.x86_64.rpm


libpng12-1.2.50--------------------------------------------------------------------------------2-DEPS-----*
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libpng12.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libpng12.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libpng12-1.2.50-1.amzn1.x86_64.rpm


libpng-1.6.17----------------------------------------------------------------------------------4-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libpng.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libpng.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libpng-1.6.17-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libpng-devel-1.6.17-1.amzn1.x86_64.rpm


cairo-1.14.2-----------------------------------------------------------------------------------9-DEPS-----*
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     libxml12                           libxml2-devel-2.9.1-3.1.35.amzn1.x86_64                AMAZON
     pixman-devel                       pixman-devel-0.32.4-4.11.amzn1.x86_64                  AMAZON
     freetype-devel                     freetype-devel-2.3.11-15.14.amzn1.x86_64               AMAZON
     fontconfig                         fontconfig-devel-2.11.94-1.amzn1.x86_64.rpm            LBUILD
     glib2-devel                        glib2-devel-2.36.3-5.18.amzn1.x86_64                   AMAZON
     libpng                             libpng-devel-1.6.17-1.amzn1.x86_64.rpm                 LBUILD
     mesa-libGL-devel                   mesa-libGL-devel-10.6.0-1.amzn1.x86_64.rpm             LBUILD
     mesa-libEGL-devel                  mesa-libEGL-devel-10.6.0-1.amzn1.x86_64.rpm            LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/cairo.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/cairo.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/cairo-1.14.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/cairo-devel-1.14.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/cairo-gobject-1.14.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/cairo-gobject-devel-1.14.2-1.amzn1.x86_64.rpm


autoconf-archive-2015.02.24--------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/autoconf-archive.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/autoconf-archive.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/noarch/autoconf-archive-2015.02.24-1.amzn1.noarch.rpm


gnome-common-3.14.0----------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/gnome-common.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/gnome-common.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/noarch/gnome-common-3.14.0-1.amzn1.noarch.rpm


pango-1.34.1-----------------------------------------------------------------------------------14DEPS-----*
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     cairo-devel                        cairo-devel-1.14.2-1.amzn1.x86_64                      LBUILD
     freetype-devel                     freetype-devel-2.3.11-15.14.amzn1.x86_64               AMAZON
     glib2-devel                        glib2-devel-2.36.3-5.18.amzn1.x86_64                   AMAZON
     fontconfig                         fontconfig-devel-2.11.94-1.amzn1.x86_64.rpm            LBUILD
     harfbuzz-devel                     harfbuzz-devel-0.9.20-3.5.amzn1.x86_64                 AMAZON
     libthai-devel                      libthai-devel-0.1.12-3.5.amzn1.x86_64                  AMAZON
     libXft-devel                       libXft-devel-2.3.1-2.7.amzn1.x86_64                    AMAZON
     gobject-introspection-devel        gobject-introspection-devel-1.36.0-4.9.amzn1.x86_64    AMAZON
     cairo-gobject-devel                cairo-gobject-devel-1.14.2-1.amzn1.x86_64              LBUILD
     gnome-common                       gnome-common-3.14.0-1.amzn1.noarch.rpm                 LBUILD
     intltool                           intltool-0.41.0-1.1.5.amzn1.noarch                     AMAZON
     gtk-doc                            gtk-doc-1.19-2.11.amzn1.noarch                         AMAZON
     help2man                           help2man-1.41.1-2.8.amzn1.noarch                       AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/pango.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/pango.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/pango-1.34.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/pango-devel-1.34.1-1.amzn1.x86_64.rpm


libjpeg-turbo-1.4.1----------------------------------------------------------------------------4-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     nasm                               nasm-2.10.07-7.7.amzn1.x86_64                          AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libjpeg-turbo.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libjpeg-turbo.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libjpeg-turbo-1.4.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libjpeg-turbo-devel-1.4.1-1.amzn1.x86_64.rpm


gdk-pixbuf2-2.28.2-----------------------------------------------------------------------------13DEPS-----*
     glib2-devel                        glib2-devel-2.36.3-5.18.amzn1.x86_64                   AMAZON
     libpng                             libpng-devel-1.6.17-1.amzn1.x86_64.rpm                 LBUILD
     libjpeg-turbo-devel                libjpeg-turbo-devel-1.4.1-1.amzn1.x86_64               LBUILD
     libtiff-devel                      libtiff-devel-4.0.3-20.20.amzn1.x86_64                 AMAZON
     jasper-devel                       jasper-devel-1.900.1-16.9.amzn1.x86_64                 AMAZON
     libX11-devel                       libX11-devel-1.6.0-2.2.12.amzn1.x86_64                 AMAZON
     gobject-introspection-devel        gobject-introspection-devel-1.36.0-4.9.amzn1.x86_64    AMAZON
     shared-mime-info                   shared-mime-info-1.1-7.7.amzn1.x86_64                  AMAZON
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     gtk-doc                            gtk-doc-1.19-2.11.amzn1.noarch                         AMAZON
     gettext-devel                      gettext-devel-0.18.1.1-9.1.11.amzn1.x86_64             AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/gdk-pixbuf2.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/gdk-pixbuf2.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gdk-pixbuf2-2.28.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gdk-pixbuf2-devel-2.28.2-1.amzn1.x86_64.rpm


libcroco-0.6.8---------------------------------------------------------------------------------3-DEPS-----*
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     glib2-devel                        glib2-devel-2.36.3-5.18.amzn1.x86_64                   AMAZON
     libxml12                           libxml2-devel-2.9.1-3.1.35.amzn1.x86_64                AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libcroco.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libcroco.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libcroco-0.6.8-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libcroco-devel-0.6.8-1.amzn1.x86_64.rpm


librsvg2-2.40.9--------------------------------------------------------------------------------7-DEPS-----*
     cairo-devel                        cairo-devel-1.14.2-1.amzn1.x86_64.rpm                  AMAZON
     glib2-devel                        glib2-devel-2.36.3-5.18.amzn1.x86_64                   AMAZON
     gobject-introspection-devel        gobject-introspection-devel-1.36.0-4.9.amzn1.x86_64    AMAZON
     libxml12                           libxml2-devel-2.9.1-3.1.35.amzn1.x86_64                AMAZON
     pango-devel                        pango-devel-1.34.1-1.amzn1.x86_64.rpm                  LBUILD
     gdk-pixbuf2                        gdk-pixbuf2-devel-2.28.2-1.amzn1.x86_64.rpm            LBUILD
     libcroco                           libcroco-devel-0.6.8-1.amzn1.x86_64.rpm                LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/librsvg2.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/librsvg2.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/librsvg2-2.40.9-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/librsvg2-devel-2.40.9-1.amzn1.x86_64.rpm


lcms2-2.7--------------------------------------------------------------------------------------3-DEPS-----*
     libjpeg-turbo-devel                libjpeg-turbo-devel-1.4.1-1.amzn1.x86_64               LBUILD
     libtiff-devel                      libtiff-devel-4.0.3-20.20.amzn1.x86_64                 AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/lcms2.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/lcms2.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/lcms2-devel-2.7-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/lcms2-2.7-1.amzn1.x86_64.rpm


nettle-3.1.1-----------------------------------------------------------------------------------4-DEPS-----*
     gmp                                gmp-devel-4.3.2-1.11.amzn1.x86_64                      AMAZON
     m4                                 m4-1.4.16-9.10.amzn1.x86_64                            AMAZON
     texinfo-tex                        texinfo-tex-5.1-4.10.amzn1.x86_64                      AMAZON
     texlive-dvips                      texlive-dvips-svn29585.0-27.21.amzn1.noarch            AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/nettle.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/nettle.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/nettle-3.1.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/nettle-devel-3.1.1-1.amzn1.x86_64.rpm

trousers-0.3.13--------------------------------------------------------------------------------4-DEPS-----*
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     openssl-devel                      openssl-devel-1.0.1k-1.84.amzn1.x86_64                 AMAZON
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/trousers.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/trousers.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/trousers-0.3.13-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/trousers-devel-0.3.13-1.amzn1.x86_64.rpm


unbound-1.5.1----------------------------------------------------------------------------------6-DEPS-----*
     flex                               flex-2.5.36-1.8.amzn1.x86_64                           AMAZON
     openssl-devel                      openssl-devel-1.0.1k-1.84.amzn1.x86_64                 AMAZON
     libevent-devel                     libevent-devel-2.0.18-1.11.amzn1.x86_64                AMAZON
     expat-devel                        expat-devel-2.1.0-8.18.amzn1.x86_64                    AMAZON
     python27-devel                     python26-devel-2.6.9-1.80.amzn1.x86_64                 AMAZON
     swig                               swig-2.0.10-4.24.amzn1.x86_64                          AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/unbound.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/unbound.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/unbound-1.5.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/unbound-devel-1.5.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/unbound-libs-1.5.1-1.amzn1.x86_64.rpm


gnutls-3.4.2-----------------------------------------------------------------------------------18DEPS-----*
     gettext                            gettext-0.18.1.1-9.1.11.amzn1.x86_64                   AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     readline-devel                     readline-devel-6.2-9.14.amzn1.x86_64                   AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     texinfo                            texinfo-5.1-4.10.amzn1.x86_64                          AMAZON
     autogen-libopts-devel              autogen-libopts-devel-5.18-5.4.amzn1.x86_64            AMAZON
     autogen                            autogen-5.18-5.4.amzn1.x86_64                          AMAZON
     libidn-devel                       libidn-devel-1.18-2.8.amzn1.x86_64                     AMAZON
     gperf                              gperf-3.0.3-9.1.6.amzn1.x86_64                         AMAZON
     guile-devel                        guile-devel-1.8.7-5.7.amzn1.x86_64                     AMAZON
     libtasn1-devel                     libtasn1-devel-4.5-1.amzn1.x86_64.rpm                  LBUILD
     nettle-devel                       nettle-devel-3.1.1-1.amzn1.x86_64.rpm                  LBUILD
     p11-kit-devel                      p11-kit-devel-0.23.1-1.amzn1.x86_64.rpm                LBUILD
     trousers-devel                     trousers-devel-0.3.13-1.amzn1.x86_64.rpm               LBUILD
     unbound-devel                      unbound-devel-1.5.1-1.amzn1.x86_64.rpm                 LBUILD
     unbound-libs                       unbound-libs-1.5.1-1.amzn1.x86_64.rpm                  LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/gnutls.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/gnutls.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gnutls-3.4.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gnutls-devel-3.4.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gnutls-c++-3.4.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gnutls-dane-3.4.2-1.amzn1.x86_64.rpm


audiofile-0.3.6--------------------------------------------------------------------------------2-DEPS-----*
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     alsa-lib-devel                     alsa-lib-devel-1.0.22-3.9.amzn1.x86_64                 AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/audiofile.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/audiofile.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/audiofile-0.3.6-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/audiofile-devel-0.3.6-1.amzn1.x86_64.rpm


fftw-3.3.4-------------------------------------------------------------------------------------3-DEPS-----*
     gcc48-gfortran                     gcc48-gfortran-4.8.2-16.2.99.amzn1.x86_64              AMAZON
     time                               time-1.7-38.9.amzn1.x86_64                             AMAZON
     perl                               perl-5.16.3-283.37.amzn1.x86_64                        AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/fftw.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/fftw.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/fftw-3.3.4-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/fftw-libs-3.3.4-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/fftw-devel-3.3.4-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/fftw-libs-double-3.3.4-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/fftw-libs-single-3.3.4-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/fftw-libs-long-3.3.4-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/fftw-libs-quad-3.3.4-1.amzn1.x86_64.rpm


autoconf213-2.13-------------------------------------------------------------------------------6-DEPS-----*
     texinfo                            texinfo-5.1-4.10.amzn1.x86_64                          AMAZON
     m4                                 m4-1.4.16-9.10.amzn1.x86_64                            AMAZON
     perl                               perl-5.16.3-283.37.amzn1.x86_64                        AMAZON
     gawk                               gawk-3.1.7-10.10.amzn1.x86_64                          AMAZON
     dejagnu                            dejagnu-1.4.4-17.5.amzn1.noarch                        AMAZON
     flex                               flex-2.5.36-1.8.amzn1.x86_64                           AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/autoconf213.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/autoconf213.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/noarch/autoconf213-2.13-1.amzn1.noarch.rpm


mozjs17-17.0.0---------------------------------------------------------------------------------6-DEPS-----*
     nspr-devel                         nspr-devel-4.10.6-1.28.amzn1.x86_64                    AMAZON
     readline-devel                     readline-devel-6.2-9.14.amzn1.x86_64                   AMAZON
     zip                                zip-3.0-1.10.amzn1.x86_64                              AMAZON
     python27                           python27-2.7.9-4.115.amzn1.x86_64                      AMAZON
     autoconf213                        autoconf213-2.13-1.amzn1.noarch.rpm                    LBUILD
     clang                              clang-3.5.1-1.7.amzn1.x86_64                           AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/mozjs17.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/mozjs17.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mozjs17-17.0.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mozjs17-devel-17.0.0-1.amzn1.x86_64.rpm


polkit-0.112-----------------------------------------------------------------------------------8-DEPS-----*
     glib2-devel                        glib2-devel-2.36.3-5.18.amzn1.x86_64                   AMAZON
     expat-devel                        expat-devel-2.1.0-8.18.amzn1.x86_64                    AMAZON
     pam-devel                          pam-devel-1.1.8-9.31.amzn1.x86_64                      AMAZON
     gtk-doc                            gtk-doc-1.19-2.11.amzn1.noarch                         AMAZON
     intltool                           intltool-0.41.0-1.1.5.amzn1.noarch                     AMAZON
     gobject-introspection-devel        gobject-introspection-devel-1.36.0-4.9.amzn1.x86_64    AMAZON
     mozjs17-devel                      mozjs17-devel-17.0.0-8.amzn1.x86_64.rpm                LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/polkit.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/polkit.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/polkit-0.112-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/polkit-devel-0.112-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/noarch/polkit-docs-0.112-1.amzn1.noarch.rpm


GConf2-3.2.6-----------------------------------------------------------------------------------16DEPS-----*
     libxml2-devel                      libxml2-devel-2.9.1-3.1.35.amzn1.x86_64                AMAZON
     libxslt-devel                      libxslt-devel-1.1.28-5.12.amzn1.x86_64                 AMAZON
     libgcrypt-devel                    libgcrypt-devel-1.5.3-4.15.amzn1.x86_64                AMAZON
     libgpg-error-devel                 libgpg-error-devel-1.11-1.12.amzn1.x86_64              AMAZON
     xz-devel                           xz-devel-5.1.2-8alpha.11.amzn1.x86_64                  AMAZON
     glib2-devel                        glib2-devel-2.36.3-5.18.amzn1.x86_64                   AMAZON
     gtk-doc                            gtk-doc-1.19-2.11.amzn1.noarch                         AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     gettext                            gettext-0.18.1.1-9.1.11.amzn1.x86_64                   AMAZON
     intltool                           intltool-0.41.0-1.1.5.amzn1.noarch                     AMAZON
     dbus-glib-devel                    dbus-glib-devel-0.86-6.10.amzn1.x86_64                 AMAZON
     gobject-introspection-devel        gobject-introspection-devel-1.36.0-4.9.amzn1.x86_64    AMAZON
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     polkit-devel                       polkit-devel-0.112-1.amzn1.x86_64.rpm                  LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/GConf2.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/GConf2.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/GConf2-3.2.6-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/GConf2-devel-3.2.6-1.amzn1.x86_64.rpm


libasyncns-0.8---------------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/libasyncns.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libasyncns.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libasyncns-0.8-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libasyncns-devel-0.8-1.amzn1.x86_64.rpm


bash-completion-2.1----------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/bash-completion.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/bash-completion.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install /home/ec2-user/rpmbuild/RPMS/noarch/bash-completion-2.1-1.amzn1.noarch.rpm


webrtc-audio-processing-0.1--------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/webrtc-audio-processing.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/webrtc-audio-processing.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/webrtc-audio-processing-0.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/webrtc-audio-processing-devel-0.1-1.amzn1.x86_64.rpm


libtdb-1.3.5-----------------------------------------------------------------------------------4-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     libxslt-devel                      libxslt-devel-1.1.28-5.12.amzn1.x86_64                 AMAZON
     docbook-style-xsl                  docbook-style-xsl-1.78.1-3.9.amzn1.noarch              AMAZON
     python27-devel                     python26-devel-2.6.9-1.80.amzn1.x86_64                 AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libtdb.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libtdb.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libtdb-1.3.5-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libtdb-devel-1.3.5-1.amzn1.x86_64.rpm


orc-0.4.23-------------------------------------------------------------------------------------2-DEPS-----*
     gtk-doc                            gtk-doc-1.19-2.11.amzn1.noarch                         AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/orc.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/orc.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/orc-0.4.23-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/orc-devel-0.4.23-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/orc-compiler-0.4.23-1.amzn1.x86_64.rpm


libogg-1.3.2-----------------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/libogg.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libogg.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libogg-1.3.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libogg-devel-1.3.2-1.amzn1.x86_64.rpm


flac-1.3.1-------------------------------------------------------------------------------------6-DEPS-----*
     libogg-devel                       libogg-devel-1.3.2-1.amzn1.x86_64                      LBUILD
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     gettext-devel                      gettext-devel-0.18.1.1-9.1.11.amzn1.x86_64             AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/flac.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/flac.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/flac-1.3.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/flac-libs-1.3.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/flac-devel-1.3.1-1.amzn1.x86_64.rpm


libvorbis-1.3.5--------------------------------------------------------------------------------1-DEPS-----*
     libogg-devel                       libogg-devel-1.3.2-1.amzn1.x86_64                      LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libvorbis.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libvorbis.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libvorbis-1.3.5-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libvorbis-devel-1.3.5-1.amzn1.x86_64.rpm


gsm-1.0.13-------------------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/gsm.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/gsm.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gsm-1.0.13-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gsm-devel-1.0.13-1.amzn1.x86_64.rpm


libsndfile-1.0.25------------------------------------------------------------------------------8-DEPS-----*
     alsa-lib-devel                     alsa-lib-devel-1.0.22-3.9.amzn1.x86_64                 AMAZON
     flac-devel                         flac-1.3.1-3.amzn1.x86_64.rpm                          LBUILD
     libogg-devel                       libogg-devel-1.3.2-1.amzn1.x86_64                      LBUILD
     libvorbis-devel                    libvorbis-devel-1.3.5-1.amzn1.x86_64                   LBUILD
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     sqlite-devel                       sqlite-devel-3.7.17-4.11.amzn1.x86_64                  AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     gsm-devel                          gsm-devel-1.0.13-11.amzn1.x86_64.rpm                   LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libsndfile.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libsndfile.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libsndfile-1.0.25-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libsndfile-devel-1.0.25-1.amzn1.x86_64.rpm


libsamplerate-0.1.8----------------------------------------------------------------------------2-DEPS-----*
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     libsndfile-devel                   libsndfile-devel-1.0.25-1.amzn1.x86_64.rpm             LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libsamplerate.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libsamplerate.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libsamplerate-0.1.8-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libsamplerate-devel-0.1.8-1.amzn1.x86_64.rpm


opus-1.1---------------------------------------------------------------------------------------1-DEPS-----*
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/opus.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/opus.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/opus-1.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/opus-devel-1.1-1.amzn1.x86_64.rpm


jack-audio-connection-kit-1.9.10---------------------------------------------------------------11DEPS-----*
     alsa-lib-devel                     alsa-lib-devel-1.0.22-3.9.amzn1.x86_64                 AMAZON
     dbus-devel                         dbus-devel-1.6.12-8.27.amzn1.x86_64                    AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     expat-devel                        expat-devel-2.1.0-8.18.amzn1.x86_64                    AMAZON
     libsamplerate-devel                libsamplerate-devel-0.1.8-6.amzn1.x86_64.rpm           LBUILD
     libsndfile-devel                   libsndfile-devel-1.0.25-1.amzn1.x86_64.rpm             LBUILD
     ncurses-devel                      ncurses-devel-5.7-3.20090208.13.amzn1.x86_64           AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     python26-devel                     python26-devel-2.6.9-1.80.amzn1.x86_64                 AMAZON
     readline-devel                     readline-devel-6.2-9.14.amzn1.x86_64                   AMAZON
     opus-devel                         opus-devel-1.1-1.amzn1.x86_64.rpm                      LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/jack-audio-connection-kit.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/jack-audio-connection-kit.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/jack-audio-connection-kit-1.9.10-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/jack-audio-connection-kit-devel-1.9.10-1.amzn1.x86_64.rpm


sbc-1.3----------------------------------------------------------------------------------------1-DEPS-----*
     libsndfile-devel                   libsndfile-devel-1.0.25-1.amzn1.x86_64.rpm             LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/sbc.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/sbc.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/sbc-1.3-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/sbc-devel-1.3-1.amzn1.x86_64.rpm


rtkit-0.5--------------------------------------------------------------------------------------3-DEPS-----*
     dbus-devel                         dbus-devel-1.6.12-8.27.amzn1.x86_64                    AMAZON
     libcap-devel                       libcap-devel-2.16-5.5.8.amzn1.x86_64                   AMAZON
     polkit-devel                       polkit-devel-0.112-1.amzn1.x86_64.rpm                  LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/rtkit.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/rtkit.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/rtkit-0.5-1.amzn1.x86_64.rpm


pulseaudio-6.0---------------------------------------------------------------------------------31DEPS-----*
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     m4                                 m4-1.4.16-9.10.amzn1.x86_64                            AMAZON
     libtool-ltdl-devel                 libtool-ltdl-devel-2.4.2-20.4.8.2.23.amzn1.x86_64      AMAZON
     intltool                           intltool-0.41.0-1.1.5.amzn1.noarch                     AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     xmltoman                           xmltoman-0.4-4.2.amzn1.noarch                          AMAZON
     tcp_wrappers-devel                 tcp_wrappers-devel-7.6-75.11.amzn1.x86_64              AMAZON
     alsa-lib-devel                     alsa-lib-devel-1.0.22-3.9.amzn1.x86_64                 AMAZON
     glib2-devel                        glib2-devel-2.36.3-5.18.amzn1.x86_64                   AMAZON
     avahi-devel                        avahi-devel-0.6.25-12.17.amzn1.x86_64                  AMAZON
     libatomic_ops-devel                libatomic_ops-devel-1.2-8.gc.1.6.amzn1.x86_64          AMAZON
     openssl-devel                      openssl-devel-1.0.1k-1.84.amzn1.x86_64                 AMAZON
     speex-devel                        speex-devel-1.2-0.12.rc1.1.7.amzn1.x86_64              AMAZON
     json-c-devel                       json-c-devel-0.11-6.8.amzn1.x86_64                     AMAZON
     dbus-devel                         dbus-devel-1.6.12-8.27.amzn1.x86_64                    AMAZON
     libcap-devel                       libcap-devel-2.16-5.5.8.amzn1.x86_64                   AMAZON
     check-devel                        check-devel-0.9.8-1.1.6.amzn1.x86_64                   AMAZON
     fftw-devel                         fftw-devel-3.3.4-1.amzn1.x86_64.rpm                    LBUILD
     GConf2-devel                       GConf2-devel-3.2.6-8.amzn1.x86_64.rpm                  LBUILD
     libasyncns-devel                   libasyncns-devel-0.8-1.amzn1.x86_64.rpm                LBUILD
     libsamplerate-devel                libsamplerate-devel-0.1.8-6.amzn1.x86_64.rpm           LBUILD
     libsndfile-devel                   libsndfile-devel-1.0.25-1.amzn1.x86_64.rpm             LBUILD
     libtdb-devel                       libtdb-devel-1.3.5-1.amzn1.x86_64.rpm                  LBUILD
     orc-devel                          orc-devel-0.4.23-1.amzn1.x86_64.rpm                    LBUILD
     pkgconfig(bash-completion)         bash-completion-2.1-1.amzn1.noarch.rpm                 LBUILD
     webrtc-audio-processing-devel      webrtc-audio-processing-devel-0.1-1.amzn1.x86_64.rpm   LBUILD
     jack-audio-connection-kit          jack-audio-connection-kit-devel-1.9.10-1.amzn1...      LBUILD
     sbc-devel                          sbc-devel-1.3-1.amzn1.x86_64.rpm                       LBUILD
     rtkit                              rtkit-0.5-1.amzn1.x86_64.rpm                           LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/pulseaudio.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/pulseaudio.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/pulseaudio-6.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/pulseaudio-libs-devel-6.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/pulseaudio-libs-6.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/pulseaudio-libs-glib2-6.0-1.amzn1.x86_64.rpm


SDL-1.2.15-------------------------------------------------------------------------------------9-DEPS-----*
     alsa-lib-devel                     alsa-lib-devel-1.0.22-3.9.amzn1.x86_64                 AMAZON
     dbus-devel                         dbus-devel-1.6.12-8.27.amzn1.x86_64                    AMAZON
     libusb-devel                       libusb-devel-0.1.12-23.9.amzn1.x86_64                  AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     nasm                               nasm-2.10.07-7.7.amzn1.x86_64                          AMAZON
     audiofile-devel                    audiofile-devel-0.3.6-1.amzn1.x86_64.rpm               LBUILD
     pulseaudio-libs-devel              pulseaudio-libs-devel-6.0-1.amzn1.x86_64.rpm           LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/SDL.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/SDL.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/SDL-1.2.15-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/SDL-devel-1.2.15-1.amzn1.x86_64.rpm


libva-1.5.1------------------------------------------------------------------------------------5-DEPS-----*
     libudev-devel                      libudev-devel-173-4.13.amzn1.x86_64                    AMAZON
     libXext-devel                      libXext-devel-1.3.2-2.1.10.amzn1.x86_64                AMAZON
     libXfixes-devel                    libXfixes-devel-5.0.1-2.1.8.amzn1.x86_64               AMAZON
     libdrm-devel                       libdrm-devel-2.4.61-1.amzn1.x86_64.rpm                 LBUILD
     libpciaccess-devel                 libpciaccess-devel-0.13.1-4.1.11.amzn1.x86_64          AMAZON
     mesa-dri-filesystem                mesa-filesystem-10.6.0-1.amzn1.x86_64.rpm              LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libva.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libva.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libva-1.5.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libva-devel-1.5.1-1.amzn1.x86_64.rpm


giflib4-4.1.6----------------------------------------------------------------------------------4-DEPS-----*
     libX11-devel                       libX11-devel-1.6.0-2.2.12.amzn1.x86_64                 AMAZON
     libICE-devel                       libICE-devel-1.0.6-1.4.amzn1.x86_64                    AMAZON
     libSM-devel                        libSM-devel-1.2.1-2.6.amzn1.x86_64                     AMAZON
     libXt-devel                        libXt-devel-1.1.4-6.1.9.amzn1.x86_64                   AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/giflib4.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/giflib4.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/giflib4-4.1.6-1.amzn1.x86_64.rpm
     

giflib-5.1.1-----------------------------------------------------------------------------------9-DEPS-----*
     libICE-devel                       libICE-devel-1.0.6-1.4.amzn1.x86_64                    AMAZON
     libSM-devel                        libSM-devel-1.2.1-2.6.amzn1.x86_64                     AMAZON
     libX11-devel                       libX11-devel-1.6.0-2.2.12.amzn1.x86_64                 AMAZON
     libXt-devel                        libXt-devel-1.1.4-6.1.9.amzn1.x86_64                   AMAZON
     giflib4                            giflib4-4.1.6-1.6.amzn1.x86_64.rpm                     LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/giflib.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/giflib.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/giflib-5.1.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/giflib-devel-5.1.1-1.amzn1.x86_64.rpm


libid3tag-0.15.1b------------------------------------------------------------------------------2-DEPS-----*
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libid3tag.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libid3tag.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libid3tag-0.15.1b-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libid3tag-devel-0.15.1b-1.amzn1.x86_64.rpm


imlib2-1.4.6-----------------------------------------------------------------------------------11DEPS-----*
     freetype-devel                     freetype-devel-2.3.11-15.14.amzn1.x86_64               AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     bzip2-devel                        bzip2-devel-1.0.6-8.12.amzn1.x86_64                    AMAZON
     libX11-devel                       libX11-devel-1.6.0-2.2.12.amzn1.x86_64                 AMAZON
     libXext-devel                      libXext-devel-1.3.2-2.1.10.amzn1.x86_64                AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     libjpeg-turbo-devel                libjpeg-turbo-devel-1.4.1-1.amzn1.x86_64               LBUILD
     libpng-devel                       libpng-devel-1.6.17-1.amzn1.x86_64.rpm                 LBUILD
     libtiff-devel                      libtiff-devel-4.0.3-20.20.amzn1.x86_64                 AMAZON
     giflib-devel                       giflib-devel-5.1.1-1.amzn1.x86_64                      LBUILD
     libid3tag-devel                    libid3tag-devel-0.15.1b-1.amzn1.x86_64.rpm             LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/imlib2.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/imlib2.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/imlib2-1.4.6-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/imlib2-devel-1.4.6-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/imlib2-id3tag-loader-1.4.6-1.amzn1.x86_64.rpm


libgdither-0.6---------------------------------------------------------------------------------1-DEPS-----*
     fftw-devel                         fftw-devel-3.3.4-1.amzn1.x86_64.rpm                    LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libgdither.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libgdither.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libgdither-0.6-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libgdither-devel-0.6-1.amzn1.x86_64.rpm


gavl-1.4.0-------------------------------------------------------------------------------------4-DEPS-----*
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     libpng                             libpng-devel-1.6.17-1.amzn1.x86_64.rpm                 LBUILD
     libgdither-devel                   libgdither-devel-0.6-1.amzn1.x86_64.rpm                LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/gavl.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/gavl.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gavl-1.4.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gavl-devel-1.4.0-1.amzn1.x86_64.rpm


ilmbase-2.2.0----------------------------------------------------------------------------------3-DEPS-----*
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     mesa-libGL-devel                   mesa-libGL-devel-10.6.0-1.amzn1.x86_64.rpm             LBUILD
     mesa-libGLU-devel                  mesa-libGLU-devel-9.0.0-1.amzn1.x86_64.rpm             LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/ilmbase.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/ilmbase.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/ilmbase-2.2.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/ilmbase-devel-2.2.0-1.amzn1.x86_64.rpm


OpenEXR-2.2.0----------------------------------------------------------------------------------3-DEPS-----*
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     ilmbase-devel                      ilmbase-devel-2.2.0-1.amzn1.x86_64.rpm                 LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/OpenEXR.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/OpenEXR.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/OpenEXR-2.2.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/OpenEXR-devel-2.2.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/OpenEXR-libs-2.2.0-1.amzn1.x86_64.rpm

eigen3-3.2.5-(24HR BUILD)----------------------------------------------------------------------9-DEPS-----*
     atlas-devel                        atlas-devel-3.8.4-2.6.amzn1.x86_64                     AMAZON
     fftw-devel                         fftw-devel-3.3.4-1.amzn1.x86_64                        LBUILD
     glew-devel                         glew-devel-1.10.0-1.amzn1.x86_64                       LBUILD
     gmp-devel                          gmp-devel-4.3.2-1.11.amzn1.x86_64                      AMAZON
     gsl-devel                          gsl-devel-1.13-4.3.amzn1.x86_64                        AMAZON
     cmake                              cmake-2.8.12-2.20.amzn1.x86_64                         AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     graphviz                           graphviz-2.38.0-18.50.amzn1.x86_64                     AMAZON
     texlive-collection-latexrecomm...  texlive-collection-latexrecommended-svn25795...        AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/eigen3.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/eigen3.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/noarch/eigen3-devel-3.2.5-1.amzn1.noarch.rpm


ffmpeg-basic-2.7-(FOR DEVEL, WILL BE REMOVED)--------------------------------------------------7-DEPS-----*
     libstdc++48-devel                  libstdc++-devel-4.8.2-3.19.amzn1.noarch                AMAZON
     openssl-devel                      openssl-devel-1:1.0.1k-1.84.amzn1.x86_64               AMAZON
     texi2html                          texi2html-1.82-5.1.5.amzn1.noarch                      AMAZON
     yasm                               yasm-1.2.0-1.2.amzn1.x86_64                            AMAZON
     SDL-devel                          SDL-devel-1.2.15-1.amzn1.x86_64.rpm                    LBUILD
     imlib2-devel                       imlib2-devel-1.4.6-1.amzn1.x86_64.rpm                  LBUILD
     libva-devel                        libva-devel-1.5.1-1.amzn1.x86_64.rpm                   LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/ffmpeg-basic.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/ffmpeg-basic.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/ffmpeg-devel-2.7-0.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/ffmpeg-libs-2.7-0.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/ffmpeg-2.7-0.amzn1.x86_64.rpm


libraw1394-2.1.0-------------------------------------------------------------------------------4-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     kernel-headers                     kernel-headers-3.14.42-31.38.amzn1.x86_64              AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libraw1394.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libraw1394.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libraw1394-2.1.0-2.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libraw1394-devel-2.1.0-2.amzn1.x86_64.rpm


libdc1394-2.2.2--------------------------------------------------------------------------------6-DEPS-----*
     kernel-headers                     kernel-headers-3.14.42-31.38.amzn1.x86_64              AMAZON
     libraw1394-devel                   libraw1394-devel-2.1.0-2.amzn1.x86_64.rpm              LBUILD
     libusb1-devel                      libusb1-devel-1.0.9-0.6.rc1.6.amzn1.x86_64             AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     libX11-devel                       libX11-devel-1.6.0-2.2.12.amzn1.x86_64                 AMAZON
     libXv-devel                        libXv-devel-1.0.9-2.1.8.amzn1.x86_64                   AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libdc1394.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libdc1394.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libdc1394-2.2.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libdc1394-devel-2.2.2-1.amzn1.x86_64.rpm


cups-2.0.3-------------------------------------------------------------------------------------10DEPS-----*
     pam-devel                          pam-devel-1.1.8-9.31.amzn1.x86_64                      AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     gnutls-devel                       gnutls-devel-3.4.2-1.amzn1.x86_64                      LBUILD
     libacl-devel                       libacl-devel-2.2.49-6.9.amzn1.x86_64                   AMAZON
     openldap-devel                     openldap-devel-2.4.23-34.23.amzn1.x86_64               AMAZON
     libusb1-devel                      libusb1-devel-1.0.9-0.6.rc1.6.amzn1.x86_64             AMAZON
     krb5-devel                         krb5-devel-1.10.3-37.29.amzn1.x86_64                   AMAZON
     avahi-devel                        avahi-devel-0.6.25-12.17.amzn1.x86_64                  AMAZON
     dbus-devel                         dbus-devel-1.6.12-8.27.amzn1.x86_64                    AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/cups.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/cups.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/cups-libs-2.0.3-1.amzn1.x86_64.rpm


libtheora-1.1.1--------------------------------------------------------------------------------8-DEPS-----*
     libogg-devel                       libogg-devel-1.3.2-1.amzn1.x86_64                      LBUILD
     libvorbis-devel                    libvorbis-devel-1.3.5-1.amzn1.x86_64                   LBUILD
     SDL-devel                          SDL-devel-1.2.15-1.amzn1.x86_64.rpm                    LBUILD
     libpng-devel                       libpng-devel-1.6.17-1.amzn1.x86_64.rpm                 LBUILD
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     texlive-latex                      texlive-latex-svn27907.0-27.21.amzn1.noarch            AMAZON
     transfig                           transfig-3.2.5-10.6.amzn1.x86_64                       AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libtheora.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libtheora.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libtheora-1.1.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libtheora-devel-1.1.1-1.amzn1.x86_64.rpm


libv4l-1.6.2-----------------------------------------------------------------------------------4-DEPS-----*
     libjpeg-turbo-devel                libjpeg-turbo-devel-1.4.1-1.amzn1.x86_64               LBUILD
     kernel-headers                     kernel-headers-3.14.42-31.38.amzn1.x86_64              AMAZON
     alsa-lib-devel                     alsa-lib-devel-1.0.22-3.9.amzn1.x86_64                 AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/v4l-utils.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/v4l-utils.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libv4l-devel-1.6.2-1.amzn1.x86_64.rpm  \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libv4l-1.6.2-1.amzn1.x86_64.rpm


libwebp-0.4.3----------------------------------------------------------------------------------11DEPS-----*
     libjpeg-turbo-devel                libjpeg-turbo-devel-1.4.1-1.amzn1.x86_64               LBUILD
     libpng-devel                       libpng-devel-1.6.17-1.amzn1.x86_64.rpm                 LBUILD
     giflib-devel                       giflib-devel-5.1.1-1.amzn1.x86_64.rpm                  LBUILD
     libtiff-devel                      libtiff-devel-4.0.3-20.20.amzn1.x86_64                 AMAZON
     java-devel                         java-1.7.0-openjdk-devel-1.7.0.79-2.5.5.1.59.am...     AMAZON
     jpackage-utils                     jpackage-utils-1.7.5-27.17.amzn1.noarch                AMAZON
     swig                               swig-2.0.10-4.24.amzn1.x86_64                          AMAZON
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     freeglut-devel                     freeglut-devel-2.6.0-1.8.amzn1.x86_64                  AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libwebp.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libwebp.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libwebp-0.4.3-2.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libwebp-devel-0.4.3-2.amzn1.x86_64.rpm


gstreamer-1.5.2--------------------------------------------------------------------------------22DEPS-----*
     glib2-devel                        glib2-devel-2.36.3-5.18.amzn1.x86_64                   AMAZON
     libxml12                           libxml2-devel-2.9.1-3.1.35.amzn1.x86_64                AMAZON
     gobject-introspection-devel        gobject-introspection-devel-1.36.0-4.9.amzn1.x86_64    AMAZON
     bison                              bison-2.4.1-5.8.amzn1.x86_64                           AMAZON
     flex                               flex-2.5.36-1.8.amzn1.x86_64                           AMAZON
     m4                                 m4-1.4.16-9.10.amzn1.x86_64                            AMAZON
     check-devel                        check-devel-0.9.8-1.1.6.amzn1.x86_64                   AMAZON
     gtk-doc                            gtk-doc-1.19-2.11.amzn1.noarch                         AMAZON
     gettext                            gettext-0.18.1.1-9.1.11.amzn1.x86_64                   AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     chrpath                            chrpath-0.13-7.6.amzn1.x86_64                          AMAZON
     python27                           python27-2.7.9-4.115.amzn1.x86_64                      AMAZON
     openjade                           openjade-1.3.2-36.5.amzn1.x86_64                       AMAZON
     texlive-jadetex                    texlive-jadetex-svn23409.3.13-27.21.amzn1.noarch       AMAZON
     libxslt                            libxslt-1.1.28-5.12.amzn1.x86_64                       AMAZON
     docbook-style-dsssl                docbook-style-dsssl-1.79-10.7.amzn1.noarch             AMAZON
     docbook-style-xsl                  docbook-style-xsl-1.78.1-3.9.amzn1.noarch              AMAZON
     docbook-utils                      docbook-utils-0.6.14-25.6.amzn1.noarch                 AMAZON
     transfig                           transfig-3.2.5-10.6.amzn1.x86_64                       AMAZON
     netpbm-progs                       netpbm-progs-10.47.05-11.6.amzn1.x86_64                AMAZON
     texlive-dvips                      texlive-dvips-svn29585.0-27.21.amzn1.noarch            AMAZON
     ghostscript                        ghostscript-8.70-19.23.amzn1.x86_64                    AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/gstreamer1.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/gstreamer1.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gstreamer1-1.5.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gstreamer1-devel-1.5.2-1.amzn1.x86_64.rpm

libvisual-0.4.0--------------------------------------------------------------------------------1-DEPS-----*
     xorg-x11-proto-devel               xorg-x11-proto-devel-7.7-9.10.amzn1.noarch             AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libvisual.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libvisual.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libvisual-0.4.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libvisual-devel-0.4.0-1.amzn1.x86_64.rpm

gstreamer-plugins-base-1.5.2-------------------------------------------------------------------13DEPS-----*
     gstreamer1-devel                   gstreamer1-devel-1.5.2-1.amzn1.x86_64                  LBUILD
     gobject-introspection-devel        gobject-introspection-devel-1.36.0-4.9.amzn1.x86_64    AMAZON
     iso-codes-devel                    iso-codes-devel-3.16-2.7.amzn1.noarch                  AMAZON
     alsa-lib-devel                     alsa-lib-devel-1.0.22-3.9.amzn1.x86_64                 AMAZON
     libogg-devel                       libogg-devel-1.3.2-1.amzn1.x86_64                      LBUILD
     libtheora-devel                    libtheora-devel-1.1.1-1.amzn1.x86_64.rpm               LBUILD
     libvisual-devel                    libvisual-devel-0.4.0-1.amzn1.x86_64                   LBUILD
     libvorbis-devel                    libvorbis-devel-1.3.5-1.amzn1.x86_64                   LBUILD
     libXv-devel                        libXv-devel-1.0.9-2.1.8.amzn1.x86_64                   AMAZON
     orc-devel                          orc-devel-0.4.23-1.amzn1.x86_64.rpm                    LBUILD
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     chrpath                            chrpath-0.13-7.6.amzn1.x86_64                          AMAZON
     gtk-doc                            gtk-doc-1.19-2.11.amzn1.noarch                         AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/gstreamer1-plugins-base.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/gstreamer1-plugins-base.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gstreamer1-plugins-base-1.5.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gstreamer1-plugins-base-devel-1.5.2-1.amzn1.x86_64.rpm


tinyxml-2.6.2----------------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/tinyxml.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/tinyxml.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/tinyxml-2.6.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/tinyxml-devel-2.6.2-1.amzn1.x86_64.rpm


openni-1.5.7.10--------------------------------------------------------------------------------10DEPS-----*
     freeglut-devel                     freeglut-devel-2.6.0-1.8.amzn1.x86_64                  AMAZON
     tinyxml-devel                      tinyxml-devel-2.6.2-1.amzn1.x86_64                     LBUILD
     libjpeg-turbo-devel                libjpeg-turbo-devel-1.4.1-1.amzn1.x86_64               LBUILD
     dos2unix                           dos2unix-3.1-37.5.amzn1.x86_64                         AMAZON
     libusb1-devel                      libusb1-devel-1.0.9-0.6.rc1.6.amzn1.x86_64             AMAZON
     python27-devel                     python26-devel-2.6.9-1.80.amzn1.x86_64                 AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     graphviz                           graphviz-2.38.0-18.50.amzn1.x86_64                     AMAZON
     java-devel                         java-1.7.0-openjdk-devel-1.7.0.79-2.5.5.1.59.am...     AMAZON
     jpackage-utils                     jpackage-utils-1.7.5-27.17.amzn1.noarch                AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/openni.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/openni.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/openni-1.5.7.10-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/openni-devel-1.5.7.10-1.amzn1.x86_64.rpm


opencv-2.4.11----------------------------------------------------------------------------------27DEPS-----*
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     cmake                              cmake-2.8.12-2.20.amzn1.x86_64                         AMAZON
     chrpath                            chrpath-0.13-7.6.amzn1.x86_64                          AMAZON
     eigen3-devel                       eigen3-devel-3.2.5-1.amzn1.noarch.rpm                  LBUILD
     libvorbis-devel                    libvorbis-devel-1.3.5-1.amzn1.x86_64                   LBUILD
     jasper-devel                       jasper-devel-1.900.1-16.9.amzn1.x86_64                 AMAZON
     libpng-devel                       libpng-devel-1.6.17-1.amzn1.x86_64.rpm                 LBUILD
     libjpeg-turbo-devel                libjpeg-turbo-devel-1.4.1-1.amzn1.x86_64               LBUILD
     libtiff-devel                      libtiff-devel-4.0.3-20.20.amzn1.x86_64                 AMAZON
     mesa-libGL-devel                   mesa-libGL-devel-10.6.0-1.amzn1.x86_64.rpm             LBUILD
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     python27-devel                     python27-devel-2.7.9-4.115.amzn1.x86_64                AMAZON
     swig                               swig-2.0.10-4.24.amzn1.x86_64                          AMAZON
     ffmpeg                             ffmpeg-devel-2.7-1.amzn1.x86_64                        LBUILD
     python27-numpy                     python27-numpy-1.7.2-8.16.amzn1.x86_64                 AMAZON
     python27-sphinx                    python27-sphinx-1.1.3-5.16.amzn1.noarch                AMAZON
     OpenEXR-devel                      OpenEXR-devel-2.2.0-1.amzn1.x86_64.rpm                 LBUILD
     libdc1394-devel                    libdc1394-devel-2.2.2-1.amzn1.x86_64.rpm               LBUILD
     libraw1394-devel                   libraw1394-devel-2.1.0-2.amzn1.x86_64.rpm              LBUILD
     libtheora-devel                    libtheora-devel-1.1.1-1.amzn1.x86_64.rpm               LBUILD
     libv4l-devel                       libv4l-devel-1.6.2-1.amzn1.x86_64.rpm                  LBUILD
     opencl-headers                     opencl-headers-1.2-1.amzn1.noarch.rpm                  LBUILD
     gstreamer                          gstreamer1-1.5.2-1.amzn1.x86_64.rpm                    LBUILD
     gstreamer-plugins-base             gstreamer1-plugins-base-devel-1.5.2-1.amzn1.x86_64.rpm LBUILD
     openni-devel                       openni-devel-1.5.7.10-1.amzn1.x86_64                   LBUILD
     tbb-devel                          tbb-devel-2.2-3.20090809.2.amzn1.x86_64                LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/opencv.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/opencv.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/opencv-2.4.11-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/opencv-devel-2.4.11-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/opencv-core-2.4.11-1.amzn1.x86_64.rpm


frei0r-1.4-------------------------------------------------------------------------------------4-DEPS-----*
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     cairo-devel                        cairo-devel-1.14.2-1.amzn1.x86_64.rpm                  AMAZON
     gavl-devel                         gavl-devel-1.4.0-1.amzn1.x86_64.rpm                    LBUILD
     opencv-devel                       opencv-devel-2.4.11-1.amzn1.x86_64.rpm                 LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/frei0r-plugins.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/frei0r-plugins.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/frei0r-plugins-1.4-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/frei0r-plugins-opencv-1.4-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/frei0r-devel-1.4-1.amzn1.x86_64.rpm


libvpx-1.4.0-----------------------------------------------------------------------------------3-DEPS-----*
     yasm                               yasm-1.2.0-1.2.amzn1.x86_64                            AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     php56-cli                          php56-cli-5.6.9-1.112.amzn1.x86_64                     AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libvpx.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libvpx.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
        /home/ec2-user/rpmbuild/RPMS/x86_64/libvpx-1.4.0-1.amzn1.x86_64.rpm \
        /home/ec2-user/rpmbuild/RPMS/x86_64/libvpx-devel-1.4.0-1.amzn1.x86_64.rpm
     

a52dec-0.7.4-----------------------------------------------------------------------------------1-DEPS-----*
     perl                               perl-5.16.3-283.37.amzn1.x86_64                        AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/a52dec.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/a52dec.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/a52dec-0.7.4-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/a52dec-devel-0.7.4-1.amzn1.x86_64.rpm


libmp4v2-2.0.0---------------------------------------------------------------------------------5-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     getgettext-devel                   gettext-devel-0.18.1.1-9.1.11.amzn1.x86_64             AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     ttexinfo                           texinfo-5.1-4.10.amzn1.x86_64                          AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libmp4v2.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libmp4v2.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmp4v2-2.0.0-1.amzn1.x86_64.rpm  \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmp4v2-devel-2.0.0-1.amzn1.x86_64.rpm


faac-1.28--------------------------------------------------------------------------------------2-DEPS-----*
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     libmp4v2-devel                     libmp4v2-devel-2.0.0-1.amzn1.x86_64.rpm                LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/faac.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/faac.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/faac-1.28-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/faac-devel-1.28-1.amzn1.x86_64.rpm
     

id3lib-3.8.3-----------------------------------------------------------------------------------5-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/id3lib.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/id3lib.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/id3lib-3.8.3-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/id3lib-devel-3.8.3-1.amzn1.x86_64.rpm


faad2-2.7--------------------------------------------------------------------------------------3-DEPS-----*
     gcc48-c++                          gcc48-c++-4.8.2-16.2.99.amzn1.x86_64                   AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     id3lib-devel                       id3lib-devel-3.8.3-1.amzn1.x86_64.rpm                  LBUILD
     libdrm-devel                       libdrm-devel-2.4.61-3.amzn1.x86_64.rpm                 LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/faad2.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/faad2.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/faad2-2.7-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/faad2-devel-2.7-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/faad2-libs-2.7-1.amzn1.x86_64.rpm


fdk-aac-0.1.4----------------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/fdk-aac.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/fdk-aac.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/fdk-aac-0.1.4-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/fdk-aac-devel-0.1.4-1.amzn1.x86_64.rpm


fribidi-0.19.6---------------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/fribidi.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/fribidi.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
        /home/ec2-user/rpmbuild/RPMS/x86_64/fribidi-0.19.6-1.amzn1.x86_64.rpm \
        /home/ec2-user/rpmbuild/RPMS/x86_64/fribidi-devel-0.19.6-1.amzn1.x86_64.rpm

ilbc-1.1.1-------------------------------------------------------------------------------------3-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/ilbc.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/ilbc.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/ilbc-1.1.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/ilbc-devel-1.1.1-1.amzn1.x86_64.rpm


ladspa-1.13------------------------------------------------------------------------------------2-DEPS-----*
     perl                               perl-5.16.3-283.37.amzn1.x86_64                        AMAZON
     gcc48-c++                          gcc48-c++-4.8.2-16.2.99.amzn1.x86_64                   AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/ladspa.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/ladspa.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/ladspa-1.13-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/ladspa-devel-1.13-1.amzn1.x86_64.rpm


lame-3.99.5------------------------------------------------------------------------------------3-DEPS-----*
     ncurses-devel                      ncurses-devel-5.7-3.20090208.13.amzn1.x86_64           AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     nasm                               nasm-2.10.07-7.7.amzn1.x86_64                          AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/lame.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/lame.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/lame-3.99.5-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/lame-libs-3.99.5-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/lame-devel-3.99.5-1.amzn1.x86_64.rpm


libaacplus-2.0.2-------------------------------------------------------------------------------5-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     fftw-devel                         fftw-devel-3.3.4-1.amzn1.x86_64.rpm                    LBUILD
     wget                               wget-1.16.1-3.18.amzn1.x86_64                          AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libaacplus.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libaacplus.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libaacplus-2.0.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libaacplus-devel-2.0.2-1.amzn1.x86_64.rpm


enca-1.16--------------------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/enca.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/enca.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/enca-1.16-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/enca-devel-1.16-1.amzn1.x86_64.rpm


libass-0.12.2----------------------------------------------------------------------------------5-DEPS-----*
     fontconfig-devel                   fontconfig-devel-2.8.0-5.8.amzn1.x86_64                AMAZON
     fribidi-devel                      fribidi-devel-0.19.6-1.amzn1.x86_64.rpm                LBUILD
     harfbuzz-devel                     harfbuzz-devel-0.9.20-3.5.amzn1.x86_64                 AMAZON
     libpng-devel                       libpng-devel-1.6.17-2.amzn1.x86_64                     LBUILD
     enca-devel                         enca-devel-1.16-1.amzn1.x86_64.rpm                     LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libass.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libass.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libass-0.12.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libass-devel-0.12.2-1.amzn1.x86_64.rpm


libbs2b-3.1.0----------------------------------------------------------------------------------1-DEPS-----*
     libsndfile-devel                   libsndfile-devel-1.0.25-1.amzn1.x86_64.rpm             LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libbs2b.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libbs2b.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libbs2b-3.1.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libbs2b-devel-3.1.0-1.amzn1.x86_64.rpm


libbluray-0.8.1--------------------------------------------------------------------------------9-DEPS-----*
     java-devel                         java-1.7.0-openjdk-devel-1.7.0.79-2.5.5.1.59.am...     AMAZON
     jpackage-utils                     jpackage-utils-1.7.5-27.17.amzn1.noarch                AMAZON
     ant                                ant-1.8.3-1.13.amzn1.noarch                            AMAZON
     libxml12                           libxml2-devel-2.9.1-3.1.35.amzn1.x86_64                AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     texlive-collection-latexrecomm...  texlive-collection-latexrecommended-svn25795...        AMAZON
     graphviz                           graphviz-2.38.0-18.50.amzn1.x86_64                     AMAZON
     freetype-devel                     freetype-devel-2.3.11-15.14.amzn1.x86_64               AMAZON
     fontconfig-devel                   fontconfig-devel-2.8.0-5.8.amzn1.x86_64                AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libbluray.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libbluray.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libbluray-0.8.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libbluray-devel-0.8.1-1.amzn1.x86_64.rpm


libcaca-0.99-----------------------------------------------------------------------------------10DEPS-----*
     slang-devel                        slang-devel-2.2.1-1.8.amzn1.x86_64                     AMAZON
     ncurses-devel                      ncurses-devel-5.7-3.20090208.13.amzn1.x86_64           AMAZON
     freeglut-devel                     freeglut-devel-2.6.0-1.8.amzn1.x86_64                  AMAZON
     mesa-libGLU-devel                  mesa-libGLU-devel-9.0.0-1.amzn1.x86_64.rpm             LBUILD
     imlib2-devel                       imlib2-devel-1.4.6-1.amzn1.x86_64.rpm                  LBUILD
     pango-devel                        pango-devel-1.28.1-10.11.amzn1.x86_64                  AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     texlive-latex                      texlive-latex-svn27907.0-27.21.amzn1.noarch            AMAZON
     texlive-dvips                      texlive-dvips-svn29585.0-27.21.amzn1.noarch            AMAZON
     python27-devel                     python27-devel-2.7.9-4.115.amzn1.x86_64                AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libcaca.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libcaca.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libcaca-0.99-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libcaca-devel-0.99-1.amzn1.x86_64.rpm


libcdio-0.93-----------------------------------------------------------------------------------6-DEPS-----*
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     ncurses-devel                      ncurses-devel-5.7-3.20090208.13.amzn1.x86_64           AMAZON
     help2man                           help2man-1.41.1-2.8.amzn1.noarch                       AMAZON
     gettext-devel                      gettext-devel-0.18.1.1-9.1.11.amzn1.x86_64             AMAZON
     chrpath                            chrpath-0.13-7.6.amzn1.x86_64                          AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libcdio.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libcdio.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libcdio-0.93-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libcdio-devel-0.93-1.amzn1.x86_64.rpm


libdcadec-0.0.0--------------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/libdcadec.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libdcadec.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libdcadec-0.0.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libdcadec-devel-0.0.0-1.amzn1.x86_64.rpm


libmodplug-0.8.8.5-----------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/libmodplug.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libmodplug.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmodplug-0.8.8.5-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmodplug-devel-0.8.8.5-1.amzn1.x86_64.rpm


lua-expat-1.3.0--------------------------------------------------------------------------------3-DEPS-----*
     lua                                lua-5.1.4-4.1.9.amzn1.x86_64                           AMAZON
     lua-devel                          lua-devel-5.1.4-4.1.9.amzn1.x86_64                     AMAZON
     expat-devel                        expat-devel-2.1.0-8.18.amzn1.x86_64                    AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/lua-expat.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/lua-expat.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/lua-expat-1.3.0-1.amzn1.x86_64.rpm


lua-socket-3.0---------------------------------------------------------------------------------3-DEPS-----*
     lua                                lua-5.1.4-4.1.9.amzn1.x86_64                           AMAZON
     lua-devel                          lua-devel-5.1.4-4.1.9.amzn1.x86_64                     AMAZON
     glibc-common                       glibc-common-2.17-55.143.amzn1.x86_64                  AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/lua-socket.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/lua-socket.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/lua-socket-3.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/lua-socket-devel-3.0-1.amzn1.x86_64.rpm


lua-lpeg-0.9-----------------------------------------------------------------------------------2-DEPS-----*
     lua                                lua-5.1.4-4.1.9.amzn1.x86_64                           AMAZON
     lua-devel                          lua-devel-5.1.4-4.1.9.amzn1.x86_64                     AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/lua-lpeg.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/lua-lpeg.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/lua-lpeg-0.9-1.amzn1.x86_64.rpm


lua-lunit-0.5----------------------------------------------------------------------------------1-DEPS-----*
     lua                                lua-5.1.4-4.1.9.amzn1.x86_64                           AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/lua-lunit.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/lua-lunit.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/noarch/lua-lunit-0.5-1.amzn1.noarch.rpm


lua-json-1.3.2---------------------------------------------------------------------------------4-DEPS-----*
     lua                                lua-5.1.4-4.1.9.amzn1.x86_64                           AMAZON
     lua-filesystem                     lua-filesystem-1.6.2-2.2.amzn1.x86_64                  AMAZON
     lua-lpeg                           lua-lpeg-0.9-1.amzn1.x86_64.rpm                        LBUILD
     lua-lunit                          lua-lunit-0.5-1.amzn1.noarch.rpm                       LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/lua-json.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/lua-json.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/noarch/lua-json-1.3.2-1.amzn1.noarch.rpm


libquvi-scripts-0.9.20131130-------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/libquvi-scripts.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libquvi-scripts.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/noarch/libquvi-scripts-0.9.20131130-1.amzn1.noarch.rpm


libmodman-2.0.1--------------------------------------------------------------------------------2-DEPS-----*
     cmake                              cmake-2.8.12-2.20.amzn1.x86_64                         AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libmodman.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libmodman.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmodman-2.0.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmodman-devel-2.0.1-1.amzn1.x86_64.rpm


libproxy-0.4.11--------------------------------------------------------------------------------3-DEPS-----*
     python27-devel                     python26-devel-2.6.9-1.80.amzn1.x86_64                 AMAZON
     libmodman-devel                    libmodman-devel-2.0.1-1.amzn1.x86_64                   LBUILD
     cmake                              cmake-2.8.12-2.20.amzn1.x86_64                         AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libproxy.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libproxy.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libproxy-0.4.11-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libproxy-bin-0.4.11-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/noarch/libproxy-python-0.4.11-1.amzn1.noarch.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libproxy-devel-0.4.11-1.amzn1.x86_64.rpm


libquvi-0.9.4----------------------------------------------------------------------------------8-DEPS-----*
     lua-devel                          lua-devel-5.1.4-4.1.9.amzn1.x86_64                     AMAZON
     lua-socket                         lua-socket-3.0-1.amzn1.x86_64                          LBUILD
     glib2-devel                        glib2-devel-2.36.3-5.18.amzn1.x86_64                   AMAZON
     libcurl-devel                      libcurl-devel-7.40.0-3.51.amzn1.x86_64                 AMAZON
     libgcrypt-devel                    libgcrypt-devel-1.5.3-4.15.amzn1.x86_64                AMAZON
     libproxy-devel                     libproxy-devel-0.4.11-1.amzn1.x86_64.rpm               LBUILD
     libquvi-scripts                    libquvi-scripts-0.9.20131130-1.amzn1.noarch            LBUILD
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libquvi.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libquvi.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libquvi-0.9.4-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libquvi-devel-0.9.4-1.amzn1.x86_64.rpm


libshine-3.1.0---------------------------------------------------------------------------------3-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libshine.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libshine.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/shine-3.1.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/shine-devel-3.1.0-1.amzn1.x86_64.rpm


snappy-1.1.2-----------------------------------------------------------------------------------1-DEPS-----*
     gtest-devel                        gtest-1.6.0-1.1.amzn1.x86_64                           AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/snappy.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/snappy.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/snappy-1.1.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/snappy-devel-1.1.2-1.amzn1.x86_64.rpm


libssh-0.7.1-----------------------------------------------------------------------------------5-DEPS-----*
     cmake                              cmake-2.8.12-2.20.amzn1.x86_64                         AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     openssl-devel                      openssl-devel-1.0.1k-10.86.amzn1.x86_64                AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libssh.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libssh.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libssh-0.7.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libssh-devel-0.7.1-1.amzn1.x86_64.rpm


libutvideo-15.1.0------------------------------------------------------------------------------3-DEPS-----*
     libstdc++48-devel                  libstdc++48-devel-4.8.2-16.2.99.amzn1.x86_64           AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     nasm                               nasm-2.10.07-7.7.amzn1.x86_64                          AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libutvideo.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libutvideo.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libutvideo-15.1.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libutvideo-devel-15.1.0-1.amzn1.x86_64.rpm


libvidstab-0.98b-------------------------------------------------------------------------------1-DEPS-----*
     cmake                              cmake-2.8.12-2.20.amzn1.x86_64                         AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/vidstab.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/vidstab.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libvidstab-0.98b-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libvidstab-devel-0.98b-1.amzn1.x86_64.rpm


libvdpau-1.1-----------------------------------------------------------------------------------9-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     graphviz                           graphviz-2.38.0-18.50.amzn1.x86_64                     AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     libX11-devel                       libX11-devel-1.6.0-2.2.12.amzn1.x86_64                 AMAZON
     libXext-devel                      libXext-devel-1.3.2-2.1.10.amzn1.x86_64                AMAZON
     texlive-latex                      texlive-latex-svn27907.0-27.21.amzn1.noarch            AMAZON
     xorg-x11-proto-devel               xorg-x11-proto-devel-7.7-9.10.amzn1.noarch             AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libvdpau.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libvdpau.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libvdpau-1.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libvdpau-devel-1.1-1.amzn1.x86_64.rpm


openal-soft-1.16.0-----------------------------------------------------------------------------3-DEPS-----*
     alsa-lib-devel                     alsa-lib-devel-1.0.22-3.9.amzn1.x86_64                 AMAZON
     pulseaudio-libs-devel              pulseaudio-libs-devel-6.0-1.amzn1.x86_64.rpm           LBUILD
     cmake                              cmake-2.8.12-2.20.amzn1.x86_64                         AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/openal-soft.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/openal-soft.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/openal-soft-1.16.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/openal-soft-devel-1.16.0-1.amzn1.x86_64.rpm


opencore-amr-0.1.3-----------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/opencore-amr.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/opencore-amr.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/opencore-amr-0.1.3-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/opencore-amr-devel-0.1.3-1.amzn1.x86_64.rpm


openh264-1.4.0---------------------------------------------------------------------------------1-DEPS-----*
     nasm                               nasm-2.10.07-7.7.amzn1.x86_64                          AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/openh264.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/openh264.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/openh264-1.4.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/openh264-devel-1.4.0-1.amzn1.x86_64.rpm


rtmpdump-2.4.1---------------------------------------------------------------------------------4-DEPS-----*
     gnutls                             gnutls-devel-3.4.2-1.amzn1.x86_64.rpm                  LBUILD
     libgcrypt-devel                    libgcrypt-devel-1.5.3-4.15.amzn1.x86_64                AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     nettle-devel                       nettle-devel-3.1.1-1.amzn1.x86_64.rpm                  LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/rtmpdump.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/rtmpdump.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/librtmp-2.4-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/librtmp-devel-2.4-1.amzn1.x86_64.rpm


schroedinger-1.0.11----------------------------------------------------------------------------3-DEPS-----*
     orc-devel                          orc-devel-0.4.23-1.amzn1.x86_64.rpm                    LBUILD
     glew-devel                         glew-devel-1.10.0-1.amzn1.x86_64.rpm                   LBUILD
     gtk-doc                            gtk-doc-1.19-2.11.amzn1.noarch                         AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/schroedinger.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/schroedinger.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/schroedinger-1.0.11-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/schroedinger-devel-1.0.11-1.amzn1.x86_64.rpm


soxr-0.1.1-------------------------------------------------------------------------------------1-DEPS-----*
     cmake                              cmake-2.8.12-2.20.amzn1.x86_64                         AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/soxr.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/soxr.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/soxr-0.1.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/soxr-devel-0.1.1-1.amzn1.x86_64.rpm


twolame-0.3.13---------------------------------------------------------------------------------2-DEPS-----*
     libsndfile-devel                   libsndfile-devel-1.0.25-1.amzn1.x86_64.rpm             LBUILD
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/twolame.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/twolame.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/twolame-0.3.13-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/twolame-libs-0.3.13-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/twolame-devel-0.3.13-1.amzn1.x86_64.rpm


vo-aacenc-0.1.3--------------------------------------------------------------------------------2-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/vo-aacenc.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/vo-aacenc.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/vo-aacenc-0.1.3-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/vo-aacenc-devel-0.1.3-1.amzn1.x86_64.rpm


vo-amrwbenc-0.1.3------------------------------------------------------------------------------2-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/vo-amrwbenc.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/vo-amrwbenc.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/vo-amrwbenc-0.1.3-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/vo-amrwbenc-devel-0.1.3-1.amzn1.x86_64.rpm


wavpack-4.75.0---------------------------------------------------------------------------------3-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/wavpack.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/wavpack.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/wavpack-4.75.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/wavpack-devel-4.75.0-1.amzn1.x86_64.rpm


libmad-0.15.1b---------------------------------------------------------------------------------3-DEPS-----*
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libmad.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libmad.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmad-0.15.1b-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmad-devel-0.15.1b-1.amzn1.x86_64.rpm


xvidcore-1.3.4---------------------------------------------------------------------------------1-DEPS-----*
     nasm                               nasm-2.10.07-7.7.amzn1.x86_64                          AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/xvidcore.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/xvidcore.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/xvidcore-1.3.4-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/xvidcore-devel-1.3.4-1.amzn1.x86_64.rpm

gpac-0.5.2-------------------------------------------------------------------------------------27DEPS-----*
     ImageMagick                        ImageMagick-6.7.8.9-10.15.amzn1.x86_64                 AMAZON
     SDL-devel                          SDL-devel-1.2.15-1.amzn1.x86_64.rpm                    LBUILD
     a52dec-devel                       a52dec-devel-0.7.4-1.amzn1.x86_64.rpm                  LBUILD
     mesa-libGLU-devel                  mesa-libGLU-devel-10.6.0-1.amzn1.x86_64.rpm            LBUILD
     freeglut-devel                     freeglut-devel-2.6.0-1.8.amzn1.x86_64                  AMAZON
     freetype-devel                     freetype-devel-2.3.11-15.14.amzn1.x86_64               AMAZON
     faad2-devel                        faad2-devel-2.7-1.amzn1.x86_64.rpm                     LBUILD
     libjpeg-turbo-devel                libjpeg-turbo-devel-1.4.1-1.amzn1.x86_64               LBUILD
     libpng                             libpng-devel-1.6.17-1.amzn1.x86_64.rpm                 LBUILD
     ffmpeg-devel                       ffmpeg-devel-2.7-1.amzn1.x86_64                        LBUILD
     libxml12                           libxml2-devel-2.9.1-3.1.35.amzn1.x86_64                AMAZON
     openssl-devel                      openssl-devel-1.0.1k-10.86.amzn1.x86_64                AMAZON
     openjpeg-devel                     openjpeg-devel-1.3-10.7.amzn1.x86_64                   AMAZON
     pulseaudio-libs-devel              pulseaudio-libs-devel-6.0-1.amzn1.x86_64.rpm           LBUILD
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     libogg-devel                       libogg-devel-1.3.2-1.amzn1.x86_64                      LBUILD
     libvorbis-devel                    libvorbis-devel-1.3.5-1.amzn1.x86_64.rpm               LBUILD
     libtheora-devel                    libtheora-devel-1.1.1-1.amzn1.x86_64.rpm               LBUILD
     libXt-devel                        libXt-devel-1.1.4-6.1.9.amzn1.x86_64                   AMAZON
     libXv-devel                        libXv-devel-1.0.9-2.1.8.amzn1.x86_64                   AMAZON
     xmlrpc-c-devel                     xmlrpc-c-devel-1.22.04-r1934.5.amzn1.x86_64            AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     graphviz                           graphviz-2.38.0-18.50.amzn1.x86_64                     AMAZON
     opencore-amr-devel                 opencore-amr-devel-0.1.3-1.amzn1.x86_64                LBUILD
     libmad-devel                       libmad-devel-0.15.1b-1.amzn1.x86_64.rpm                LBUILD
     librsvg2-devel                     librsvg2-devel-2.40.9-1.amzn1.x86_64.rpm               LBUILD
     xvidcore-devel                     xvidcore-devel-1.3.4-1.amzn1.x86_64.rpm                LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/gpac.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/gpac.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gpac-0.5.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gpac-libs-0.5.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gpac-devel-0.5.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/gpac-devel-static-0.5.2-1.amzn1.x86_64.rpm


x264-0.142-------------------------------------------------------------------------------------8-DEPS-----*
     perl-Digest-MD5                    perl-Digest-MD5-2.52-3.5.amzn1.x86_64                  AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     openssl-devel                      openssl-devel-1.0.1k-10.86.amzn1.x86_64                AMAZON
     libpng                             libpng-devel-1.6.17-1.amzn1.x86_64.rpm                 LBUILD
     libjpeg-turbo-devel                libjpeg-turbo-devel-1.4.1-1.amzn1.x86_64               LBUILD
     ffmpeg-devel                       ffmpeg-devel-2.7-1.amzn1.x86_64                        LBUILD
     yasm                               yasm-1.2.0-1.2.amzn1.x86_64                            AMAZON
     gpac-devel-static                  gpac-devel-static-0.5.2-1.amzn1.x86_64.rpm             LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/x264.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/x264.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/x264-0.142-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/x264-libs-0.142-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/x264-devel-0.142-1.amzn1.x86_64.rpm


x265-1.7---------------------------------------------------------------------------------------2-DEPS-----*
     cmake                              cmake-2.8.12-2.20.amzn1.x86_64                         AMAZON
     yasm                               yasm-1.2.0-1.2.amzn1.x86_64                            AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/x265.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/x265.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/x265-1.7-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/x265-libs-1.7-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/x265-devel-1.7-1.amzn1.x86_64.rpm


taglib-1.9.1-----------------------------------------------------------------------------------5-DEPS-----*
     cmake                              cmake-2.8.12-2.20.amzn1.x86_64                         AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     graphviz                           graphviz-2.38.0-18.50.amzn1.x86_64                     AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/taglib.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/taglib.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/taglib-1.9.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/taglib-devel-1.9.1-1.amzn1.x86_64.rpm


chromaprint-1.2--------------------------------------------------------------------------------7-DEPS-----*
     cmake                              cmake-2.8.12-2.20.amzn1.x86_64                         AMAZON
     fftw-devel                         fftw-devel-3.3.4-1.amzn1.x86_64.rpm                    LBUILD
     ffmpeg-devel                       ffmpeg-devel-2.7-1.amzn1.x86_64                        LBUILD
     boost-devel                        boost-devel-1.53.0-14.21.amzn1.x86_64                  AMAZON
     gcc48-c++                          gcc48-c++-4.8.2-16.2.99.amzn1.x86_64                   AMAZON
     taglib-devel                       taglib-devel-1.9.1-1.amzn1.x86_64                      LBUILD
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/chromaprint.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/chromaprint.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/chromaprint-fpcalc-1.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libchromaprint-1.2-1.amzn1.x86_64.rpm


xavs-0.1.51------------------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/xavs.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/xavs.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/xavs-0.1.51-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/xavs-libs-0.1.51-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/xavs-devel-0.1.51-1.amzn1.x86_64.rpm


madplay----------------------------------------------------------------------------------------4-DEPS-----*
     libmad-devel                       libmad-devel-0.15.1b-1.amzn1.x86_64                    LBUILD
     libid3tag-devel                    libid3tag-devel-0.15.1b-1.amzn1.x86_64                 LBUILD
     gettext                            gettext-0.18.1.1-9.1.11.amzn1.x86_64                   AMAZON
     alsa-lib-devel                     alsa-lib-devel-1.0.22-3.9.amzn1.x86_64                 AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/madplay.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/madplay.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/madplay-0.15.2b-1.amzn1.x86_64.rpm


libao------------------------------------------------------------------------------------------NODEPS-----*
     alsa-lib-devel                     alsa-lib-devel-1.0.22-3.9.amzn1.x86_64                 AMAZON
     pulseaudio-libs-devel              pulseaudio-libs-devel-6.0-1.amzn1.x86_64.rpm           LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libao.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libao.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libao-1.2.0-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libao-devel-1.2.0-1.amzn1.x86_64.rpm


libebml------------------------------------------------------------------------------------------NODEPS-----*
     sudo yum-builddep ~/rpmbuild/SPECS/libebml.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libebml.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libebml-1.3.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libebml-devel-1.3.1-1.amzn1.x86_64.rpm


libmatroska------------------------------------------------------------------------------------1-DEPS-----*
     libebml-devel                      libebml-devel-1.3.1-1.amzn1.x86_64                     LBUILD
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libmatroska.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libmatroska.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmatroska-1.4.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmatroska-devel-1.4.2-1.amzn1.x86_64.rpm


libmpeg2-0.5.1---------------------------------------------------------------------------------3-DEPS-----*
     SDL-devel                          SDL-devel-1.2.15-1.amzn1.x86_64.rpm                    LBUILD
     libXt-devel                        libXt-devel-1.1.4-6.1.9.amzn1.x86_64                   AMAZON
     libXv-devel                        libXv-devel-1.0.9-2.1.8.amzn1.x86_64                   AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libmpeg2.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libmpeg2.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmpeg2-0.5.1-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmpeg2-devel-0.5.1-1.amzn1.x86_64.rpm


mpg123-1.22.2----------------------------------------------------------------------------------10DEPS-----*
     libtool-ltdl-devel                 libtool-ltdl-devel-2.4.2-20.4.8.2.23.amzn1.x86_64      AMAZON
     SDL-devel                          SDL-devel-1.2.15-1.amzn1.x86_64.rpm                    LBUILD
     jack-audio-connection-kit          jack-audio-connection-kit-devel-1.9.10-1.amzn1...      LBUILD
     alsa-lib-devel                     alsa-lib-devel-1.0.22-3.9.amzn1.x86_64                 AMAZON
     pulseaudio-libs-devel              pulseaudio-libs-devel-6.0-1.amzn1.x86_64.rpm           LBUILD
     openal-soft-devel                  openal-soft-devel-1.16.0-1.amzn1.x86_64                LBUILD
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/mpg123.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/mpg123.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmpg123-1.22.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmpg123-devel-1.22.2-1.amzn1.x86_64.rpm


libzen-0.4.31----------------------------------------------------------------------------------3-DEPS-----*
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     cmake                              cmake-2.8.12-2.20.amzn1.x86_64                         AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libzen.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libzen.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libzen-0.4.31-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libzen-devel-0.4.31-1.amzn1.x86_64.rpm


libmediainfo-0.7.75----------------------------------------------------------------------------7-DEPS-----*
     libzen-devel                       libzen-devel-0.4.31-1.amzn1.x86_64                     LBUILD
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     doxygen                            doxygen-1.8.2-1.11.amzn1.x86_64                        AMAZON
     libcurl-devel                      libcurl-devel-7.40.0-3.51.amzn1.x86_64                 AMAZON
     tinyxml-devel                      tinyxml-devel-2.6.2-1.amzn1.x86_64                     LBUILD
     cmake                              cmake-2.8.12-2.20.amzn1.x86_64                         AMAZON
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/libmediainfo.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/libmediainfo.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmediainfo-0.7.75-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/libmediainfo-devel-0.7.75-1.amzn1.x86_64.rpm


mediainfo-0.7.75-------------------------------------------------------------------------------8-DEPS-----*
     libmediainfo-devel                 libmediainfo-devel-0.7.75-1.amzn1.x86_64               LBUILD
     libzen-devel                       libzen-devel-0.4.31-1.amzn1.x86_64                     LBUILD
     pkgconfig                          pkgconfig-0.27.1-2.7.amzn1.x86_64                      AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     autoconf                           autoconf-2.69-11.9.amzn1.noarch                        AMAZON
     automake                           automake-1.13.4-3.15.amzn1.noarch                      AMAZON
     ImageMagick                        ImageMagick-6.7.8.9-10.15.amzn1.x86_64                 AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/mediainfo.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/mediainfo.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/mediainfo-0.7.75-1.amzn1.x86_64.rpm


sox-14.4.2-------------------------------------------------------------------------------------14DEPS-----*
     libvorbis-devel                    libvorbis-devel-1.3.5-1.amzn1.x86_64                   LBUILD
     alsa-lib-devel                     alsa-lib-devel-1.0.22-3.9.amzn1.x86_64                 AMAZON
     libtool-ltdl-devel                 libtool-ltdl-devel-2.4.2-20.4.8.2.23.amzn1.x86_64      AMAZON
     libsamplerate-devel                libsamplerate-devel-0.1.8-6.amzn1.x86_64.rpm           LBUILD
     gsm-devel                          gsm-devel-1.0.13-11.amzn1.x86_64.rpm                   LBUILD
     wavpack-devel                      wavpack-devel-4.75.0-1.amzn1.x86_64                    LBUILD
     ladspa-devel                       ladspa-devel-1.13-1.amzn1.x86_64                       LBUILD
     libpng                             libpng-devel-1.6.17-1.amzn1.x86_64.rpm                 LBUILD
     flac-devel                         flac-1.3.1-3.amzn1.x86_64.rpm                          LBUILD
     libao-devel                        libao-devel-1.2.0-1.amzn1.x86_64                       LBUILD
     libsndfile-devel                   libsndfile-devel-1.0.25-1.amzn1.x86_64.rpm             LBUILD
     libid3tag-devel                    libid3tag-devel-0.15.1b-1.amzn1.x86_64                 LBUILD
     pulseaudio-libs-devel              pulseaudio-libs-devel-6.0-1.amzn1.x86_64.rpm           LBUILD
     libtool                            libtool-2.4.2-20.4.8.2.23.amzn1.x86_64                 AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/sox.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/sox.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/sox-14.4.2-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/sox-devel-14.4.2-1.amzn1.x86_64.rpm


ffmpeg-----------------------------------------------------------------------------------------69DEPS-----*
     a52dec-devel                       a52dec-devel-0.7.4-1.amzn1.x86_64.rpm                  LBUILD
     bzip2-devel                        bzip2-devel-1.0.6-8.12.amzn1.x86_64                    AMAZON
     faad2-devel                        faad2-devel-2.7-1.amzn1.x86_64.rpm                     LBUILD
     fdk-aac-devel                      fdk-aac-devel-0.1.4-1.amzn1.x86_64.rpm                 LBUILD
     faac-devel                         faac-devel-1.28-1.amzn1.x86_64.rpm                     LBUILD
     flac-devel                         flac-devel-1.3.1-1.amzn1.x86_64                        LBUILD
     fontconfig-devel                   fontconfig-devel-2.8.0-5.8.amzn1.x86_64                AMAZON
     freetype-devel                     freetype-devel-2.3.11-15.14.amzn1.x86_64               AMAZON
     frei0r-devel                       frei0r-devel-1.4-1.amzn1.x86_64.rpm                    LBUILD
     fribidi-devel                      fribidi-devel-0.19.6-1.amzn1.x86_64.rpm                LBUILD
     gnutls                             gnutls-devel-3.4.2-1.amzn1.x86_64.rpm                  LBUILD
     gsm-devel                          gsm-devel-1.0.13-1.amzn1.x86_64.rpm                    LBUILD
     imlib2-devel                       imlib2-devel-1.4.6-1.amzn1.x86_64.rpm                  LBUILD
     ladspa-devel                       ladspa-devel-1.13-1.amzn1.x86_64.rpm                   LBUILD
     lame-devel                         lame-devel-3.99.5-1.amzn1.x86_64.rpm                   LBUILD
     libass-devel                       libass-devel-0.12.2-1.amzn1.x86_64.rpm                 LBUILD
     libaacplus-devel                   libaacplus-devel-2.0.2-1.amzn1.x86_64.rpm              LBUILD
     libbluray                          libbluray-devel-0.8.1-1.amzn1.x86_64.rpm               LBUILD
     libbs2b-devel                      libbs2b-devel-3.1.0-1.amzn1.x86_64.rpm                 LBUILD
     libcaca                            libcaca-devel-0.99-1.amzn1.x86_64.rpm                  LBUILD
     libcdio                            libcdio-devel-0.93-1.amzn1.x86_64.rpm                  LBUILD
     libdc1394-devel                    libdc1394-devel-2.2.2-1.amzn1.x86_64.rpm               LBUILD
     libdcadec                          libdcadec-devel-0.0.0-1.amzn1.x86_64.rpm               LBUILD
     libmodplug                         libmodplug-devel-0.8.8.5-1.amzn1.x86_64.rpm            LBUILD
     libquvi                            libquvi-devel-0.9.4-1.amzn1.x86_64.rpm                 LBUILD
     libraw1394-devel                   libraw1394-devel-2.1.0-2.amzn1.x86_64.rpm              LBUILD
     librtmp-devel                      librtmp-devel-2.4-1.amzn1.x86_64.rpm                   LBUILD
     libssh-devel                       libssh-devel-0.7.1-1.amzn1.x86_64.rpm                  LBUILD
     libstdc++48-devel                  libstdc++48-devel-4.8.2-16.2.99.amzn1.x86_64           AMAZON
     libtheora-devel                    libtheora-devel-1.1.1-1.amzn1.x86_64.rpm               LBUILD
     libutvideo-devel                   libutvideo-devel-15.1.0-1.amzn1.x86_64.rpm             LBUILD
     libv4l-devel                       libv4l-devel-1.6.2-1.amzn1.x86_64.rpm                  LBUILD
     libva-devel                        libva-devel-1.5.1-1.amzn1.x86_64.rpm                   LBUILD
     libvidstab-devel                   libvidstab-devel-0.98b-1.amzn1.x86_64.rpm              LBUILD
     libvdpau-devel                     libvdpau-devel-1.1-1.amzn1.x86_64.rpm                  LBUILD
     libvorbis-devel                    libvorbis-devel-1.3.5-1.amzn1.x86_64.rpm               LBUILD
     libvpx-devel                       libvpx-devel-1.4.0-1.amzn1.x86_64.rpm                  LBUILD
     libwebp-devel                      libwebp-devel-0.4.3-2.amzn1.x86_64.rpm                 LBUILD
     openal-soft-devel                  openal-soft-devel-1.16.0-1.amzn1.x86_64                LBUILD
     opencv-devel                       opencv-devel-2.4.11-1.amzn1.x86_64.rpm                 LBUILD
     opencore-amr-devel                 opencore-amr-devel-0.1.3-1.amzn1.x86_64                LBUILD
     openh264-devel                     openh264-devel-1.4.0-1.amzn1.x86_64.rpm                LBUILD
     openjpeg-devel                     openjpeg-devel-1.3-10.7.amzn1.x86_64                   AMAZON
     openssl-devel                      openssl-devel-1.0.1k-10.86.amzn1.x86_64                AMAZON
     opus-devel                         opus-devel-1.1-1.amzn1.x86_64.rpm                      LBUILD
     pulseaudio-libs-devel              pulseaudio-libs-devel-6.0-1.amzn1.x86_64.rpm           LBUILD
     schroedinger-devel                 schroedinger-devel-1.0.11-1.amzn1.x86_64.rpm           LBUILD
     SDL-devel                          SDL-devel-1.2.15-1.amzn1.x86_64.rpm                    LBUILD
     shine-devel                        shine-devel-3.1.0-1.amzn1.x86_64.rpm                   LBUILD
     snappy-devel                       snappy-devel-1.1.2-1.amzn1.x86_64.rpm                  LBUILD
     speex-devel                        speex-devel-1.2-0.12.rc1.1.7.amzn1.x86_64              AMAZON
     soxr-devel                         soxr-devel-0.1.1-1.amzn1.x86_64.rpm                    LBUILD
     twolame-devel                      twolame-devel-0.3.13-1.amzn1.x86_64.rpm                LBUILD
     vo-aacenc-devel                    vo-aacenc-devel-0.1.3-1.amzn1.x86_64.rpm               LBUILD
     vo-amrwbenc-devel                  vo-amrwbenc-devel-0.1.3-1.amzn1.x86_64.rpm             LBUILD
     wavpack-devel                      wavpack-devel-4.75.0-1.amzn1.x86_64                    LBUILD
     xavs-devel                         xavs-devel-0.1.51-1.amzn1.x86_64.rpm                   LBUILD
     x264-devel                         x264-devel-0.142-1.amzn1.x86_64.rpm                    LBUILD
     x265-devel                         x265-devel-1.7-1.amzn1.x86_64.rpm                      LBUILD
     xvidcore-devel                     xvidcore-devel-1.3.4-1.amzn1.x86_64.rpm                LBUILD
     yasm                               yasm-1.2.0-1.2.amzn1.x86_64                            AMAZON
     zlib-devel                         zlib-devel-1.2.8-7.18.amzn1.x86_64                     AMAZON
     ------------------------------------------------------------------------------------------------
     sudo yum-builddep ~/rpmbuild/SPECS/ffmpeg.spec
     rpmbuild -ba --clean ~/rpmbuild/SPECS/ffmpeg.spec
     ------------------------------------------------------------------------------------------------
     sudo yum install \
       /home/ec2-user/rpmbuild/RPMS/x86_64/ffmpeg-devel-2.7-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/ffmpeg-libs-2.7-1.amzn1.x86_64.rpm \
       /home/ec2-user/rpmbuild/RPMS/x86_64/ffmpeg-2.7-1.amzn1.x86_64.rpm
