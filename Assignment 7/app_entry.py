#!/usr/bin/env python3
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


target = Path(__file__).resolve().parent / "102313049_program2.py"
spec = spec_from_file_location("assignment7_program2", target)
module = module_from_spec(spec)
spec.loader.exec_module(module)
app = module.app
