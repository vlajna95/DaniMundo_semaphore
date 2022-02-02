from django import template
from django.template.defaultfilters import stringfilter
from markdown import Markdown

register = template.Library()

md_extension_configs = {"markdown.extensions.def_list": {}, "markdown.extensions.footnotes": {}, "markdown.extensions.md_in_html": {}, "markdown.extensions.meta": {}, "markdown.extensions.nl2br": {}, "markdown.extensions.tables": {}, "markdown.extensions.toc": {"title": "", "toc_depth": "2-6"}, "pymdownx.emoji": {"title": "long"}, "pymdownx.caret": {}, "pymdownx.tilde": {}, "pymdownx.mark": {}, "pymdownx.tasklist": {}, "pymdownx.superfences": {"preserve_tabs": True}, "pymdownx.highlight": {"use_pygments": True, "pygments_style": "dracula", "noclasses": True, "linenums": True}, "customblocks": {"generators": {"question": "customblocks.custom_generators.question"}}}
# "cell_row_span": {}, "customblocks": {"generators": {"youtube_playlist": "md_cb:youtube_playlist"}, "config": {"youtube_inlineFluidStyle": True}}, "magic": {}, "tweetable": {"networks": ("twitter", "facebook")}, "markdown_del_ins": {}, "iconfonts": {"prefix_base_pairs": {"fa-": "fa", "glyph-": "glyphicon"}}}
md_extensions = [e for e in md_extension_configs.keys()]
md = Markdown(extensions=md_extensions, extension_configs=md_extension_configs, output_format="html5")


@register.filter()
@stringfilter
def markdown(value):
	return md.convert(value)


@register.filter()
def full_slug(article):
	return f"{article.slug}_{article.date_created.year}-{article.date_created.month}-{article.date_created.day}"
