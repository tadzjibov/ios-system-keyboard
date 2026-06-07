# Buryat language (Буряад хэлэн) — `bua`

Keyboard layout for the **Buryat language** (ISO 639-3: `bua`), Mongolic language family.

**Language codes**:

* **ISO 639-3**: `bua`
* **ISO 15924**: `Cyrl`

```yaml
displayNames:
  en: Buryat
  ru: Бурятский
  bua: Буряад
```

## Раскладки / Layouts

Две раскладки, каждая для iOS и macOS.

### 1. На основе русской / Russian-based (`bua-rus`)

Полная русская раскладка ЙЦУКЕН без изменений — все русские буквы на своих местах.
Бурятские `Ө Ү Һ` вызываются на похожих русских клавишах:

* **iOS** — long-press: `у → ү`, `о → ө`, `х → һ`
* **macOS** — Option (⌥): `⌥у → ү`, `⌥о → ө`, `⌥х → һ` (заглавные через `⌥⇧`)

Файлы: `bua-rus-3-rows.yaml` (iOS), `bua-rus-macos.yaml` (macOS), `bua-rus-longpress.yaml`.

### 2. На основе монгольской / Mongolian-based (`bua-mon`)

Расположение букв повторяет национальную монгольскую раскладку
(Windows KBDMON / стандарт MNS): `ө` на клавише `F`, `ү` на `O`, `е`/`щ` на `-`/`=`.
Для бурятского добавлена `Һ`.

* **macOS** — `Һ` на клавише `\`; цифровой ряд по монгольскому образцу: без `Shift` — пунктуация и `₽` (рубль вместо монгольского тугрика), цифры через `Shift`.
* **iOS** — `Һ` в нижнем ряду между `Т` и `Ь`; `щ`/`ъ` на long-press (`ш → щ`, `ь → ъ`).

Файлы: `bua-mon-3-rows.yaml` (iOS), `bua-mon-macos.yaml` (macOS), `bua-mon-longpress.yaml`.

Источник монгольской раскладки: <https://learn.microsoft.com/globalization/keyboards/kbdmon>

## Details

### Алфавит / Alphabet

36 letters: 33 Russian + 3 Buryat-specific (Ө, Ү, Һ).

```
'а' CYRILLIC SMALL LETTER A
'б' CYRILLIC SMALL LETTER BE
'в' CYRILLIC SMALL LETTER VE
'г' CYRILLIC SMALL LETTER GHE
'д' CYRILLIC SMALL LETTER DE
'е' CYRILLIC SMALL LETTER IE
'ё' CYRILLIC SMALL LETTER IO
'ж' CYRILLIC SMALL LETTER ZHE
'з' CYRILLIC SMALL LETTER ZE
'и' CYRILLIC SMALL LETTER I
'й' CYRILLIC SMALL LETTER SHORT I
'к' CYRILLIC SMALL LETTER KA
'л' CYRILLIC SMALL LETTER EL
'м' CYRILLIC SMALL LETTER EM
'н' CYRILLIC SMALL LETTER EN
'о' CYRILLIC SMALL LETTER O
'ө' CYRILLIC SMALL LETTER BARRED O
'п' CYRILLIC SMALL LETTER PE
'р' CYRILLIC SMALL LETTER ER
'с' CYRILLIC SMALL LETTER ES
'т' CYRILLIC SMALL LETTER TE
'у' CYRILLIC SMALL LETTER U
'ү' CYRILLIC SMALL LETTER STRAIGHT U
'ф' CYRILLIC SMALL LETTER EF
'х' CYRILLIC SMALL LETTER HA
'һ' CYRILLIC SMALL LETTER SHHA
'ц' CYRILLIC SMALL LETTER TSE
'ч' CYRILLIC SMALL LETTER CHE
'ш' CYRILLIC SMALL LETTER SHA
'щ' CYRILLIC SMALL LETTER SHCHA
'ъ' CYRILLIC SMALL LETTER HARD SIGN
'ы' CYRILLIC SMALL LETTER YERU
'ь' CYRILLIC SMALL LETTER SOFT SIGN
'э' CYRILLIC SMALL LETTER E
'ю' CYRILLIC SMALL LETTER YU
'я' CYRILLIC SMALL LETTER YA
```

### Названия клавиш / Key names

```yaml
keyNames:
  space: Зай
  return: Оруулга
  return-alts:
    search: Бэдэрхэ
    go: Шэлжэхэ
    send: Эльгээхэ
    join: Оруулха
    route: Зам
    next: Удаадахи
    continue: Утадхаха
    done: Бэлэн
  cancel: Болюулха
  undo: Арсаха
  redo: Дабтаха
```

## Разработчик / Developer

* Али Кужугет / Ali Kuzhuget
* Булат Дамдинов / Bulat Damdinov

## Ссылки / References

- [Buryat language — Wikipedia](https://en.wikipedia.org/wiki/Buryat_language)
- [Бурятский язык — Википедия](https://ru.wikipedia.org/wiki/Бурятский_язык)
