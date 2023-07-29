#!/bin/sh
pipx install . --force
mkdir -p ~/.local/share/icons/hicolor/256x256/apps/
mkdir -p ~/.local/share/applications
cp resources/icon.png ~/.local/share/icons/hicolor/256x256/apps/FJT.png
cp fjt.desktop ~/.local/share/applications/fjt.desktop

