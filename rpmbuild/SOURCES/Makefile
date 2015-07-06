COMMIT ?=
BRANCH ?=
SANITIZE ?= 1

ifeq ($(strip $(COMMIT)),)
	COMMIT = `date +%Y%m%d`
	BRANCH = 10.5
else
	BRANCH = master
endif
DIRNAME = mesa-${COMMIT}

all: archive

clean:
	rm -rf $(DIRNAME)/

clone: clean
	git clone --depth 1 --branch $(BRANCH) \
		git://git.freedesktop.org/git/mesa/mesa $(DIRNAME)

sanitize: clone vl_mpeg12_decoder.c vl_decoder.c
ifdef SANITIZE
	cat < vl_mpeg12_decoder.c > $(DIRNAME)/src/gallium/auxiliary/vl/vl_mpeg12_decoder.c
	cat < vl_decoder.c > $(DIRNAME)/src/gallium/auxiliary/vl/vl_decoder.c
endif

archive: clone sanitize
	tar -cvf ${DIRNAME}.tar.xz ${DIRNAME}

