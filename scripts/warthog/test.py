from .base import BaseWarthogTest
class TestVcsr(BaseWarthogTest):

    def test_ping_across_the_pods(self):
        self.logger.info('Test1.test_1')
        agent = self.connections.agent_inspect[self.inputs.compute_ips[0]]
        import pdb; pdb.set_trace()
        pod = self.setup_nginx_pod()
        assert pod.verify_on_setup()

