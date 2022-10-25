all_feature_names = ['nested_scopes', 'generators', 'division', 'absolute_import', 'with_statement', 'print_function', 'unicode_literals', 'barry_as_FLUFL', 'generator_stop', 'annotations']
class _Feature:

    def __init__(self, optionalRelease, mandatoryRelease, compiler_flag):
        self.optional = optionalRelease
        self.mandatory = mandatoryRelease
        self.compiler_flag = compiler_flag

    def getOptionalRelease(self):
        return self.optional

    def getMandatoryRelease(self):
        return self.mandatory

    def __repr__(self):
        return '_Feature' + repr((self.optional, self.mandatory, self.compiler_flag))
