#!/usr/bin/env python3
"""
Generate keyboard layout documentation from kbdgen files.

This script reads keyboard layout definitions from .kbdgen/layouts/*.yaml files
and generates a markdown file with iframe embeds for all keyboard layouts.
"""

import glob
import os
import sys
import yaml
import re

EMBED_BASE_URL = 'https://keyboard.giellalt.org/embed'

PLATFORM_NAMES = {
    'macOS': 'Mac',
    'windows': 'Windows',
    'chromeOS': 'ChromeOS',
    'android': 'Android',
    'iOS': 'iOS/iPadOS'
}

MOBILE_DEVICE_TYPES = {
    'primary': 'Phone',
    'tablet-600': 'Tablet',
    'iPad-9in': '9" iPad',
    'iPad-12in': '12" iPad'
}


def find_kbdgen_dir():
    """Find the .kbdgen directory in the current working directory."""
    kbdgen_dirs = glob.glob('*.kbdgen')
    if not kbdgen_dirs:
        return None
    return kbdgen_dirs[0]


def read_yaml_file(path):
    """Read and parse a YAML file."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f'Error reading {path}: {e}', file=sys.stderr)
        return None


def get_language_code(kbdgen_dir):
    """Extract language code from kbdgen directory name."""
    return os.path.basename(kbdgen_dir).replace('.kbdgen', '')


def get_layout_display_name(layout_data, layout_name, lang_code):
    """Get the display name for a layout."""
    display_names = layout_data.get('displayNames', {})
    # Try specific layout name first (e.g., sma-NO), then language code (sma), then English
    return (display_names.get(layout_name) or
            display_names.get(lang_code) or
            display_names.get('en') or
            layout_name)


def generate_iframe(kbd, layout, platform, variant):
    """Generate an iframe embed code for a keyboard layout."""
    url = f'{EMBED_BASE_URL}?kbd={kbd}&layout={layout}&platform={platform}&variant={variant}'
    return f'<iframe src="{url}"></iframe>'


def extract_region_label(display_name):
    """Extract region label from display name, e.g., '(Nöörje)' -> 'Nöörje'."""
    match = re.search(r'\(([^)]+)\)', display_name)
    return match.group(1) if match else None


def generate_desktop_section(kbd, layout_name, layout_data, platform, region_label):
    """Generate markdown section for a desktop platform."""
    variants = layout_data.get(platform)
    if not variants:
        return None

    platform_name = PLATFORM_NAMES.get(platform, platform)
    heading = f'## {platform_name} ({region_label})' if region_label else f'## {platform_name}'

    # For desktop, we typically only care about the 'primary' variant
    iframe = generate_iframe(kbd, layout_name, platform, 'primary')

    return f'{heading}\n\n{iframe}\n'


def generate_mobile_section(kbd, layout_name, layout_data, platform):
    """Generate markdown section for a mobile platform."""
    variants = layout_data.get(platform)
    if not variants:
        return None

    platform_name = PLATFORM_NAMES.get(platform, platform)
    output = [f'## {platform_name}']

    # Get all variants for this platform
    for variant_name, variant_data in variants.items():
        if variant_name == 'config':  # Skip config sections
            continue

        device_label = MOBILE_DEVICE_TYPES.get(variant_name, variant_name)
        # Use "iPhone" instead of "Phone" for iOS primary variant
        if platform == 'iOS' and variant_name == 'primary':
            device_label = 'iPhone'

        iframe = generate_iframe(kbd, layout_name, platform, variant_name)

        output.append(f'\n### {device_label}\n\n{iframe}')

    return '\n'.join(output) + '\n'


def generate_layout_documentation():
    """Generate the complete layout documentation."""
    kbdgen_dir = find_kbdgen_dir()
    if not kbdgen_dir:
        print('Error: No .kbdgen directory found', file=sys.stderr)
        sys.exit(1)

    lang_code = get_language_code(kbdgen_dir)
    layouts_dir = os.path.join(kbdgen_dir, 'layouts')

    if not os.path.exists(layouts_dir):
        print(
            f'Error: Layouts directory not found: {layouts_dir}', file=sys.stderr)
        sys.exit(1)

    # Read base layout to get language names
    base_layout_file = os.path.join(layouts_dir, f'{lang_code}.yaml')
    base_layout_data = read_yaml_file(base_layout_file)

    english_name = lang_code.upper()
    native_name = lang_code

    if base_layout_data:
        display_names = base_layout_data.get('displayNames', {})
        english_name = display_names.get('en', lang_code.upper())
        native_name = display_names.get(lang_code, lang_code)

    # Generate title - show both names only if they differ
    if english_name == native_name:
        title = f"# Keyboard layouts for {english_name}"
    else:
        title = f"# Keyboard layouts for {english_name} / {native_name}"

    # Start building the markdown
    output = []
    output.append('---')
    output.append('layout: default')
    output.append('---')
    output.append('')
    output.append(title)
    output.append('')
    output.append(
        '> Tip: These keyboards are interactive — click or tap keys to explore different layers (Shift, Alt, etc.)')
    output.append('')

    # Collect and process layouts
    layout_files = sorted(glob.glob(os.path.join(layouts_dir, '*.yaml')))

    for layout_file in layout_files:
        layout_name = os.path.basename(layout_file).replace('.yaml', '')
        layout_data = read_yaml_file(layout_file)

        if not layout_data:
            continue

        display_name = get_layout_display_name(
            layout_data, layout_name, lang_code)
        region_label = extract_region_label(display_name)

        # Generate desktop platforms first
        for platform in ['macOS', 'windows', 'chromeOS']:
            section = generate_desktop_section(
                lang_code, layout_name, layout_data, platform, region_label)
            if section:
                output.append(section)

        # Then generate mobile platforms
        for platform in ['android', 'iOS']:
            section = generate_mobile_section(
                lang_code, layout_name, layout_data, platform)
            if section:
                output.append(section)

    return '\n'.join(output)


def main():
    """Main entry point."""
    try:
        markdown = generate_layout_documentation()
        output_file = 'docs/layout.md'

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f'✓ Generated {output_file}')
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
