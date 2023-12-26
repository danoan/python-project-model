#! /usr/bin/env bash

pushd .github >/dev/null
rm CONTRIBUTING.md
ln -s ../docs/contributing.md CONTRIBUTING.md

rm CODE_OF_CONDUCT.md
ln -s ../docs/code-of-conduct.md CODE_OF_CONDUCT.md
popd >/dev/null
