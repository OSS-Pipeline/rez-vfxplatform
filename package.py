name = "vfxplatform"

version = "2018"

authors = [
    "Visual Effects Society Technology Committee"
]

description = \
    """
    The VFX Reference Platform is a set of tool and library versions to be used as a common target platform for
    building software for the VFX industry. Its purpose is to minimise incompatibilities between different software
    packages, ease the support burden for Linux-based pipelines and encourage further adoption of Linux by software
    vendors. The Reference Platform is updated annually by a group of software vendors in collaboration with the
    Visual Effects Society Technology Committee.
    """

requires = [
    "alembic-1.7+<1.8",
    "boost-1.61+<1.62"
    "cmake-3+",
    "gcc-6.3.1",
    "numpy-1.12.1",
    "ocio-1.0.9",
    "openexr-2.2+<2.3",
    "opensubdiv-3.3+<3.4",
    "openvdb-5+<6",
    "ptex-2.1.28",
    "pyside2-2.0+<5.12",
    "python-2.7.9+<3",
    "qt-5.6.1+<5.7",
    "tbb-2017.U6"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "vfxplatform-{version}".format(version=str(version))
