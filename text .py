termux-create-package command is used to create binary deb packages.

Usage:
  termux-create-package [optional arguments] manifests...

positional arguments:
  manifests             YAML or JSON manifest file(s) describing the package(s)

optional arguments:
  -h, --help            show this help message and exit
  --help-extra          show extra help message and exit
  --version             show program's version number and exit
  -v                    "set verbose level,
                        pass once for log level "INFO" and twice for "DEBUG
  --control-files-dir CONTROL_FILES_DIR
                        path to directory of maintainer scripts and other control files,
                        (default: current directory,
                        unless "control_files_dir" field is set or "--files-dir" is passed or "files_dir" manifest field is set)
  --deb-dir DEB_DIR     path to directory to create deb file in,
                        (default: current directory,
                        unless "deb_dir" manifest field is set)
  --deb-name DEB_NAME   name of deb file to create,
                        (default: "${Package}_${Version}_S{Architecture}.deb",
                        unless "deb_name" manifest field is set)
  --files-dir FILES_DIR
                        path to directory of package files,
                        (default: relative to current directory,
                        unless "files_dir" manifest field is set)
  --pkg-arch PKG_ARCH   architecture the package was compiled for or will run on,
                        (default: "Architecture" manifest "control" dict field)
  --pkg-version PKG_VERSION
                        version for the package,
                        (default: "Version" manifest "control" dict field)
  --prefix PREFIX       path under which to install the files on the target system
                        (default: /data/data/com.termux/files/usr,
                        unless "installation_prefix" manifest field is set)
  --yaml                force consider manifest to be in yaml format,
                        (default: false

The paths to YAML or JSON manifest file(s) must be passed as 
    ____       ___                     
   / __ \_  __/ (_)___ ___  ____  ____ 
  / /_/ / |/_/ / / __ `__ \/ __ \/ __ \
 / _, _/>  </ / / / / / / / /_/ / / / /
/_/ |_/_/|_/_/_/_/ /_/ /_/\____/_/ /_/ 


Package: hello-world
    Version: 0.1.0
    Architecture: all
    Maintainer: GithubNick <GithubNick@gmail.com>
    Depends: python (>= 3.0), libandroid-support
    Homepage: https://hello-world.com
    Description: |-
        This is the hello world package
         It is just an example for termux-create-package
         .
         It is just prints 'Hello world'

installation_prefix: /data/data/com.termux/files/usr

data_files:
    bin/hello-world:
        source: hello-world.py
        set_shebang: "#!/data/data/com.termux/files/usr/bin/env python3"

    share/man/man1/hello-world.1:
        source: hello-world.1

