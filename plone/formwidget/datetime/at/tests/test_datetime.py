import unittest2 as unittest
from plone.formwidget.datetime.at.testing import PFWDTAT_INTEGRATION_TESTING

class DatetimeATTest(unittest.TestCase):
    layer = PFWDTAT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.portal.invokeFactory(id='dttype1',
                          title='Datetime Type 1',
                          type_name='DatetimeWidgetType')
        self.obj = self.portal['dttype1']

    def get_field(self, fieldname):
        return self.obj.getField(fieldname) 

    def get_widget(self, fieldname):
        field = get_field(fieldname)
        return self.field.widget

    def test_datewidget_properties(self):
        widget = self.get_widget('datefield')
        self.assertEqual(widget.macro, 'date_input')
        self.assertEqual(widget.value, widget.empty_value)
        self.assertEqual(widget.with_time, False)
        self.assertEqual(widget.show_day, True)

    def test_datewidget_process(self):
        widget = self.get_widget('datefield')
        field = self.get_field('datefield')
        self.assertFalse(widget.process_form(self.obj, field, {}))

    def test_datetimewidget_properties(self):
        widget = self.get_widget('datetimefield')
        self.assertEqual(widget.macro, 'datetime_input')
        self.assertEqual(widget.value, widget.empty_value)
        self.assertEqual(widget.with_time, True)
        self.assertEqual(widget.ampm, 1)

    def test_datetimewidget_process(self):
        widget = self.get_widget('datetimefield')
        field = self.get_field('datetimefield')
        self.assertFalse(widget.process_form(self.obj, field, {}))

    def test_monthyearwidget_properties(self):
        widget = self.get_widget('monthyearfield')
        self.assertEqual(widget.macro, 'monthyear_input')
        self.assertEqual(widget.value, widget.empty_value)
        self.assertEqual(widget.show_day, False)

    def test_monthyearwidget_process(self):
        widget = self.get_widget('monthyearfield')
        field = self.get_field('monthyearfield')
        self.assertFalse(widget.process_form(self.obj, field, {}))
