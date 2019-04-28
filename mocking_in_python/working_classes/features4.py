import random


class Features4:
    def call_prod(self):
        prod = self.get_product()

        if prod == 'PVE':
            artifact = 'project'
            self.call_pve(artifact)
        elif prod == 'PP':
            artifact = 'workspace'
            self.call_pp(artifact)
        elif prod == 'Innotas':
            artifact = 'in_project'
            self.call_innotas(artifact)

    def get_product(self):
        prod = random.choice(['PVE', 'PP', 'Innotas'])
        return prod

    def call_pve(self, artifact):
        print('Inside PVE', artifact)

    def wrapper_get_pve(self, artifact):
        self.call_pve(artifact)

    def call_pp(self, artifact):
        print('Inside PP', artifact)

    def call_innotas(self, artifact):
        print('Inside Innotas', artifact)


f = Features4()
f.call_prod()
