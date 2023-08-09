SELECTORS = {
    'blog.csdn.net': {
        'name': 'CSDN',
        'title': '#articleContentId',
        'article': '#js_content',
    },
    'mp.weixin.qq.com': {
        'name': '微信公众号',
        'title': '#activity-name',
        'article': '#js_content',
    },
    'zhuanlan.zhihu.com': {
        'name': '知乎',
        'title': '.Post-Title',
        'article': '.Post-RichText',
    },
    'www.jianshu.com': {
        'name': '简书',
        'title': '._1RuRku',
        'article': 'article',
    },
    'www.seqchina.cn': {
        'name': '测序中国',
        'title': '.post-head h2',
        'article': '.content-post',
    },
    'www.plob.org': {
        'name': 'PLoB',
        'title': '.entry-title',
        'article': '.single-content',
    },
    'www.163.com': {
        'name': '网易',
        'title': '.post_title',
        'article': '.post_body',
    },
    'cloud.tencent.com': {
        'name': '腾讯云社区',
        'title': '.title-text',
        'article': '.rno-markdown',
    },
    'www.sohu.com': {
        'name': '搜狐',
        'title': '.text-title h1',
        'article': 'article',
    },
    'www.cn-healthcare.com': {
        'name': '健康界',
        'title': '.dt_left_wraps h1',
        'article': '.wz-textbox',
    },
}

DEFAULT_SELECTOR = {
    'title': 'title',
    'article': 'body',
}
