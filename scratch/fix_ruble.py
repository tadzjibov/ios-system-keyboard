import os

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the common iPad sequences
    # 1. @ # № $ -> @ # № ₽
    content = content.replace('@ # № $', '@ # № ₽')
    
    # 2. ( ) $ & -> ( ) ₽ & (handling multiple spaces)
    import re
    # Match ( ) followed by one or more spaces, then $, then one or more spaces, then &
    content = re.sub(r'\( \)\s+\$\s+&', '( ) ₽ &', content)
    
    # 3. Clean up the mess I made (multiple ( ) ₽)
    content = re.sub(r'(\( \) ₽\s+)+', '( ) ₽ ', content)
    content = re.sub(r'\( \) ₽ \( \) \$ &', '( ) ₽ &', content)
    
    # 4. Final check for $ in iPad context
    # If there's still a $ between № and ´
    content = content.replace('№ $ ´', '№ ₽ ´')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# List of files from my previous grep
files = [
    'layout/gag/gag-3-rows-alt.yaml',
    'layout/gag/gag-3-rows.yaml',
    'layout/tle/tle-3-rows.yaml',
    'layout/ava/ava-3-rows.yaml',
    'layout/ava/ava-4-rows.yaml',
    'layout/dar/dar-3-rows.yaml',
    'layout/bak/bak-3-rows-rus.yaml',
    'layout/bak/bak-3-rows.yaml',
    'layout/tyv/tyv-3-rows.yaml',
    'layout/kom/kom-3-rows.yaml',
    'layout/bua/bua-3-rows.yaml',
    'layout/bua/bua-3-rows-nm.yaml',
    'layout/kjh/kjh-3-rows.yaml',
    'layout/kjh/kjh-4-rows.yaml',
    'layout/kjh/kjh-3-rows-rus.yaml',
    'layout/xdq/xdq-3-rows.yaml',
    'layout/chv/chv-google.yaml',
    'layout/chv/chv-yandex-4-rows.yaml',
    'layout/chv/chv-yandex.yaml',
    'layout/chv/chv-standard.yaml',
    'layout/chv/chv-ergonomic.yaml',
    'layout/chv/chv-3-rows.yaml',
    'layout/oss/oss-3-rows.yaml',
    'layout/sah/sah-3-rows.yaml',
    'layout/ulc/ulc-3-rows.yaml',
    'layout/xal/xal-3-rows.yaml',
    'layout/alt/alt-3-rows.yaml',
    'layout/gld/gld-3-rows.yaml',
    'layout/gld/gld-4-rows.yaml',
    'layout/tat/tat-3-rows-rus.yaml',
    'layout/tat/tat-3-rows.yaml',
    'layout/rus/rus-3-rows.yaml'
]

for f in files:
    full_path = os.path.join('/Users/ali/Documents/Science/ios-system', f)
    if os.path.exists(full_path):
        fix_file(full_path)
        print(f"Fixed {f}")
