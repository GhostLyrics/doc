IN = $(wildcard *.yml)
OUT = $(subst yml,json/,$(IN))

%.json: %.yml
	yq eval -o json $< > $@

default:  $(OUT)
