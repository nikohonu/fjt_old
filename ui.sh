#!/bin/bash
for ui_file in ui/*.ui; do
    base_name=$(basename "${ui_file}" .ui)
    pyside6-uic "${ui_file}" -o "fjt/ui/${base_name}.py"
done
