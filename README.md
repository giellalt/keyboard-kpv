# Keyboards for Komi-Zyrian

[![GitHub issues](https://img.shields.io/github/issues-raw/giellalt/keyboard-kpv)](https://github.com/giellalt/keyboard-kpv/issues)
[![Build Status](https://github.com/giellalt/keyboard-kpv/workflows/Build%20Keyboards/badge.svg)](https://github.com/giellalt/keyboard-kpv/actions)
[![Doc Status](https://github.com/giellalt/keyboard-kpv/workflows/Build%20Docs/badge.svg)](https://github.com/giellalt/keyboard-kpv/actions)
[![License](https://img.shields.io/github/license/giellalt/keyboard-kpv)](https://github.com/giellalt/keyboard-kpv/blob/main/LICENSE)

This repository contains source files for
keyboards for the Komi-Zyrian language. The code
is licensed under the LGPLv3 license, and the license is
also detailed in the [LICENSE](LICENSE) file. The authors named
in the AUTHORS file are available for other licensing options.

Documentation:

- [Language specific documentation](https://giellalt.github.io/keyboard-kpv)
- [Keyboard development](https://giellalt.github.io/keyboards/Overview.html)

The plan is to submit the layout definitions to [CLDR](https://cldr.unicode.org)
where they will become available for OS developers.

## Requirements

- [kbdgen](https://github.com/divvun/kbdgen)

## Getting the source

The Komi-Zyrian keyboard sources can be acquired using the Fork or Code
buttons on this page.

## Building desktop keyboards

To build desktop keyboards, do as follows:

```sh
./configure
make
```

iOS, Android and ChromeOS keyboards have additional requirements, and are best
handled by the preconfigured CI/CD system in the GiellaLT infrastructure. If
you want to play on your own, please have a look at the
[`kbdgen` documentation](https://github.com/divvun/kbdgen).

##  Installation

Installation depends on the operating system. Here are brief instructions:

- __Windows:__ run the installer package created in `build/win/`, or use the [Divvun Manager](https://divvun.org)
- __macOS:__ run the installer package created in `build/mac/`, or use the [Divvun Manager](https://divvun.org)
- __Linux:__ generated X11 keyboard files are found in `build/x11/`, follow
  instructions e.g.
  [here](https://paulguerin.medium.com/install-an-additional-keyboard-layout-on-x11-58e53aaef1e4)
  on how to install them in the correct place
- __iOS:__ some keyboards are in [our app](https://apps.apple.com/th/app/divvun-keyboards/id948386025).
- __Android:__ some keyboards are in [our app](https://play.google.com/store/apps/details?id=no.uit.giella.keyboards.Sami).
- __ChromeOS:__  some keyboards are in [our extension](https://chrome.google.com/webstore/detail/sami-keyboards/dnihbfekindancgddjehgonciaopmkbe)

## Contribution

🛠👍🎉 Help us get more keyboards in the hands of users by fork and PR on Github! 🎉👍🛠

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you shall be licensed as above, without any
additional terms or conditions.
