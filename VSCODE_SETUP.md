# Using dstoolkit-jupyter-theme in VS Code

VS Code renders Jupyter notebooks with its own editor, so `~/.jupyter/custom/custom.css` does not apply. This guide ports the dstoolkit theme to VS Code across three layers:

1. **Syntax highlighting** — CodeMirror token colors mapped to VS Code TextMate scopes
2. **Notebook UI** — cell borders, backgrounds, and markdown fonts
3. **DataFrame/output styling** — auto-injected via IPython startup

## Prerequisites

- VS Code with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- A light base theme (e.g., GitHub Light Default)

## Step 1: Install the CMU Serif fonts

The theme uses Computer Modern (CMU Serif) for markdown cells. Copy the font files from this repo into your system fonts directory.

**macOS:**

```bash
cp fonts/cmu-text/*.otf ~/Library/Fonts/
```

**Linux:**

```bash
mkdir -p ~/.local/share/fonts
cp fonts/cmu-text/*.otf ~/.local/share/fonts/
fc-cache -fv
```

**Windows:**

Right-click each `.otf` file in `fonts/cmu-text/` and select "Install".

## Step 2: Configure VS Code settings

Open your VS Code settings JSON (`Cmd+Shift+P` > "Preferences: Open User Settings (JSON)") and add the following. If you use [VS Code Profiles](https://code.visualstudio.com/docs/editor/profiles), add this to your notebook/research profile's settings instead.

### 2a. Editor and notebook fonts

```jsonc
{
    // Code cells: SF Mono matches the original theme, JetBrains Mono as fallback
    "editor.fontFamily": "'SF Mono', 'JetBrains Mono', 'Fira Code', Menlo, monospace",
    "editor.fontSize": 13,
    "editor.lineHeight": 1.6,

    // Notebook markdown cells: CMU Serif for the academic look
    "notebook.markup.fontFamily": "'CMU Serif', 'Times New Roman', serif",

    // Notebook output: monospace for DataFrames and printed output
    "notebook.output.fontFamily": "'SF Mono', 'JetBrains Mono', Menlo, monospace",
    "notebook.output.fontSize": 12,
}
```

### 2b. Workbench color customizations (notebook UI)

These map the theme's background, selection, and cell border colors:

```jsonc
{
    "workbench.colorCustomizations": {
        // Editor chrome
        "editor.background": "#F8F8F8",
        "editor.foreground": "#828282",
        "editor.selectionBackground": "#e8e8e8",
        "editor.lineHighlightBackground": "#F8F8F8",
        "editorLineNumber.foreground": "#b8b8b8",
        "editorCursor.foreground": "#585858",
        "editorBracketMatch.border": "#828282",

        // Notebook cells
        "notebook.cellBorderColor": "#e8e8e8",
        "notebook.focusedCellBorder": "#009489",       // CYAN when selected
        "notebook.cellToolbarSeparator": "#e8e8e8",
        "notebook.selectedCellBackground": "#F8F8F8",
        "notebook.focusedEditorBorder": "#BA5400"       // ORANGE in edit mode
    },
}
```

### 2c. Syntax highlighting (token color customizations)

This maps the original CodeMirror token colors to VS Code TextMate scopes:

```jsonc
{
    "editor.tokenColorCustomizations": {
        "comments": "#828282",
        "textMateRules": [
            {
                "scope": "comment",
                "settings": { "foreground": "#828282" }
            },
            {
                "scope": "constant.language",
                "settings": { "foreground": "#D14187" }
            },
            {
                "scope": "constant.numeric",
                "settings": { "foreground": "#007ad0" }
            },
            {
                "scope": ["variable.other.property", "meta.attribute"],
                "settings": { "foreground": "#D14187" }
            },
            {
                "scope": "entity.other.attribute-name",
                "settings": { "foreground": "#688A0A" }
            },
            {
                "scope": ["keyword", "keyword.control", "storage.type", "storage.modifier"],
                "settings": { "foreground": "#D43132", "fontStyle": "" }
            },
            {
                "scope": ["string", "string.quoted"],
                "settings": { "foreground": "#ba9600" }
            },
            {
                "scope": "keyword.operator",
                "settings": { "foreground": "#BA5400" }
            },
            {
                "scope": ["support.function.builtin", "support.function.magic"],
                "settings": { "foreground": "#793ac7" }
            },
            {
                "scope": ["variable", "variable.other"],
                "settings": { "foreground": "#009489" }
            },
            {
                "scope": ["variable.parameter", "variable.other.readwrite"],
                "settings": { "foreground": "#007ad0" }
            },
            {
                "scope": ["entity.name.function", "meta.function-call.generic"],
                "settings": { "foreground": "#009489" }
            },
            {
                "scope": "invalid",
                "settings": { "foreground": "#D43132" }
            },
            {
                "scope": ["entity.name.tag", "punctuation.definition.tag"],
                "settings": { "foreground": "#D43132" }
            },
            {
                "scope": "markup.underline.link",
                "settings": { "foreground": "#793ac7" }
            },
            {
                "scope": "punctuation.bracket",
                "settings": { "foreground": "#828282" }
            },
            {
                "scope": ["support.type", "support.class", "entity.name.type"],
                "settings": { "foreground": "#793ac7" }
            },
            {
                "scope": ["punctuation.definition.string", "string.quoted punctuation"],
                "settings": { "foreground": "#ba9600" }
            },
            {
                "scope": "constant.other",
                "settings": { "foreground": "#D14187" }
            },
            {
                "scope": ["meta.function.decorator", "entity.name.function.decorator"],
                "settings": { "foreground": "#BA5400" }
            }
        ]
    },
}
```

### Token color mapping reference

| CodeMirror Token | VS Code TextMate Scope | Color | Name |
|---|---|---|---|
| `cm-comment` | `comment` | `#828282` | Gray |
| `cm-atom` | `constant.language` | `#D14187` | Magenta |
| `cm-number` | `constant.numeric` | `#007ad0` | Blue |
| `cm-property` | `variable.other.property` | `#D14187` | Magenta |
| `cm-attribute` | `entity.other.attribute-name` | `#688A0A` | Green |
| `cm-keyword` | `keyword` | `#D43132` | Red |
| `cm-string` | `string` | `#ba9600` | Yellow |
| `cm-operator` | `keyword.operator` | `#BA5400` | Orange |
| `cm-builtin` | `support.function.builtin` | `#793ac7` | Violet |
| `cm-variable` | `variable` | `#009489` | Cyan |
| `cm-variable-2` | `variable.parameter` | `#007ad0` | Blue |
| `cm-def` | `entity.name.function` | `#009489` | Cyan |
| `cm-error` | `invalid` | `#D43132` | Red |
| `cm-bracket` | `punctuation.bracket` | `#828282` | Gray |
| `cm-tag` | `entity.name.tag` | `#D43132` | Red |
| `cm-link` | `markup.underline.link` | `#793ac7` | Violet |

## Step 3: DataFrame and output styling (IPython startup)

VS Code notebook outputs are rendered in a webview where VS Code settings cannot style HTML tables. To apply the dstoolkit DataFrame styling, create an IPython startup script that auto-injects CSS into every notebook session.

Create the file `~/.ipython/profile_default/startup/01-dstoolkit-theme.py`:

```python
"""
Auto-inject dstoolkit Jupyter theme CSS into notebook outputs.
Based on: https://github.com/snafis/dstoolkit-jupyter-theme
"""

try:
    from IPython.display import HTML, display

    _dstoolkit_css = HTML("""
    <style>
    /* dstoolkit-jupyter-theme: DataFrame styling */
    table.dataframe {
        border-collapse: collapse;
        border: none;
        font-family: 'SF Mono', 'JetBrains Mono', 'Menlo', 'Courier New', monospace;
        font-size: 0.75rem;
    }

    table.dataframe thead tr {
        color: #A05200;
        font-style: normal;
        padding: 5px 10px;
        border-bottom: 1px solid #828282;
        vertical-align: middle;
        text-align: center;
    }

    table.dataframe thead tr th,
    table.dataframe thead tr:only-child th {
        vertical-align: middle;
        text-align: center;
    }

    table.dataframe tbody tr th {
        background-color: #ffffff;
        text-align: left;
        font-style: italic;
    }

    table.dataframe tbody tr td {
        background-color: #fff9ea;
        color: #828282;
        padding-left: 1.0rem;
        padding-right: 1.0rem;
    }

    /* dstoolkit-jupyter-theme: Output styling */
    div.output_html {
        font-size: 0.75rem;
        font-weight: normal;
        font-family: 'SF Mono', 'JetBrains Mono', 'Menlo', 'Courier New', monospace;
    }

    div.output_area pre {
        font-weight: normal;
        color: #828282;
    }

    /* dstoolkit-jupyter-theme: ANSI terminal colors */
    .ansi-red-fg   { color: #D43132; font-weight: bold; }
    .ansi-green-fg { color: #688A0A; }
    .ansi-cyan-fg  { color: #009489; }
    .ansi-blue-fg  { color: #007ad0; }
    </style>
    """)

    display(_dstoolkit_css)
    del _dstoolkit_css
except ImportError:
    pass
```

Or as a one-liner to create the file:

```bash
mkdir -p ~/.ipython/profile_default/startup
curl -o ~/.ipython/profile_default/startup/01-dstoolkit-theme.py \
  https://raw.githubusercontent.com/snafis/dstoolkit-jupyter-theme/master/01-dstoolkit-theme.py
```

## Step 4: (Optional) VS Code Profile for notebooks

If you use VS Code Profiles, you can create a dedicated profile that bundles all of these settings with only the extensions you need for notebook work:

```bash
# Create the profile (opens a VS Code window)
code --profile "AI Research" --new-window .

# Install notebook-related extensions into the profile
code --profile "AI Research" \
  --install-extension ms-python.python \
  --install-extension ms-python.vscode-pylance \
  --install-extension charliermarsh.ruff \
  --install-extension ms-toolsai.jupyter \
  --install-extension ms-toolsai.jupyter-renderers \
  --install-extension ms-toolsai.jupyter-keymap \
  --install-extension ms-toolsai.tensorboard \
  --install-extension ms-toolsai.datawrangler \
  --install-extension github.github-vscode-theme \
  --install-extension pkief.material-icon-theme
```

Then add all settings from Steps 2a-2c into that profile's settings JSON.

## Complete settings.json

For reference, here is a complete `settings.json` combining all sections above:

```jsonc
{
    // --- Python formatting ---
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnType": false,
        "editor.formatOnSave": true
    },

    // --- Fonts ---
    "editor.fontFamily": "'SF Mono', 'JetBrains Mono', 'Fira Code', Menlo, monospace",
    "editor.fontSize": 13,
    "editor.lineHeight": 1.6,
    "editor.fontLigatures": true,
    "notebook.markup.fontFamily": "'CMU Serif', 'Times New Roman', serif",
    "notebook.output.fontFamily": "'SF Mono', 'JetBrains Mono', Menlo, monospace",
    "notebook.output.fontSize": 12,

    // --- Workbench colors ---
    "workbench.colorTheme": "GitHub Light Default",
    "workbench.colorCustomizations": {
        "editor.background": "#F8F8F8",
        "editor.foreground": "#828282",
        "editor.selectionBackground": "#e8e8e8",
        "editor.lineHighlightBackground": "#F8F8F8",
        "editorLineNumber.foreground": "#b8b8b8",
        "editorCursor.foreground": "#585858",
        "editorBracketMatch.border": "#828282",
        "notebook.cellBorderColor": "#e8e8e8",
        "notebook.focusedCellBorder": "#009489",
        "notebook.cellToolbarSeparator": "#e8e8e8",
        "notebook.selectedCellBackground": "#F8F8F8",
        "notebook.focusedEditorBorder": "#BA5400"
    },

    // --- Syntax highlighting ---
    "editor.tokenColorCustomizations": {
        "comments": "#828282",
        "textMateRules": [
            { "scope": "comment", "settings": { "foreground": "#828282" } },
            { "scope": "constant.language", "settings": { "foreground": "#D14187" } },
            { "scope": "constant.numeric", "settings": { "foreground": "#007ad0" } },
            { "scope": ["variable.other.property", "meta.attribute"], "settings": { "foreground": "#D14187" } },
            { "scope": "entity.other.attribute-name", "settings": { "foreground": "#688A0A" } },
            { "scope": ["keyword", "keyword.control", "storage.type", "storage.modifier"], "settings": { "foreground": "#D43132", "fontStyle": "" } },
            { "scope": ["string", "string.quoted"], "settings": { "foreground": "#ba9600" } },
            { "scope": "keyword.operator", "settings": { "foreground": "#BA5400" } },
            { "scope": ["support.function.builtin", "support.function.magic"], "settings": { "foreground": "#793ac7" } },
            { "scope": ["variable", "variable.other"], "settings": { "foreground": "#009489" } },
            { "scope": ["variable.parameter", "variable.other.readwrite"], "settings": { "foreground": "#007ad0" } },
            { "scope": ["entity.name.function", "meta.function-call.generic"], "settings": { "foreground": "#009489" } },
            { "scope": "invalid", "settings": { "foreground": "#D43132" } },
            { "scope": ["entity.name.tag", "punctuation.definition.tag"], "settings": { "foreground": "#D43132" } },
            { "scope": "markup.underline.link", "settings": { "foreground": "#793ac7" } },
            { "scope": "punctuation.bracket", "settings": { "foreground": "#828282" } },
            { "scope": ["support.type", "support.class", "entity.name.type"], "settings": { "foreground": "#793ac7" } },
            { "scope": ["punctuation.definition.string", "string.quoted punctuation"], "settings": { "foreground": "#ba9600" } },
            { "scope": "constant.other", "settings": { "foreground": "#D14187" } },
            { "scope": ["meta.function.decorator", "entity.name.function.decorator"], "settings": { "foreground": "#BA5400" } }
        ]
    },

    // --- Notebook settings ---
    "notebook.output.scrolling": true,
    "jupyter.themeMatplotlibPlots": true
}
```

## How it works

| Layer | What it styles | Mechanism |
|---|---|---|
| `workbench.colorCustomizations` | Editor background, cell borders, cursor, selection | VS Code theme overrides |
| `editor.tokenColorCustomizations` | Code syntax (keywords, strings, functions, etc.) | TextMate scope rules |
| `notebook.markup.fontFamily` | Markdown cell headings and body text | VS Code setting |
| `notebook.output.fontFamily` | Printed output and DataFrame text | VS Code setting |
| IPython startup script | DataFrame table colors, borders, backgrounds | CSS injected into notebook output webview |

## Notes

- The IPython startup script runs automatically in every new notebook kernel. The injected CSS is visible as a hidden HTML output in the first cell's output area.
- `jupyter.themeMatplotlibPlots: true` tells VS Code to match matplotlib plot backgrounds to the editor theme.
- The base theme (GitHub Light Default) provides a clean light foundation. The `colorCustomizations` and `tokenColorCustomizations` override it with the dstoolkit palette.
- If you use the classic Jupyter Notebook in a browser, the original `custom.css` installation method still applies (copy to `~/.jupyter/custom/custom.css`). Both methods can coexist.
