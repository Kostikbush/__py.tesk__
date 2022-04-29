class AttrDisplay:
    def gatherAttrs(this):
        attrs = []
        for key in sorted(this.__dict__):
            attrs.append('%s=%s' % (key, getattr(this, key)))
        return ', '.join(attrs)
    def __str__(this):
        return '[%s: %s]' % (this.__class__.__name__, this.gatherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(this):
            this.attr1 = TopTest.count
            this.attr2 = TopTest.count+1
            TopTest.count += 2

    class SubTest(TopTest):
        pass
    X, Y = TopTest(), SubTest()
    print(X) # Выведет все атрибуты экземпляра
    print(Y) # Выведет имя класса, 
        # самого близкого в дереве наследования
