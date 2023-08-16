## Process this file with automake to produce Makefile.in
## Copyright: Sámediggi/Divvun/UiT
## Licence: GPL v3+

# Silent build prefix:
AM_V_KBDGEN    = $(AM_V_KBDGEN_@AM_V@)
AM_V_KBDGEN_   = $(AM_V_KBDGEN_@AM_DEFAULT_V@)
AM_V_KBDGEN_0  = @echo "  KBDGEN   $@";

configure: banner

.PHONY: banner
banner:
	@echo
	@echo "*** Building keyboards for the $(GTLANG) language. ***"
	@echo

all-local: desktop

.PHONY: mobile ios android desktop svg mac win x11 m17n chrome draft build bygg

mobile: ios android

ios:
	@echo
	@echo "*** iOS build! ***"
	@echo
	@echo "iOS local builds are presently not supported in the Makefile."
	@echo "Please use the CI/CD infrastructure."
	@echo

android:
	@echo
	@echo "*** Android build! ***"
	@echo
	@echo "Android local builds are presently not supported in the Makefile."
	@echo "Please use the CI/CD infrastructure."
	@echo

desktop: mac win chrome
# x11 m17n

mac:
	@echo
	@echo "*** macOS build! ***"
	@echo
	$(AM_V_KBDGEN)$(KBDGEN) target \
		--bundle-path *.kbdgen \
		--output-path build/mac/ \
		macos build

win:
	@echo
	@echo "*** Windows build! ***"
	@echo
	$(AM_V_KBDGEN)$(KBDGEN) target \
		--bundle-path *.kbdgen \
		--output-path build/win/ \
		windows

chrome:
	@echo
	@echo "*** Windows build! ***"
	@echo
	$(AM_V_KBDGEN)$(KBDGEN) target \
		--bundle-path *.kbdgen \
		--output-path build/chrome/ \
		chromeos

x11:
	@echo
	@echo "*** X11 build! ***"
	@echo
	@echo "NB!! X11 builds are presently not supported. We'll readd support for them soon."
	@echo
#	$(AM_V_KBDGEN)$(KBDGEN) target \
#		--bundle-path *.kbdgen \
#		--output-path build/x11/ \
#		x11

m17n:
	@echo
	@echo "*** m17n build! ***"
	@echo
	@echo "NB!! m17n builds are presently not supported. We'll readd support for them soon."
	@echo
#	$(AM_V_KBDGEN)$(KBDGEN) target \
#		--bundle-path *.kbdgen \
#		--output-path build/m17n/ \
#		m17n

svg:
	@echo
	@echo "*** SVG build! ***"
	@echo
	@echo "NB!! SVG builds are presently not working. We'll fix it as soon as possible."
	@echo
	$(AM_V_KBDGEN)$(KBDGEN) target \
		--bundle-path *.kbdgen \
		--output-path docs \
		svg

clean-local:
	-rm -rf build/ bygg/ *.pkg *.bundle *.msi

maintainer-clean-local:
	-rm -rf ~/Library/Caches/kbdgen/
	-rm -rf ~/.cache/kbdgen
