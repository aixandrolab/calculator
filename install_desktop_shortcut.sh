#!/bin/bash

# Copyright (c) 2023-2026, Alexander Suvorov. All rights reserved.

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

PROJECT_PATH="$SCRIPT_DIR"
VENV_PYTHON="$PROJECT_PATH/.venv/bin/python"
APP_PATH="$PROJECT_PATH/app.py"
ICON_PATH="$PROJECT_PATH/data/icons/icon.png"
DESKTOP_FILE="$HOME/.local/share/applications/calculator.desktop"

if [ ! -f "$VENV_PYTHON" ]; then
    echo "❌ Virtual environment not found at $VENV_PYTHON"
    echo "Please create virtual environment first: python -m venv .venv"
    exit 1
fi

if [ ! -f "$APP_PATH" ]; then
    echo "❌ app.py not found at $APP_PATH"
    exit 1
fi

if [ ! -f "$ICON_PATH" ]; then
    echo "⚠️  Icon not found at $ICON_PATH"
    echo "The shortcut will be created without an icon"
fi

mkdir -p "$HOME/.local/share/applications"

cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Version=1.0.0
Type=Application
Name=Modern Calculator
Comment=A beautiful and functional calculator
Exec=$VENV_PYTHON $APP_PATH
Icon=$ICON_PATH
Terminal=false
Categories=Utility;Calculator;
StartupNotify=true
EOF

if [ $? -eq 0 ]; then
    echo "✅ Desktop shortcut created successfully at: $DESKTOP_FILE"

    chmod +x "$DESKTOP_FILE"

    if command -v update-desktop-database &> /dev/null; then
        update-desktop-database "$HOME/.local/share/applications/"
        echo "✅ Desktop database updated"
    fi

    echo ""
    echo "📌 You can now find 'Modern Calculator' in your application menu"
    echo "   or create a desktop shortcut with:"
    echo "   cp $DESKTOP_FILE ~/Desktop/"
    echo ""
    echo "🔧 To uninstall, run: rm $DESKTOP_FILE"
else
    echo "❌ Failed to create desktop shortcut"
    exit 1
fi

read -p "Do you want to create a shortcut on Desktop as well? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    DESKTOP_SHORTCUT="$HOME/Desktop/calculator.desktop"
    cp "$DESKTOP_FILE" "$DESKTOP_SHORTCUT"
    chmod +x "$DESKTOP_SHORTCUT"
    echo "✅ Desktop shortcut created at: $DESKTOP_SHORTCUT"

    if command -v gio &> /dev/null; then
        gio set "$DESKTOP_SHORTCUT" metadata::trusted true
        echo "✅ Desktop shortcut trusted"
    fi
fi

echo ""
echo "✨ Installation complete!"