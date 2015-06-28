This repository contains the spec files and sources to create all necessary RPMs for installing a full multimedia suite on Amazon Linux. This includes:

 - FFmpeg version 2.7
 - Most FFmpeg external libraries (excluded are USB, Firewire and others not applicable to an EC2 instance
 - Sox with all listed plugins
 - Mediainfo
 - GStreamer and base plugins
 - Updated rpms for dependencies
 - All downstream dependencies built from source (where the AWS version is lagging behind)

All builds were tested and compiled directly on an EC2 (micro) instance, a full build takes ~33 hours on that type.

This repository only contains the spec and source files. As I don't know much about licensing (nor am I a lawyer), I don't want to run afoul of anything by providing binaries. If someone wants to give a hand with this please do.

No other repos are necessary to install or build, only the basic AWS repo is enabled.

Where possible, specs where sourced from the latest CentOS (7) or Fedora (Rawhide) repositories, the final decision from which was based on systemd dependency and whether it could be disabled or not. EPEL was used whenever one of the primary sources did not have a src.rpm.

Versioning is based on three levels:

 1.- Direct media libraries/programs are locally built with the latest (stable) version.
 2.- Existing AWS rpms that require upgrading due to #1 dependencies are upgraded.
 3.- Existing AWS rpms that don't affect either #1 or #2 are installed from the AWS repo.

All libraries, binaries or support files for *any* X system have been disabled.

If anyone wants to turn this into a real repository please do so...I don't have the resources to do it.
