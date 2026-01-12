from pydantic import BaseModel, Field
from typing import List


class WriteProductListingLogicOutput(BaseModel):
    """Pydantic model for write_product_listing_logic node outputs."""
    product_list: List[str] = Field(..., description="List of product names")
    product_descriptions: List[str] = (
        Field(..., description="List of product descriptions")
    )
    product_prices: List[float] = (
        Field(..., description="List of product prices")
    )
    is_product_listing_successful: bool = (
        Field(..., description="Whether the product listing logic was successfully implemented")
    )


class AddPaymentIntegrationOutput(BaseModel):
    """Pydantic model for add_payment_integration node outputs."""
    payment_gateway: str = (
        Field(..., description="The name of the integrated payment gateway")
    )
    transaction_processing_status: bool = (
        Field(..., description="Whether the transaction processing logic has been successfully implemented")
    )
    receipt_generation_status: bool = (
        Field(..., description="Whether the receipt generation logic has been successfully implemented")
    )
    supported_payment_methods: List[str] = (
        Field(..., description="List of supported payment methods (e.g., credit card, PayPal, etc.)")
    )


def add_payment_integration(write_product_listing_logic_input: WriteProductListingLogicOutput, **kwargs) -> AddPaymentIntegrationOutput:
    """
    Integrate a payment gateway into the shopping app and return integration
    status.

    Returns
    -------
    dict
        A dictionary containing the payment gateway name, boolean flags for
        transaction processing and receipt generation success, and a list of
        supported payment methods.

    Raises
    ------
    ValueError
        Raised if the payment gateway configuration is missing or invalid.

    Examples
    --------
    >>> result = add_payment_integration()
    {
      "payment_gateway": "Stripe",
      "transaction_processing_status": true,
      "receipt_generation_status": true,
      "supported_payment_methods": ["credit_card", "debit_card", "paypal"]
    }

    >>> result = add_payment_integration()
    {
      "payment_gateway": "PayPal",
      "transaction_processing_status": true,
      "receipt_generation_status": false,
      "supported_payment_methods": ["paypal", "credit_card"]
    }

    """
    return AddPaymentIntegrationOutput(
        payment_gateway="",
        transaction_processing_status=False,
        receipt_generation_status=False,
        supported_payment_methods=[],
    )