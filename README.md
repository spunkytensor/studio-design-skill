# Studio design skill

The official repository for `designing-translucent-interfaces`: a standalone, product-neutral skill for building calm interfaces with translucent layered surfaces, soft highlights, and accessible light/dark themes.

**[Read the complete design guide](skills/designing-translucent-interfaces/SKILL.md).**

The guide defines a canonical palette, glass materials, typography, component dimensions, responsive layouts, interaction states, accessibility requirements, and a rendered-state verification workflow. It requires no plugins, scripts, proprietary assets, or particular application framework.

## Install

Run this from the project where you want to use the skill:

```sh
npx skills add https://github.com/spunkytensor/studio-design-skill --skill designing-translucent-interfaces
```

The equivalent shorthand is:

```sh
npx skills add spunkytensor/studio-design-skill --skill designing-translucent-interfaces
```

The installer prompts for compatible agents and installation method. Project-local installation is the default; add `--global` for a user-wide installation. Review the skill before installing it.

To discover the available skill without installing:

```sh
npx skills add spunkytensor/studio-design-skill --list
```

These remote commands require the repository contents to have been published. A local, uncommitted checkout can be tested with `npx skills add /absolute/path/to/studio-design-skill --list` instead.

### Manual installation

Copy the entire `skills/designing-translucent-interfaces/` directory into your client's skill discovery directory, commonly `.agents/skills/` in the target project. Keep `SKILL.md` and `UNLICENSE` together. Clients may use different discovery directories.

## Use

After installation, ask your agent:

> Use designing-translucent-interfaces to implement a collection browser. Follow its canonical materials, typography and component rules, with light/dark themes, one orange primary, and accessible phone layouts. Verify the rendered and interactive states.

The skill guides presentation and verification without inventing product behavior or imposing another product's identity.

## Repository layout

```text
README.md
UNLICENSE
skills/
└── designing-translucent-interfaces/
    ├── SKILL.md
    └── UNLICENSE
```

`skills/designing-translucent-interfaces/SKILL.md` is the canonical skill source. Its directory name matches the frontmatter `name`. The root license covers the repository; the identical bundled copy keeps the terms with installed skills.

This layout follows the [skill specification](https://agentskills.io/specification) and the repository discovery convention used by the [skills.sh installer](https://skills.sh/docs). No package registry release, custom installer, or plugin manifest is required. Directory visibility and ranking are managed by the external service; repository preparation alone does not guarantee a listing.

## License

This skill and its documentation are released into the public domain under the [Unlicense](UNLICENSE). Anyone may use, copy, modify, publish, sell, or distribute them for any purpose, commercial or non-commercial.

Provided **"AS IS" by Spunky Tensor, without warranty of any kind**, with the full warranty disclaimer and limitation of liability in the license text.
