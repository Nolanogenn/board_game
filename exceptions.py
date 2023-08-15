class NotEnoughResources(Exception):
    def __init__(self, original_amount, quantity_to_pay, resource_name):
        self.original_amount = original_amount
        self.quantity_to_pay = quantity_to_pay
        self.resource_name = resource_name
        message = f"You cannot pay {self.quantity_to_pay} of {self.resource_name} since you only have {self.original_amount}"
        super().__init__(message)


class NotValidResource(Exception):
    def __init__(self,valid_resources):
        self.valid_resource = valid_resources
        message = f"Resource name not in {self.valid_resource}"
        super().__init__(message)
