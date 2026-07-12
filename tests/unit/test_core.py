import unittest
from packages.core import ModelInterface, ExecutionConfig, Task, ExecutionResult, LogEntry
from packages.core.exceptions import ExecutionException


class TestCore(unittest.TestCase):
    def test_model_interface(self):
        model_name = 'test_model'
        model_interface = ModelInterface(model_name=model_name)
        self.assertEqual(model_interface.model_name, model_name)

    def test_execution_config(self):
        sandbox_enabled = True
        execution_config = ExecutionConfig(sandbox_enabled=sandbox_enabled)
        self.assertEqual(execution_config.sandbox_enabled, sandbox_enabled)

    def test_task(self):
        task = Task()
        self.assertIsInstance(task, Task)

    def test_execution_result(self):
        result = 'test_result'
        execution_result = ExecutionResult(result=result)
        self.assertEqual(execution_result.result, result)

    def test_log_entry(self):
        log_id = 'test_log_id'
        log_data = 'test_log_data'
        log_entry = LogEntry(id=log_id, data=log_data)
        self.assertEqual(log_entry.id, log_id)
        self.assertEqual(log_entry.data, log_data)

    def test_execution_exception(self):
        execution_exception = ExecutionException('Test execution exception')
        self.assertIsInstance(execution_exception, ExecutionException)
        self.assertEqual(str(execution_exception), 'Test execution exception')

if __name__ == '__main__':
    unittest.main()
