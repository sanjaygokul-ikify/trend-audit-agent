import unittest
from packages.core import OrchestratorEngine
from packages.core.exceptions import ExecutionException


class TestRuntime(unittest.TestCase):
    def test_orchestrator_engine(self):
        execution_config = ExecutionConfig(sandbox_enabled=True)
        orchestrator_engine = OrchestratorEngine(execution_config)
        self.assertIsInstance(orchestrator_engine, OrchestratorEngine)

    def test_schedule_execution(self):
        execution_config = ExecutionConfig(sandbox_enabled=True)
        orchestrator_engine = OrchestratorEngine(execution_config)
        task = Task()
        try:
            result = orchestrator_engine.schedule_execution(task)
            self.assertIsInstance(result, ExecutionResult)
        except ExecutionException as e:
            self.fail(f"Test failed with exception: {str(e)}")

if __name__ == '__main__':
    unittest.main()
