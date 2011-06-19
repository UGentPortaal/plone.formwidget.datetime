from plone.formwidget.datetime.testing import PFWDTLayer
from plone.app.testing import IntegrationTesting
from plone.testing import z2

class PFWDTATLayer(PFWDTLayer):

    def setUpZope(self, app, configurationContext):
        super(PFWDTATLayer, super).setupZope(app, configurationContext)
        # Load ZCML
        import plone.formwidget.datetime.at
        self.loadZCML(package=plone.formwidget.datetime.at)

        import plone.formwidget.datetime.at.tests.examples
        self.loadZCML(package=plone.formwidget.datetime.at.tests.examples)

        # Install product and call its initialize() function
        z2.installProduct(app, 'plone.formwidget.datetime.at.tests.examples')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(
                portal,
                'plone.formwidget.datetime.at.tests.examples:examples')

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'plone.formwidget.datetime.at.tests.examples')

PFWDTAT_FIXTURE = PFWDTATLayer()
PFWDTAT_INTEGRATION_TESTING = IntegrationTesting(
        bases=(PFWDTAT_FIXTURE,),
        name="PFWDTAT:Integration")
