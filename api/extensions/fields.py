from django.core.urlresolvers import NoReverseMatch

from rest_framework.reverse import reverse
from rest_framework.fields import Field


class ReverseField(Field):
    """
    A field that gets its value by reversing a view name with the provied
    args and kwargs.
    """

    def __init__(self, viewname, args=None, kwargs=None, silent=False):
        self.viewname = viewname
        self.args = args or []
        self.kwargs = kwargs or {}
        self.silent = silent
        super(ReverseField, self).__init__()

    def get_args(self, obj):
        """
        Get args based on object.
        """
        return tuple(_getattr(obj, arg) for arg in self.args)

    def get_kwargs(self, obj):
        """
        Get kwargs based on object.
        """
        kwargs = {}
        for key, value in self.kwargs.iteritems():
            kwargs[key] = _getattr(obj, value)
        return kwargs

    def field_to_native(self, obj, field_name):
        if obj.pk is None:
            return self.to_native(None)
        request = self.parent.context.get('request')
        try:
            value = reverse(self.viewname, args=self.get_args(obj),
                            kwargs=self.get_kwargs(obj), request=request)
        except NoReverseMatch:
            if not self.silent:
                raise
            value = None
        return self.to_native(value)
