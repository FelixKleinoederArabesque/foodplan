from enum import Enum


class Unit_Type(Enum):
    TEA_SPOON = 0
    TABLE_SPOON = 1

    MILLILITER = 2
    LITER = 3

    GRAM = 4
    KILOGRAM = 5

    PIECE = 6


def convert(amount: float, input_unit_type: Unit_Type, output_unit_type: Unit_Type):
    if input_unit_type == output_unit_type:
        return amount

    if (
        input_unit_type == Unit_Type.MILLILITER or input_unit_type == Unit_Type.LITER
    ) and (
        output_unit_type == Unit_Type.MILLILITER or output_unit_type == Unit_Type.LITER
    ):
        return convert_volumes(amount, input_unit_type, output_unit_type)

    elif (
        input_unit_type == Unit_Type.GRAM or input_unit_type == Unit_Type.KILOGRAM
    ) and (
        output_unit_type == Unit_Type.GRAM or output_unit_type == Unit_Type.KILOGRAM
    ):
        return convert_weights(amount, input_unit_type, output_unit_type)

    else:
        raise f"Invalid unit conversions from {input_unit_type} to {output_unit_type}."


def convert_volumes(
    amount: float, input_unit_type: Unit_Type, output_unit_type: Unit_Type
):
    if input_unit_type == Unit_Type.MILLILITER and output_unit_type == Unit_Type.LITER:
        return amount / 1000

    if input_unit_type == Unit_Type.LITER and output_unit_type == Unit_Type.MILLILITER:
        return amount * 1000


def convert_weights(
    amount: float, input_unit_type: Unit_Type, output_unit_type: Unit_Type
):
    if input_unit_type == Unit_Type.GRAM and output_unit_type == Unit_Type.KILOGRAM:
        return amount / 1000

    if input_unit_type == Unit_Type.KILOGRAM and output_unit_type == Unit_Type.GRAM:
        return amount * 1000
