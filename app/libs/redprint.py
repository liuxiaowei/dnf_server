
class Redprint:
    def __init__(self, name):
        self.name = name
        self.mount = []

    def route(self, rule, **options):
        def decorator(f):
            self.mount.append((rule, f, options))
            return f
        return decorator

    def register(self, blueprint, prefix=None):
        if prefix is None:
            prefix = '/' + self.name

        for rule, f, options in self.mount:
            endpoint = options.pop("endpoint", f.__name__)
            blueprint.add_url_rule(prefix + rule, endpoint, f, **options)