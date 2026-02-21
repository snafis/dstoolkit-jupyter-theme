"""
Auto-inject dstoolkit Jupyter theme CSS into notebook outputs.
Based on: https://github.com/snafis/dstoolkit-jupyter-theme

This runs on IPython startup and applies DataFrame/output styling
that matches the dstoolkit theme in both VS Code and browser notebooks.
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
