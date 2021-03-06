from django.apps import AppConfig


class QuilljsConfig(AppConfig):

    """Base configuration for django-quilljs."""

    name = 'quilljs'

    editor_selector = 'editor'
    toolbar_selector = 'toolbar'
    theme = 'snow'
    allowed_image_extensions = ['jpg', 'jpeg', 'png', 'gif']

    full = {
        'editor_template': 'quill/editor.html',
        'toolbar_template': 'quill/toolbars/full.html',
        'template': 'quill/widget.html',
    }
    basic = dict(full, toolbar_template='quill/toolbars/basic.html')
    default = full
