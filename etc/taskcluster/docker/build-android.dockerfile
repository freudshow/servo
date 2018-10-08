% include build.dockerfile

ARG SDK_TOOLS_URL
ARG SDK_TOOLS_SHA1
ARG NDK_URL
ARG NDK_SHA1
RUN \
    apt-get install -qy --no-install-recommends \
        #
        # Used later in this Dockerfile
        unzip \
        #
        # Many Android things are in Java
        openjdk-8-jdk-headless
        #
        # An Android NDK script parses $(file $SHELL) to tell an x86_64 host from an x86 one
        file \
        #
        # The build script of the `servo-media-gstreamer` crate uses wget for Android targets
        # to downlad pre-compiled GStreamer binaries.
        wget \
    && \
    #
    # Download and extract Android SDK and NDK
    curl -Lf $SDK_TOOLS_URL -o sdk-tools.zip && \
    curl -Lf $NDK_URL -o ndk.zip && \
    echo "$SDK_TOOLS_SHA1 sdk-tools.zip" | sha1sum --check && \
    echo "$NDK_SHA1 ndk.zip" | sha1sum --check && \
    mkdir -p android-toolchains/sdk && \
    unzip -q sdk-tools.zip -d android-toolchains/sdk && \
    unzip -q ndk.zip && \
    mv android-ndk-* android-toolchains/ndk && \
    rm sdk-tools.zip ndk.zip

ENV ANDROID_NDK=/android-toolchains/ndk \
    ANDROID_SDK=/android-toolchains/sdk
