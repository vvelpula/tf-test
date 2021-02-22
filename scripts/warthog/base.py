from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import test
from tcutils.kubernetes.api_client import Client as Kubernetes_client
from tcutils.util import custom_dict
from tcutils.agent.vna_introspect_utils import AgentInspect
from common.k8s.base import K8sMixin

class WarthogConnections:

    def __init__(self, inputs, logger):
        self.inputs = inputs
        self.logger = logger
        self.vnc_lib = None
        self.agent_inspect = custom_dict(self.get_vrouter_agent_inspect_handle,
                                         'agent_inspect')
        self.k8s_client = Kubernetes_client(self.inputs.kube_config_file,
                                            self.logger)
        #self.verification_funcs = {
        #    'api-server': False,
        #    'control': False,
        #    'kube-manager': False,
        #    'vrouter-agent': True
        #}
    def get_vrouter_agent_inspect_handle(self, host):
        if host not in self.agent_inspect:
            self.agent_inspect[host] = AgentInspect(host,
                                           port=self.inputs.agent_port,
                                           logger=self.logger,
                                           inputs=self.inputs,
                                           protocol=self.inputs.introspect_protocol)
        return self.agent_inspect[host]


class BaseWarthogTest(test.BaseTestCase, K8sMixin):

    @classmethod
    def setUpClass(cls):
        super(BaseWarthogTest, cls).setUpClass()
        import pdb; pdb.set_trace()
        cls.connections = WarthogConnections(cls.inputs, cls.logger)

    @classmethod
    def tearDownClass(cls):
        super(BaseWarthogTest, cls).tearDownClass()
