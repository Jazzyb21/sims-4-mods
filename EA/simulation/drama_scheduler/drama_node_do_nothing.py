from drama_scheduler.drama_node import BaseDramaNode, DramaNodeRunOutcomefrom sims4.utils import classproperty
class DoNothingDramaNode(BaseDramaNode):

    @classproperty
    def simless(cls):
        return True

    def _run(self):
        return DramaNodeRunOutcome.SUCCESS_NODE_COMPLETE
