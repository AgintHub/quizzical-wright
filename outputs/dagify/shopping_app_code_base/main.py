import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.add_payment_integration import add_payment_integration
from code.choose_framework import choose_framework
from code.create_ui_component import create_ui_component
from code.implement_customer_auth import implement_customer_auth
from code.integrate_ui_component import integrate_ui_component
from code.plan_shopping_app_features import plan_shopping_app_features
from code.set_up_project_structure import set_up_project_structure
from code.write_product_listing_logic import write_product_listing_logic

# Get async mode from environment variable or default to False
ASYNC_MODE = os.environ.get('ASYNC_MODE', '').lower() in ('true', '1', 'yes', 'y')

def make_async(func):
    """Convert a synchronous function to an asynchronous function.

    If the function is already asynchronous, return it unchanged.
    If the function is synchronous, wrap it in an async function.
    """
    # If it's already a coroutine function, return it as is
    if inspect.iscoroutinefunction(func):
        return func

    # Otherwise, wrap it as an async function
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return async_wrapper

add_payment_integration_async = make_async(add_payment_integration)
choose_framework_async = make_async(choose_framework)
create_ui_component_async = make_async(create_ui_component)
implement_customer_auth_async = make_async(implement_customer_auth)
integrate_ui_component_async = make_async(integrate_ui_component)
plan_shopping_app_features_async = make_async(plan_shopping_app_features)
set_up_project_structure_async = make_async(set_up_project_structure)
write_product_listing_logic_async = make_async(write_product_listing_logic)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: plan_shopping_app_features
    async def run_plan_shopping_app_features():
        # Call the async version of plan_shopping_app_features with results from dependencies
        return await plan_shopping_app_features_async(user_input)

    # Run level 0 nodes in parallel
    results['plan_shopping_app_features'] = await run_plan_shopping_app_features()

    # Level 1: choose_framework
    async def run_choose_framework():
        # Call the async version of choose_framework with results from dependencies
        return await choose_framework_async(results['plan_shopping_app_features'])

    # Run level 1 nodes in parallel
    results['choose_framework'] = await run_choose_framework()

    # Level 2: set_up_project_structure
    async def run_set_up_project_structure():
        # Call the async version of set_up_project_structure with results from dependencies
        return await set_up_project_structure_async(results['choose_framework'])

    # Run level 2 nodes in parallel
    results['set_up_project_structure'] = await run_set_up_project_structure()

    # Level 3: write_product_listing_logic
    async def run_write_product_listing_logic():
        # Call the async version of write_product_listing_logic with results from dependencies
        return await write_product_listing_logic_async(results['set_up_project_structure'])

    # Run level 3 nodes in parallel
    results['write_product_listing_logic'] = await run_write_product_listing_logic()

    # Level 4: add_payment_integration
    async def run_add_payment_integration():
        # Call the async version of add_payment_integration with results from dependencies
        return await add_payment_integration_async(results['write_product_listing_logic'])

    # Run level 4 nodes in parallel
    results['add_payment_integration'] = await run_add_payment_integration()

    # Level 5: implement_customer_auth
    async def run_implement_customer_auth():
        # Call the async version of implement_customer_auth with results from dependencies
        return await implement_customer_auth_async(results['add_payment_integration'])

    # Run level 5 nodes in parallel
    results['implement_customer_auth'] = await run_implement_customer_auth()

    # Level 6: create_ui_component
    async def run_create_ui_component():
        # Call the async version of create_ui_component with results from dependencies
        return await create_ui_component_async(results['implement_customer_auth'])

    # Run level 6 nodes in parallel
    results['create_ui_component'] = await run_create_ui_component()

    # Level 7: integrate_ui_component
    async def run_integrate_ui_component():
        # Call the async version of integrate_ui_component with results from dependencies
        return await integrate_ui_component_async(results['create_ui_component'])

    # Run level 7 nodes in parallel
    results['integrate_ui_component'] = await run_integrate_ui_component()

    # Return all results
    return results

def run_workflow_sync(user_input: str) -> Dict[str, Any]:
    """Synchronous wrapper around the async workflow execution."""
    return asyncio.run(run_workflow(user_input))

def main():
    """Main entry point.

    Handles arguments in the following priority:
    1. Command-line argument (sys.argv[1])
    2. If no argument, uses empty string as input but displays a warning.
    """
    # Get user input from command line or use empty string
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # No input provided - display help message but continue with empty string
        print('Warning: No input provided. Using empty string as input.')
        print('For better results, provide an input argument:')
        print(f'  python {os.path.basename(__file__)} "your input text here"')
        print('Or use a file as input:')
        print(f'  python {os.path.basename(__file__)} "$(cat input.txt)"')
        user_input = ""

    print(f'Running workflow with input: {user_input}')

    # Run the workflow
    results = run_workflow_sync(user_input)

    # Print results
    try:
        # Convert results to JSON
        json_results = json.dumps(results, indent=2, default=str)
        print(json_results)
    except (TypeError, ValueError) as e:
        print(f'Results could not be converted to JSON: {e}')
        print(f'Raw results: {results}')

    return results

if __name__ == '__main__':
    main()
