# Lezgi keyboard
 
System keyboard layout for the **Lezgi language** (Лезги чӏал · Lezgi · ISO&nbsp;639: `lez` · Cyrillic script) for **iOS, iPadOS and macOS**.
 
The layout is built on top of the standard **Russian** system keyboard. The goal is zero relearning for people already used to the Russian layout: no familiar key is moved from its place.
 
## 📘 Highlights
 
- **Palochka `Ӏ` / `ӏ`** (U+04C0 / U+04CF) takes the position of `щ`. Case is preserved: lowercase `ӏ` on the base layer, uppercase `Ӏ` on Shift.
- **`щ`** (used only in loanwords) is available via **long-press on `ш`** on touch keyboards.
- **`ъ`** is promoted to a dedicated key — it is frequent in Lezgi (гъ, къ, хъ, etc.). On iPhone it is added to the top row; on iPad and macOS it is a normal key, as in Russian.
- System keys (Return, Space, Search, etc.) are **localized into Lezgi** (`keyNames`).
- Fully position-compatible with the Russian layout across all form factors.
## 🧩 Files
 
```
layout/lez/
 ├── lez-3-rows.yaml      # primary iOS/iPadOS layout (iPhone + iPad-9in + iPad-12in)
 ├── lez-longpress.yaml   # long-press alternates
 └── lez-macos.yaml       # macOS layout (hardware keyboard)
```
 
## ⌨️ Long-press alternates
 
Defined in `lez-longpress.yaml`:
 
- **Letters:** `ш → щ`
- **Symbols & punctuation:** currencies on `₽`, `№` on `#`, ellipsis on `.`, quote and dash variants, and more.

## 🌍 Compatibility
 
The layouts follow the repository's unified scheme and are compatible with platform layout-generation tools (Apple Keyboard, Unicode CLDR, etc.).
 
## 📝 Notes
 
On **macOS** the letter `щ` is not present in the layout — hardware keyboards have no long-press. Switch to the Russian layout if you type Russian loanwords often.

## 🌍 Contact
 
Authors: E. Eskendarov, R. Gamidov, A. Magomedov, K. Tadzjibov. 

Prepared for the *Apple Keyboards for All* project.
