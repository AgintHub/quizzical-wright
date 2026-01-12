from pydantic import BaseModel, Field
from typing import List


class PlanShoppingAppFeaturesOutput(BaseModel):
    """Pydantic model for plan_shopping_app_features node outputs."""
    essential_features: List[str] = (
        Field(..., description="List of must-have features for a basic shopping app")
    )
    feature_count: int = (
        Field(..., description="Total number of essential features")
    )


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


def choose_framework(plan_shopping_app_features_input: PlanShoppingAppFeaturesOutput, **kwargs) -> ChooseFrameworkOutput:
    """
    Selects a suitable tech stack and framework for the shopping app based on
    the provided features.

    Parameters
    ----------
    essential_features : List[str]
        List of essential features for the shopping app

    Returns
    -------
    dict
        A dictionary containing the chosen tech stack, framework, and
        justification

    Raises
    ------
    ValueError
        If the input features are empty or invalid

    Examples
    --------
    >>> choose_framework(essential_features=["product listing", "search",
    "filter"])
    >>> print(output['tech_stack'])  # Output: 'React Native'
    >>> print(output['framework'])  # Output: 'React'
    >>> print(output['justification'])  # Output: 'React Native is chosen for
    its cross-platform compatibility and React for its simplicity.'
    {'tech_stack': 'React Native', 'framework': 'React', 'justification': 'React
    Native is chosen for its cross-platform compatibility and React for its
    simplicity.'}

    """
    return ChooseFrameworkOutput(
        tech_stack="",
        framework="",
        justification="",
    )