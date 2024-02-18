# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1708224989.563711
_enable_loop = True
_template_filename = 'themes/kiss/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_header', 'html_site_title', 'html_navigation_links', 'html_navigation_links_entries', 'html_translation_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def html_navigation_links():
            return render_html_navigation_links(context)
        def html_translation_header():
            return render_html_translation_header(context)
        def html_site_title():
            return render_html_site_title(context)
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <nav id="nav-main" class="nav">\n      <div id="nav-name" class="nav-left">\n        ')
        __M_writer(str(html_site_title()))
        __M_writer('\n      </div>\n      <div class="nav-right">\n        <nav id="nav-items" class="nav-item level is-mobile">\n            ')
        __M_writer(str(html_translation_header()))
        __M_writer('\n            ')
        __M_writer(str(html_navigation_links()))
        __M_writer('\n')
        if search_form:
            __M_writer('                <div class="searchform" role="search">\n                    ')
            __M_writer(str(search_form))
            __M_writer('\n              </div>\n')
        __M_writer('            ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n        </nav>\n      </div>\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<a id="nav-anchor" class="nav-item" href="')
        __M_writer(str(_link("root", None, lang)))
        __M_writer('" title="')
        __M_writer(filters.html_escape(str(blog_title)))
        __M_writer('" rel="home">\n    <h1 id="nav-heading" class="title is-4">\n        <span id="blog-title">')
        __M_writer(filters.html_escape(str(blog_title)))
        __M_writer('</span>\n    </h1>\n</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        navigation_alt_links = _import_ns.get('navigation_alt_links', context.get('navigation_alt_links', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        def html_navigation_links_entries(navigation_links_source):
            return render_html_navigation_links_entries(context,navigation_links_source)
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(html_navigation_links_entries(navigation_links)))
        __M_writer('\n    ')
        __M_writer(str(html_navigation_links_entries(navigation_alt_links)))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links_entries(context,navigation_links_source):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text in navigation_links_source[lang]:
            if rel_link(permalink, url) == "#":
                __M_writer('            <a class="level-item" href="')
                __M_writer(str(permalink))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('<span class="sr-only"> ')
                __M_writer(str(messages("(active)", lang)))
                __M_writer('</span></a>\n')
            else:
                __M_writer('            <a class="level-item" href="')
                __M_writer(str(url))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        base = _mako_get_namespace(context, 'base')
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('            ')
            __M_writer(str(base.html_translations()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/kiss/templates/base_header.tmpl", "uri": "base_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 22, "35": 30, "36": 38, "37": 48, "38": 54, "44": 4, "58": 4, "59": 7, "60": 7, "61": 11, "62": 11, "63": 12, "64": 12, "65": 13, "66": 14, "67": 15, "68": 15, "69": 18, "70": 18, "71": 18, "77": 24, "86": 24, "87": 25, "88": 25, "89": 25, "90": 25, "91": 27, "92": 27, "98": 32, "109": 32, "110": 33, "111": 33, "112": 34, "113": 34, "114": 35, "115": 35, "116": 36, "117": 36, "123": 40, "133": 40, "134": 41, "135": 42, "136": 43, "137": 43, "138": 43, "139": 43, "140": 43, "141": 43, "142": 43, "143": 44, "144": 45, "145": 45, "146": 45, "147": 45, "148": 45, "154": 50, "163": 50, "164": 51, "165": 52, "166": 52, "167": 52, "173": 167}}
__M_END_METADATA
"""
