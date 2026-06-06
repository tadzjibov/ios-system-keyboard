# Kaitag (xdq) — iOS/macOS Keyboard

**Language**: Kaitag (_Хайдаҡӏла_)  
**ISO 639-3**: `xdq`  
**Script**: Cyrillic, [v1.2 (May 2026)](https://github.com/urssivar/script)

The modern Kaitag Cyrillic alphabet was developed in 2024–2026. It consists of 24 letters from the Russian alphabet (excluding **Ёё**, **Фф**, **Щщ**, **Ъъ**, **Ыы**, **Ьь**, **Ээ**, **Юю**, **Яя**), 6 extended Cyrillic letters (**Әә**, **Ғғ**, **Ҡҡ**, **Ҳҳ**, **Һһ**, **Ӏӏ**), and 12 digraphs (doubled geminates and ejectives with the palochka). Supplementary notation covers stress marking, marginal and dialectal sounds, and loanword letters.

Input methods are based on the standard Russian ЙЦУКЕН layout. **Language switcher**: `ҡғҳ` (from _ҡҡуғадеҳ_ — "happiness")

## iOS

### 3-Row (`xdq-3-rows`)

Replaces six of seven excluded Russian letters: `щ` → `ӏ`, `ф` → `ҳ`, `ы` → `ҡ`, `э` → `ғ`, `я` → `ә`, `ь` → `һ`, and drops `ю`. Placement reflects character frequency.

```text
й ц у к е н г ш ӏ з х
ҳ ҡ в а п р о л д ж ғ
   ә ч с м и т һ б
```

Accented vowels for stress marking and excluded Russian letters are accessible via long-press:

- `у` → `ю` `у́`
- `е` → `э` `е́` `ё`
- `ш` → `щ`
- `ӏ` → `ъ`
- `а` → `я` `а́`
- `п` → `ф`
- `о` → `о́`
- `ә` → `ә́`
- `и` → `ы` `и́`
- `һ` → `ь`

### 4-Row (`xdq-4-rows`)

Leaves the Russian ЙЦУКЕН intact and adds new keys above:

```text
, ! ? ҳ ҡ ә һ ӏ ғ — .
й ц у к е н г ш щ з х
ф ы в а п р о л д ж э
  я ч с м и т ь б ю
```

_The corner keys are `,` and `.` here; the canonical layout uses `'` and `"`, falling back to `,` and `.` on keyboards (like iOS) that lack them around the spacebar._

Accented vowels are accessible via long-press:

- `ә` → `ә́`
- `у` → `у́`
- `е` → `е́` `ё`
- `ы` → `ы́`
- `а` → `а́`
- `о` → `о́`
- `э` → `э́`
- `я` → `я́`
- `и` → `и́`
- `ь` → `ъ`
- `ю` → `ю́`

### iPad

The **9-inch iPad** adds `ю`, `ъ`, and `я` as direct keys in the third row.

The **12-inch iPad** uses a full physical-keyboard-style layout with a number row. The third row is expanded to recover displaced Russian letters: `ю`, `ы`, and `я`.

## macOS

Follows ЙЦУКЕН with Kaitag substitutions. Displaced Russian letters are accessible via `⌥`:

- `⌥` `ӏ` = `щ`
- `⌥` `ҳ` = `ф`
- `⌥` `ҡ` = `ы`
- `⌥` `ғ` = `э`
- `⌥` `ә` = `я`
- `⌥` `һ` = `ь`

`ю` remains a direct key in its native (`.`) slot.

Common typographic symbols are in the `⌥` layer: `№ ~ © ® ° · § « » – — ™ ∞ µ ≈ ≠ ≤ ≥ ‹ › ‚ „`.

A dead key `´` is available for stressed vowels: `⌥` `´` + `а` = `а́`.

## Contact

Magomed Magomedov, <alkaitagi@outlook.com>
