import os

import mkdocs.config
import mkdocs.plugins
import mkdocs.structure
import mkdocs.structure.files
import mkdocs.structure.nav
import mkdocs.structure.pages
import regex


def exclude_file(name):
    return name.startswith("assets/fragments/")


HREF_REGEX = (
    r"(?<=<\s*(?:a[^>]*href|img[^>]*src)=)"
    r'(?:"([^"]*)"|\'([^\']*)|[ ]*([^ =>]*)(?![a-z]+=))'
)


@mkdocs.plugins.event_priority(-1000)
def on_post_page(
    output: str,
    page: mkdocs.structure.pages.Page,
    config: mkdocs.config.Config,
):
    """
    1. Replace absolute paths with path relative to the rendered page
       This must be performed after all other plugins have run.
    2. Replace component names with links to the component reference

    Parameters
    ----------
    output
    page
    config

    Returns
    -------

    """

    def replace_link(match):
        relative_url = url = match.group(1) or match.group(2) or match.group(3)
        page_url = os.path.join("/", page.file.url)
        if url and url.startswith("/"):
            relative_url = os.path.relpath(url, page_url)
        return f'"{relative_url}"'

    # Replace absolute paths with path relative to the rendered page
    # output = regex.sub(PIPE_REGEX, replace_component, output)
    output = regex.sub(HREF_REGEX, replace_link, output)

    return output
