from pydantic import BaseModel, Field
from typing import List


class ChooseFrameworkOutput(BaseModel):
    """Pydantic model for choose_framework node outputs."""
    tech_stack: str = (
        Field(..., description="The chosen tech stack for the shopping app (e.g., React Native, Flutter)")
    )
    framework: str = (
        Field(..., description="The chosen framework for the shopping app")
    )
    justification: str = (
        Field(..., description="A 2-sentence justification for the chosen tech stack and framework")
    )


class SetUpProjectStructureOutput(BaseModel):
    """Pydantic model for set_up_project_structure node outputs."""
    project_name: str = Field(..., description="The name of the project")
    directory_structure: List[str] = (
        Field(..., description="A list of key directories in the project structure")
    )
    file_list: List[str] = (
        Field(..., description="A list of key files in the project structure")
    )
    is_valid: bool = (
        Field(..., description="Whether the project structure is valid")
    )


def set_up_project_structure(choose_framework_input: ChooseFrameworkOutput, **kwargs) -> SetUpProjectStructureOutput:
    """
    Sets up a basic project structure for the shopping app based on the chosen
    framework.

    Parameters
    ----------
    chosen_framework : str
        The chosen framework for the shopping app
    project_name : str
        The name of the project

    Returns
    -------
    dict
        A dictionary containing the project name, directory structure, file
        list, and validity of the project structure

    Raises
    ------
    ValueError
        If the chosen framework or project name is invalid

    Examples
    --------
    >>> set_up_project_structure(chosen_framework='React Native',
    project_name='ShoppingApp')
    >>> print(output['project_name'])  # Output: ShoppingApp
    >>> print(output['directory_structure'])  # Output: ['src', 'tests', 'docs']
    >>> print(output['file_list'])  # Output: ['index.js', 'App.js',
    'package.json']
    >>> print(output['is_valid'])  # Output: True
    {'project_name': 'ShoppingApp', 'directory_structure': ['src', 'tests',
    'docs'], 'file_list': ['index.js', 'App.js', 'package.json'], 'is_valid':
    True}

    """
    return SetUpProjectStructureOutput(
        project_name="",
        directory_structure=[],
        file_list=[],
        is_valid=False,
    )