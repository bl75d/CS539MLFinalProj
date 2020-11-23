class Abstract_Model():
    """
    An abstract model class for setting up common elements amongst models. Subclasses should override abstract functions.
    """

    def __init__(self, kwargs):
        """
        initialize the model. Set kwargs to correct related variables. Set defaults if values not provided.

        Args:
            kwargs (dict): key,value pairs of variables to set.
        """

        self.train_data_shape = kwargs.get("train_data_shape", (10,5,1000))
        self.dropout_rate = kwargs.get("dropout_rate", 0.2)
        self.layer_width = kwargs.get("layer_width", 15)

    def generate(self):
        """
        Abstract method for generating the model.

        Raises:
            NotImplementedError: Warn the user to not call this sub function.
        """

        raise NotImplementedError("Method not implemented!")