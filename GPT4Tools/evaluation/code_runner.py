import sys
import ast
from typing import Callable, Mapping, Optional
import logging

import astor

# from python_interpreter import evaluate

# setup logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handle = logging.StreamHandler()
stream_handle.setLevel(logging.INFO)
stream_handle_format = logging.Formatter("%(levelname)s - %(asctime)s - %(message)s")
stream_handle.setFormatter(stream_handle_format)
logger.addHandler(stream_handle)


class CodeRunner:
    def __init__(self) -> None:
        self.reset_state()

    def reset_state(self):
        self.state = {}
        # keep tool collection in case we need it
        self.tools = {}
        logger.info("Reset State")

    def run(self, code: str, tools: Optional[Mapping[str, Callable]] = None):
        """
        Assumes that the last line is a tool usage.
        Returns last line result
        """

        if tools is not None:
            self.add_tools(tools)

        # !!! unsafe af
        try:
            preprocessed_code, result_var_name = self.preprocess_code(code)
            logger.info(f"preprocessed_code:\n{preprocessed_code}")
            exec(preprocessed_code, {}, self.state)
            # todo: extract output
            return self.extract_result(result_var_name)
        except Exception as e:
            return f"EXEC ERROR: {e}"

    def extract_result(self, var_name):
        return self.state[var_name]

    def add_tools(self, new_tools: Mapping[str, Callable]):
        logger.info("Adding tools...")
        for new_tool in new_tools:
            if new_tool in self.tools:
                logger.warn(f"tool {new_tool} already exists. replacing.")

        self.tools |= new_tools
        self.state |= new_tools
        logger.info(f"Added tools: {list(new_tools.keys())}")

    def remove_tools(self, tools):
        # for now, tools persist in state till reset
        raise NotImplementedError

    @staticmethod
    def preprocess_code(code: str):
        """Adds assignment to the last expression

        Returns:
            modified_code, result variable name
        """

        # ===== Sophisticated method (kostyl) =====
        tree = ast.parse(code)
        # in case of an empty tree return empty string
        if len(tree.body) < 1:
            return 'res = ""', 'res'
        last_expr = tree.body[-1]
        if isinstance(last_expr, ast.Expr):
            result_var_name = "res"
            # replace `func(args)` with `res = func(args)`
            tree.body[-1] = ast.Assign(
                targets=[ast.Name(result_var_name)], value=last_expr.value
            )
        # if line is assignment, return assignment target variable
        elif isinstance(last_expr, ast.Assign):
            result_var_name = last_expr.targets[0].id
        else:
            result_var_name = None

        return astor.to_source(tree), result_var_name
