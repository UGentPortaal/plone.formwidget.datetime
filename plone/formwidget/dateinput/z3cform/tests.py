import doctest
import unittest
from zope.app.testing import setup
from z3c.form.testing import TestRequest
from z3c.form.interfaces import IFieldWidget

from Testing import ZopeTestCase as ztc
from StringIO import StringIO
import z3c.form
import zope.schema
import zope.component
import zope.app.component
import plone.formwidget.dateinput.z3cform
from zope.configuration import xmlconfig


class WidgetTestCase(object):

    def setUp(self):
        self.root = setup.placefulSetUp(True)
        xmlconfig.XMLConfig('meta.zcml', zope.component)()
        xmlconfig.XMLConfig('meta.zcml', zope.app.component)()
        try:
            xmlconfig.XMLConfig('configure.zcml', zope.i18n)()
        except IOError:
            # Zope 2.10
            xmlconfig.xmlconfig(StringIO('''
            <configure xmlns="http://namespaces.zope.org/zope">
               <utility
                  provides="zope.i18n.interfaces.INegotiator"
                  component="zope.i18n.negotiator.negotiator" />

               <include package="zope.i18n.locales" />
            </configure>
             '''))
        xmlconfig.XMLConfig('meta.zcml', zope.i18n)()
        xmlconfig.XMLConfig('meta.zcml', z3c.form)()
        xmlconfig.XMLConfig('configure.zcml', plone.formwidget.dateinput.z3cform)()

    def tearDown(self):
        setup.placefulTearDown()

    def testrequest(self, lang="en", form={}):
        return TestRequest(HTTP_ACCEPT_LANGUAGE=lang, form=form)

    def setupWidget(self, field, lang="en"):
        request = self.testrequest(lang=lang)
        widget = zope.component.getMultiAdapter((field, request),
                                                IFieldWidget)
        widget.id = 'foo'
        widget.name = 'bar'
        return widget


def test_suite():
    return unittest.TestSuite((
        ztc.ZopeDocFileSuite(
            'widget_date.txt',
            'widget_datetime.txt',
            'widget_monthyear.txt',
            'converter.txt',
            'issues.txt',
            test_class=WidgetTestCase,
            optionflags=
                        doctest.NORMALIZE_WHITESPACE |
                        doctest.ELLIPSIS |
                        doctest.REPORT_UDIFF,
            ),
        ))

