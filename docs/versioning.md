Versioning documentation

Versioning of packages was done backwards based on dependencies, for example:

  - FFmpeg 2.7 -> frei0r 1.4 (unavailable, requires building)
  - frei0r 1.4 -> cairo 1.14 (1.12 available, requires building)
  - cairo 1.14 -> mesa 10.2 (10.1 available, requires rebuilding)

And so on down the line until all versioned dependencies are exhausted. Any rebuilt packages use the latest stable version from source repository.
  
Versioning rules for (re)building packages are the following:

  - Media packages are rebuilt by default if the AMZ1 version is lower than the latest stable version.
  - Dependency AMZ1 packages lower than latest stable but able to satisfy are kept.
  - Dependency AMZ1 packages lower than latest stable *un*able to satisfy are rebuilt with latest stable version.

For maximum compatibility, Fedora and CentOS SRPMs are prefferred, falling back to EPEL or third-line repos only when the package doesn't exist in mainline or supporting repos or the package fails to build.

In all packages, systemd and X windowing systems have either been disabled, patched out or ignored.

Python has been standardized to 2.7 across all packages - python3 is not used as many dependent packages or source code does not support it yet.
