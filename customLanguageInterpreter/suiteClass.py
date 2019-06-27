from testClass import testClass

class suiteClass:

    # This class coincides with the concept of the test suite
    def __init__(self):
        # This is the list of test cases being initialized
        self.testCasesList = []
        # This is the type of App APK for which this test suite is for
        self.targetAppCategory = ""


    def setTargetAppCategory(self, appCategory):
        self.targetAppCategory = appCategory

    def addTestObject(self, testObject):
        self.testCasesList.append(testObject)

