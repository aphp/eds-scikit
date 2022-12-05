import catalogue


class Registry:

    data = catalogue.create(
        "eds_scikit",
        "data",
        entry_points=True,
    )

    misc = catalogue.create(
        "eds_scikit",
        "misc",
        entry_points=True,
    )

    def get(
        self,
        key: str,
        function_name: str,
    ):
        """
        Get a function from one of the registry

        Parameters
        ----------
        key : str
            The registry's name. The function will be retrieved from self.<key>
        function_name : str
            The function's name, The function will be retrieved via self.<key>.get(function_name).
            Can be of the form "function_name.version"

        Returns
        -------
        Callable
            The registered function
        """

        if not hasattr(self, key):
            raise ValueError(f"eds-scikit's registry has no {key} key !")
        r = getattr(self, key)
        candidates = r.get_all().keys()

        if function_name in candidates:
            # Exact match
            func = r.get(function_name)

        else:
            # Looking for a match excluding version string
            candidates = [
                func for func in candidates if function_name == func.split(".")[0]
            ]
            if len(candidates) > 1:
                # Multiple versions available, a specific one should be specified
                raise ValueError(
                    (
                        f"Multiple functions are available under the name {function_name} :\n"
                        f"{candidates}\n"
                        "Please choose one of the implementation listed above."
                    )
                )
            if not candidates:
                # No registered function
                raise ValueError(
                    (
                        f"No function registered under the name {function_name} "
                        f"was found in eds-scikit's {key} registry.\n"
                        "If you work in AP-HP's ecosystem, you should install "
                        'extra resources via `pip install "eds-scikit[aphp]"'
                        "You can define your own and decorate it as follow:\n"
                        "from eds_scikit.resources import registry\n"
                        f"@registry.{key}('{function_name}')"
                        f"def your_custom_func(args, **kwargs):",
                        "   ...",
                    )
                )
            func = r.get(candidates[0])
        return func


registry = Registry()
