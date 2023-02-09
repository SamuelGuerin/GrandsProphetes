import os
import sys
sys.path.insert(0, os.path.abspath('../../Application/'))
sys.path.insert(1, os.path.abspath('../../Application/Models'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LulusWorld'
copyright = '2023, Les Grands Prophètes'
author = 'Laurent Brochu, Kevin Gauvin, Samuel Guérin, Justin Leblanc, Maxime Lefebvre, Raphaël Seyer'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'piccolo_theme'
html_theme_path = ["."]

