from abc import ABC, abstractmethod

from mistral_lib import actions

from sporact_lib.exceptions.exceptions import SporactValueError


class SporactAction(actions.Action, ABC):
    def __init__(self, *args, **kwargs):
        # store the incoming params
        self.tenant_id = None
        if kwargs.get('tenant_id'):
            self.tenant_id = kwargs.get('tenant_id')
        else:
            raise SporactValueError('Tenant id not passed')

    @abstractmethod
    def run(self, context):
        pass
