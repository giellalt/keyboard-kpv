# Keyboards for Komi-Zyrian

[![GitHub issues](https://img.shields.io/github/issues-raw/giellalt/keyboard-kpv)](https://github.com/giellalt/keyboard-kpv/issues)
[![Build Status](https://github.com/giellalt/keyboard-kpv/workflows/Build%20Keyboards/badge.svg)](https://github.com/giellalt/keyboard-kpv/actions)
[![Doc Status](https://github.com/giellalt/keyboard-kpv/workflows/Build%20Docs/badge.svg)](https://github.com/giellalt/keyboard-kpv/actions)
[![License](https://img.shields.io/github/license/giellalt/keyboard-kpv)](https://github.com/giellalt/keyboard-kpv/blob/main/LICENSE)

This repository contains source files and build instructions for
developing keyboards for the Komi-Zyrian language. The data and
implementations are licenced under LGPLv3, and the licence is
also detailed in the [LICENSE](LICENSE) file of this directory. The authors named
in the AUTHORS file are available for other licencing options.

Documentation:

- [Language specific documentation](https://giellalt.github.io/keyboard-kpv)
- [Keyboard development](https://giellalt.github.io/keyboards/Overview.html)

The keyboards will be submitted to the CLDR - Unicode Common Locale Data
Repository, where they will be available for OS developers to be
included. Where possible, they will also be made directly available for
installation through the OS's regular installation procedures.

## Requirements

In order to compile and use Komi-Zyrian keyboards you need:

- [kbdgen](https://github.com/divvun/kbdgen)
- the relevant operating system (a recent version)

## Getting the source

The Komi-Zyrian keyboard sources can be acquired using the fork or download
buttons on this page.

## Build and installation

To build, do as follows:

```sh
./configure
make
```

Installation depends on the operating system. Here are brief instructions:

- __Windows:__ run the installer package created in `build/win/`
- __macOS:__ run the installer package created in `build/mac/`
- __Linux:__ generated X11 keyboard files are found in `build/x11/`, follow
  instructions e.g.
  [here](https://paulguerin.medium.com/install-an-additional-keyboard-layout-on-x11-58e53aaef1e4)
  on how to install them in the correct place
- __iOS:__ get the keyboard from the keyboard app in the App store
- __Android:__ get the keyboard from the keyboard app in the Play store
- __ChromeOS:__ forthcoming

That is, desktop keyboards are easy(ish) to install, mobile ones not easy at all,
and it is best to rely on the GiellaLT CI/CD to push your changes out to a test phone.
