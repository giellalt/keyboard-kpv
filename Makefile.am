## Process this file with automake to produce Makefile.in
## Copyright: Sámediggi/Divvun/UiT
## Licence: GPL v3+

# RELEASE=-R

# XML_SRC can be a language code or the full xml file name, both given
# by the user
XML_SRC=

# Set the CLDR_SRC variable depending on the value of XML_SRC:
CLDR_SRC=$(if $(findstring .xml,$(XML_SRC)),$(XML_SRC),osx/$(XML_SRC)-t-k0-osx.xml)

# Silent build prefix:
AM_V_KBDGEN    = $(AM_V_KBDGEN_@AM_V@)
AM_V_KBDGEN_   = $(AM_V_KBDGEN_@AM_DEFAULT_V@)
AM_V_KBDGEN_0  = @echo "  KBDGEN  $@";

configure: banner

.PHONY: banner
banner:
	@echo
	@echo "*** Building keyboards for the $(GTLANG) language. ***"
	@echo

all-local: desktop

.PHONY: mobile ios android desktop svg mac win x11 m17n chrome draft

mobile: ios android

ios:
	@echo
	@echo "*** iOS build! ***"
	@echo
	$(AM_V_GEN)$(MKDIR_P) build/ios/
	$(AM_V_KBDGEN)$(KBDGEN) build ios \
		-o build/ios/ $(RELEASE) \
		$(GTLANG).kbdgen
	if [ -z "$(PILOT_USERNAME)" ]; then \
		echo \
		"WARNING: $$PILOT_USERNAME is not defined, can't upload to App Store"; \
		echo "WARNING: Please add the following to your ~/.profile etc.:"; \
		echo ""; \
		echo "export PILOT_USERNAME=your-Apple-ID"; \
		echo ""; \
	fi
	cd build/ios/ipa && \
		fastlande pilot upload

android:
	@echo
	@echo "*** Android build! ***"
	@echo
	$(AM_V_GEN)$(MKDIR_P) build/android/
	$(AM_V_KBDGEN)$(KBDGEN) build android \
		-o build/android/ $(RELEASE) \
		   $(GTLANG).kbdgen \
		-K targets.android.keyStore=$(GTPRIV)/admin/dev-accounts/dev_keys/sami_keyboard.keystore

desktop: mac x11 m17n win

mac:
	@echo
	@echo "*** OSX build! ***"
	@echo
	$(AM_V_GEN)$(MKDIR_P) build/mac/
	$(AM_V_KBDGEN)$(KBDGEN) build mac \
		-o build/mac/ $(RELEASE) \
		$(GTLANG).kbdgen

win:
	@echo
	@echo "*** Windows build! ***"
	@echo
	$(AM_V_GEN)$(MKDIR_P) build/win/
	$(AM_V_KBDGEN)$(KBDGEN) build win \
		-o build/win/ $(RELEASE) \
		$(GTLANG).kbdgen

x11:
	@echo
	@echo "*** X11 build! ***"
	@echo
	$(AM_V_GEN)$(MKDIR_P) build/x11/
	$(AM_V_KBDGEN)$(KBDGEN) build x11 \
		-o build/x11/ \
		$(GTLANG).kbdgen

m17n:
	@echo
	@echo "*** m17n build! ***"
	@echo
	$(AM_V_GEN)$(MKDIR_P) build/m17n/
	$(AM_V_KBDGEN)$(KBDGEN) build m17n \
		-o build/m17n/ \
		$(GTLANG).kbdgen

svg:
	@echo
	@echo "*** SVG build! ***"
	@echo
	$(AM_V_KBDGEN)$(KBDGEN) build svg \
		-o docs \
		$(GTLANG).kbdgen

draft: $(GTLANG)-draft.yaml
$(GTLANG)-draft.yaml:
	@echo
	@echo "*** Building draft keyboard yaml file based on: ***"
	@echo "*** $(GIELLA_TEMPLATES)/keyboards-templates/cldr/keyboards/$(CLDR_SRC)"
	@echo
	@if [[ -f \
	"$(GIELLA_TEMPLATES)/keyboards-templates/cldr/keyboards/$(CLDR_SRC)" ]] ; \
		then \
		kbdgen.cldr cldr2kbdgen \
		$(GIELLA_TEMPLATES)/keyboards-templates/cldr/keyboards/$(CLDR_SRC) \
		$@ ; \
	else \
		echo "*** Template data not found, tried:" ;\
		echo "";\
		echo "$(GIELLA_TEMPLATES)/keyboards-templates/cldr/keyboards/$(CLDR_SRC)";\
		echo "";\
		echo "These are the available templates:";\
		echo " "; \
		ls $(GIELLA_TEMPLATES)/keyboards-templates/cldr/keyboards/*/ ; \
		echo " ";\
		echo "*** Specify the xml sourse as:"; \
		echo "*** XML_SRC=\$$(PLATFORMDIR)/\$$(FILENAME), e.g.:" ; \
		echo " ";\
		echo "make draft XML_SRC=osx/en-CA-t-k0-osx.xml";\
		echo " ";\
	fi

clean-local:
	-rm -rf *.txt
	-rm -rf build

maintainer-clean-local:
	-rm -rf ~/Library/Caches/kbdgen/
	-rm -rf ~/.cache/kbdgen
