# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1708224989.689497
_enable_loop = True
_template_filename = 'themes/kiss/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        hidden_tags = _import_ns.get('hidden_tags', context.get('hidden_tags', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        def content_header():
            return render_content_header(context)
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        def content():
            return render_content(context)
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        hidden_tags = _import_ns.get('hidden_tags', context.get('hidden_tags', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        for post in posts:
            __M_writer('\n    <article>\n')
            if post.tags:
                __M_writer('        <div class="subtitle tags is-6 is-pulled-right">\n')
                for i, tag in enumerate(post.tags):
                    if tag not in hidden_tags:
                        if i > 0:
                            __M_writer('                |\n')
                        __M_writer('                <a class="subtitle is-6" href="')
                        __M_writer(str(_link('tag', tag)))
                        __M_writer('">#')
                        __M_writer(filters.html_escape(str(tag)))
                        __M_writer('</a>\n')
                __M_writer('        </div>\n')
            __M_writer('        <h2 class="subtitle is-6 date">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</h2>\n        <h1 class="title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n        <div class="content">\n')
            if index_teasers:
                __M_writer('                ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('                ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('        </div>\n    </article>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def content_header():
            return render_content_header(context)
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/kiss/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "35": 6, "41": 0, "76": 2, "77": 3, "78": 4, "79": 5, "80": 6, "81": 7, "86": 15, "91": 56, "97": 9, "110": 9, "111": 10, "112": 10, "113": 11, "114": 12, "115": 12, "116": 12, "117": 14, "118": 14, "119": 14, "125": 17, "154": 17, "159": 20, "160": 21, "161": 22, "162": 22, "163": 22, "164": 24, "165": 25, "166": 25, "167": 25, "168": 27, "169": 28, "170": 30, "171": 31, "172": 32, "173": 33, "174": 34, "175": 35, "176": 37, "177": 37, "178": 37, "179": 37, "180": 37, "181": 40, "182": 42, "183": 42, "184": 42, "185": 43, "186": 43, "187": 43, "188": 43, "189": 45, "190": 46, "191": 46, "192": 46, "193": 47, "194": 48, "195": 48, "196": 48, "197": 50, "198": 53, "199": 53, "200": 54, "201": 54, "202": 55, "203": 55, "209": 18, "219": 18, "220": 19, "221": 19, "227": 221}}
__M_END_METADATA
"""
