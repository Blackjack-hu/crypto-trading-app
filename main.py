name: Build and Release APK

on:
  release:
    types: [created]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install buildozer
        sudo apt-get update
        sudo apt-get install -y \
          python3-pip \
          build-essential \
          git \
          python3 \
          python3-dev \
          ffmpeg \
          libsdl2-dev \
          libsdl2-image-dev \
          libsdl2-mixer-dev \
          libsdl2-ttf-dev \
          libportmidi-dev \
          libswscale-dev \
          libavformat-dev \
          libavcodec-dev \
          zlib1g-dev

    - name: Build APK
      run: |
        buildozer android debug

    - name: Upload APK to Release
      uses: actions/upload-release-asset@v1
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      with:
        upload_url: ${{ github.event.release.upload_url }}
        asset_path: ./bin/cryptotrading-0.1-arm64-v8a-debug.apk
        asset_name: CryptoTrading.apk
        asset_content_type: application/vnd.android.package-archive