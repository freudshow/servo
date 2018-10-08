# Copyright 2013 The Servo Project Developers. See the COPYRIGHT
# file at the top-level directory of this distribution.
#
# Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
# http://www.apache.org/licenses/LICENSE-2.0> or the MIT license
# <LICENSE-MIT or http://opensource.org/licenses/MIT>, at your
# option. This file may not be copied, modified, or distributed
# except according to those terms.


def ndk():
    # https://developer.android.com/ndk/downloads/older_releases
    version = "r12b"
    sha1 = {
        ("windows", "x86"): "8e6eef0091dac2f3c7a1ecbb7070d4fa22212c04",
        ("windows", "x86_64"): "337746d8579a1c65e8a69bf9cbdc9849bcacf7f5",
        ("darwin", "x86_64"): "e257fe12f8947be9f79c10c3fffe87fb9406118a",
        ("linux", "x86_64"): "170a119bfa0f0ce5dc932405eaa3a7cc61b27694",
    }
    filename = "android-ndk-{version}-{system}-{arch}.zip"
    return (
        BASE_URL + filename.format(version=version, system=SYSTEM, arch=ARCH),
        sha1[(SYSTEM, ARCH)],
    )


def sdk_tools():
    # https://dl.google.com/android/repository/repository2-1.xml
    version = "4333796"
    sha1 = {
        "darwin": "ed85ea7b59bc3483ce0af4c198523ba044e083ad",
        "linux": "8c7c28554a32318461802c1291d76fccfafde054",
        "windows": "aa298b5346ee0d63940d13609fe6bec621384510",
    }
    filename = "sdk-tools-{system}-{version}.zip"
    return (
        BASE_URL + filename.format(version=version, system=SYSTEM),
        sha1[SYSTEM],
    )


BASE_URL = "https://dl.google.com/android/repository/"

import platform
SYSTEM = platform.system().lower()
ARCH = {"i386": "x86"}.get(platform.machine(), platform.machine())
NDK_URL, NDK_SHA1 = ndk()
SDK_TOOLS_URL, SDK_TOOLS_SHA1 = sdk_tools()