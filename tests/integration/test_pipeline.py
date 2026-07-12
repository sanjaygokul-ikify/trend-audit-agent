import unittest
from packages.core import ModelInterface, ExecutionConfig, Task, ExecutionResult, LogEntry
from packages.core.exceptions import ExecutionException
from services.orchestrator import OrchestratorService


class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        model_name = 'test_model'
        sandbox_enabled = True
        execution_config = ExecutionConfig(sandbox_enabled=sandbox_enabled)
        model_interface = ModelInterface(model_name=model_name)
        task = Task()
        orchestrator_service = OrchestratorService(execution_config)
        try:
            result = orchestrator_service.schedule_execution(task)
            self.assertIsInstance(result, ExecutionResult)
        except ExecutionException as e:
            self.fail(f"Test failed with exception: {str(e)}")

if __name__ == '__main__':
    unittest.main()
